from dataclasses import dataclass
from typing import Any

from adh_sample_library_preview import (
    BaseEvent,
    BaseReferenceData,
    PropertyTypeCode,
    ReferenceDataCategory,
    ReferenceDataType,
    TypeProperty,
    UomValueInput,
)

from ..AuthorizationTags import setup_authorization_tag

_reference_data_properties = [
    TypeProperty(PropertyTypeCode.Double, 'DoubleValue', uom='NONE'),
]

double_reference_data_type = ReferenceDataType(
    ReferenceDataCategory.ReferenceData,
    _reference_data_properties,
    setup_authorization_tag.Id,
    'myDoubleReferenceData',
    id='myDoubleReferenceData',
    version=1,
)


@dataclass
class DoubleReferenceData(BaseReferenceData):
    DoubleValue: UomValueInput[float] = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'DoubleReferenceData':
        base = BaseEvent.fromJson(content)
        result = DoubleReferenceData()
        result.__dict__.update(base.__dict__)

        if 'doubleValue' in content:
            result.DoubleValue = UomValueInput.fromJson(content['doubleValue'])

        return result

    def toDictionary(self) -> dict[str, Any]:
        result = super().toDictionary()

        if self.DoubleValue is not None:
            result['doubleValue'] = self.DoubleValue.toDictionary()

        return result
