from dataclasses import dataclass
from typing import Any

from adh_sample_library_preview import (
    BaseEvent,
    EventType,
    PropertyTypeCode,
    TypeProperty,
    UomValueInput,
)

from ..AuthorizationTags import setup_authorization_tag

_event_properties = [
    TypeProperty(PropertyTypeCode.Double, 'DoubleValue', uom='NONE'),
]

double_event_type = EventType(
    _event_properties,
    setup_authorization_tag.Id,
    'myDoubleEvent',
    id='myDoubleEvent',
    version=1,
)


@dataclass
class DoubleEvent(BaseEvent):
    DoubleValue: UomValueInput[float] = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'DoubleEvent':
        base = BaseEvent.fromJson(content)
        result = DoubleEvent()
        result.__dict__.update(base.__dict__)

        if 'doubleValue' in content:
            result.DoubleValue = UomValueInput.fromJson(content['doubleValue'])

        return result

    def toDictionary(self) -> dict[str, Any]:
        result = super().toDictionary()

        if self.DoubleValue is not None:
            result['doubleValue'] = self.DoubleValue.toDictionary()

        return result
