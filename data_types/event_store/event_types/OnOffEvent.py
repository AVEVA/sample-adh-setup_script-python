from dataclasses import dataclass
from typing import Any

from adh_sample_library_preview import (
    BaseEvent,
    EventType,
    PropertyTypeCode,
    TypeProperty,
)

from ..AuthorizationTags import setup_authorization_tag
from ..enums import OnOffStateEnum

_event_type_properties = [
    TypeProperty(
        PropertyTypeCode.Enumeration, 'onOffState', property_type_id='onOffState'
    ),
]

on_off_event_type = EventType(
    _event_type_properties,
    setup_authorization_tag.Id,
    'equipmentOnOffStateEvent',
    id='equipmentOnOffStateEvent',
    version=1,
)


@dataclass
class OnOffEvent(BaseEvent):
    OnOffState: OnOffStateEnum = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'OnOffEvent':
        base = BaseEvent.fromJson(content)
        result = OnOffEvent()
        result.__dict__.update(base.__dict__)

        if 'onOffState' in content:
            result.OnOffState = OnOffStateEnum(content['onOffState'])

        return result

    def toDictionary(self) -> dict[str, Any]:
        result = super().toDictionary()

        if self.OnOffState is not None:
            result['onOffState'] = self.OnOffState.name

        return result
