import uuid
from collections.abc import Iterator
from datetime import datetime
from typing import Any, Generic, TypeVar

from adh_sample_library_preview import (
    AuthorizationTag,
    BaseEvent,
    Enumeration,
    EventType,
    SdsUom,
)

from data_types import EventTypeEnum, AuthorizationTagEnum, EnumEnum

from ..CSVTransformer import CSVTransformer
from ..GraphData import GraphData
from .BackfillableEventReader import BackfillableEventReader

T = TypeVar('T')


class CSVEventReader(BackfillableEventReader, Generic[T]):
    def __init__(
        self,
        id: str,
        name: str,
        file_path: str,
        event_class: type,
        event_type: EventType,
        authorization_tags: list[AuthorizationTag] = None,
        enumerations: list[Enumeration] = None,
        units_of_measure: dict[str, SdsUom] = None,
        reference_asset: str = None,
    ):
        super().__init__(id, name, reference_asset)
        self.__event_class = event_class
        self.__event_type = event_type
        self.__authorization_tags = authorization_tags if authorization_tags else []
        self.__enumerations = enumerations if enumerations else []
        self.__file_path = file_path
        self.__units_of_measure = units_of_measure
        self.__reader = CSVTransformer(
            file_path,
            self.__event_class,
            'StartTime',
            units_of_measure=units_of_measure,
        )

        self.__open_events = []
        self.__current_event = None
        self.__current_event_time = None
        self.__start_time_csv = self.__reader.get_data_start()

    def get_authorization_tags(self) -> list[AuthorizationTag]:
        return self.__authorization_tags

    def get_enumerations(self) -> list[Enumeration]:
        return self.__enumerations

    def get_type(self) -> EventType:
        return self.__event_type

    def __get_events(
        self, start_time: datetime, end_time: datetime
    ) -> Iterator[(datetime, T)]:
        if not self.__reader.offset:
            self.__reader.offset = start_time - self.__start_time_csv

        last_time = start_time
        while end_time > last_time:
            next_event = next(self.__reader, None)
            next_event: BaseEvent = self.__event_class(**next_event)
            last_time = next_event.StartTime

            if self.__current_event:
                self.__open_events.append(self.__current_event)

            self.__current_event = next_event

        event: BaseEvent
        for event in self.__open_events:
            # assign a random id and name if the event does not have one
            if not event.Id:
                event.Id = str(uuid.uuid4())
            if not event.Name:
                event.Name = str(uuid.uuid4())

            if event.EndTime < end_time:
                yield (last_time, event)
                self.__open_events.remove(event)
            else:
                yield (
                    last_time,
                    BaseEvent(
                        Id=event.Id,
                        Name=event.Name,
                        StartTime=event.StartTime,
                    ),
                )

    def read_events(self, now: datetime) -> Iterator[GraphData[T]]:
        if not self.__current_event_time:
            self.__current_event_time = now

        for last_time, value in self.__get_events(self.__current_event_time, now):
            self.__current_event_time = last_time
            yield GraphData([value], self.__event_type.Id)

    def read_backfill(
        self, start_time: datetime, end_time: datetime
    ) -> Iterator[GraphData[T]]:
        for _, value in self.__get_events(start_time, end_time):
            yield GraphData([value], self.__event_type.Id)

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'CSVEventReader':
        event_class = EventTypeEnum[content['EventClass']].value[0]
        event_type = EventTypeEnum[content['EventClass']].value[1]

        authorization_tags = None
        if 'AuthorizationTags' in content and content['AuthorizationTags']:
            authorization_tags = [
                AuthorizationTagEnum[authorization_tag].value
                for authorization_tag in content['AuthorizationTags']
            ]

        enumerations = None
        if 'Enumerations' in content and content['Enumerations']:
            enumerations = [
                EnumEnum[enumeration].value for enumeration in content['Enumerations']
            ]

        units_of_measure = None
        if 'UnitsOfMeasure' in content and content['UnitsOfMeasure']:
            units_of_measure = {
                k: SdsUom.fromJson(uom) for k, uom in content['UnitsOfMeasure'].items()
            }

        result = CSVEventReader(
            content['Id'],
            content['Name'],
            content['FilePath'],
            event_class,
            event_type,
            authorization_tags,
            enumerations,
            units_of_measure,
            content['ReferenceAsset'],
        )

        return result

    def toDictionary(self) -> dict[str, Any]:
        authorization_tags = None
        if self.__authorization_tags:
            authorization_tags = [
                authorization_tag.toDictionary()
                for authorization_tag in self.__authorization_tags
            ]

        enumerations = None
        if self.__enumerations:
            enumerations = [
                enumeration.toDictionary() for enumeration in self.__enumerations
            ]

        units_of_measure = None
        if self.__units_of_measure:
            units_of_measure = {
                k: uom.toDictionary() for k, uom in self.__units_of_measure.items()
            }

        result = {
            'Reader': 'CSVEventReader',
            'Id': self.id,
            'Name': self.name,
            'FilePath': self.__file_path,
            'EventClass': EventTypeEnum((self.__event_class, self.__event_type)).name,
            'AuthorizationTags': authorization_tags,
            'Enumerations': enumerations,
            'UnitsOfMeature': units_of_measure,
            'ReferenceAsset': self.reference_asset,
        }

        return result
