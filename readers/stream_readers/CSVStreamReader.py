from collections.abc import Iterator
from datetime import datetime
from typing import Any

from omf_sample_library_preview.Converters import convert
from omf_sample_library_preview.Models import (
    OMFContainer,
    OMFData,
    OMFFormatCode,
    OMFType,
)

from data_types import StreamTypeEnum

from ..CSVTransformer import CSVTransformer
from .BackfillableStreamReader import BackfillableStreamReader


class CSVStreamReader(BackfillableStreamReader):
    def __init__(
        self, id: str, name: str, file_path: str, data_class: type, omf_type: OMFType
    ):
        super().__init__(id, name)
        self.__file_path = file_path
        self.__data_class = data_class
        self.__omf_type = omf_type

        self.__index_property = next(
            iter(
                [
                    id
                    for id, prop in self.__omf_type.Properties.items()
                    if prop.IsIndex and prop.Format is OMFFormatCode.DateTime
                ]
            )
        )

        self.__reader = CSVTransformer(
            self.__file_path, self.__data_class, self.__index_property
        )

        self.__current_value = None
        self.__current_value_time = None
        self.__start_time_csv = self.__reader.get_data_start()

    def get_stream(self) -> OMFContainer:
        return OMFContainer(self.id, self.__omf_type.Id, self.name)

    def get_type(self) -> OMFType:
        return self.__omf_type

    def __get_values(
        self, start_time: datetime, end_time: datetime
    ) -> Iterator[(datetime, OMFData)]:
        if not self.__reader.offset:
            self.__reader.offset = start_time - self.__start_time_csv

        last_time = start_time
        while end_time > last_time:
            next_data = next(self.__reader, None)
            value = self.__data_class(**next_data)
            last_time = getattr(value, self.__index_property)

            if self.__current_value:
                yield (
                    last_time,
                    OMFData[self.__data_class](
                        [self.__current_value], ContainerId=self.id
                    ),
                )

            self.__current_value = value

    def read_data(self, now: datetime) -> Iterator[OMFData]:
        if not self.__current_value_time:
            self.__current_value_time = getattr(self.__current_value, self.__index_property)

        for last_time, value in self.__get_values(self.__current_value_time, now):
            self.__current_value_time = last_time
            for observer in self.observers:
                observer(value)
            yield value

    def read_backfill(
        self, start_time: datetime, end_time: datetime
    ) -> Iterator[OMFData]:
        for _, value in self.__get_values(start_time, end_time):
            for observer in self.observers:
                observer(value)
            yield value

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'CSVStreamReader':
        data_class = StreamTypeEnum[content['DataClass']].value
        result = CSVStreamReader(
            content['Id'],
            content['Name'],
            content['FilePath'],
            data_class,
            convert(data_class),
        )

        return result

    def toDictionary(self) -> dict[str, Any]:
        result = {
            'Reader': 'CSVStreamReader',
            'Id': self.id,
            'Name': self.name,
            'FilePath': self.__file_path,
            'DataClass': StreamTypeEnum(self.__data_class).name,
        }

        return result
