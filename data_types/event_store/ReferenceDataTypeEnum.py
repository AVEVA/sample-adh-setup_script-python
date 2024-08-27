from enum import Enum

from .reference_data_types import DoubleReferenceData, double_reference_data_type


class ReferenceDataTypeEnum(Enum):
    DoubleReferenceData = (DoubleReferenceData, double_reference_data_type)
