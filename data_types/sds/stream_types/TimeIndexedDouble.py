from datetime import datetime

from omf_sample_library_preview.Converters import omf_type, omf_type_property
from omf_sample_library_preview.Models import OMFFormatCode


@omf_type()
class TimeIndexedDouble:
    def __init__(self, Timestamp: datetime, Value: float):
        self.__timestamp = Timestamp
        self.__value = Value

    @omf_type_property(IsIndex=True)
    def Timestamp(self) -> datetime:
        return self.__timestamp

    @Timestamp.setter
    def Timestamp(self, value: datetime):
        self.__timestamp = value

    @omf_type_property(Format=OMFFormatCode.Float64)
    def Value(self) -> float:
        return self.__value
