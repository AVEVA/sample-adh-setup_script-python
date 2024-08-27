from datetime import datetime

from omf_sample_library_preview.Converters import omf_type, omf_type_property
from omf_sample_library_preview.Models import OMFFormatCode


@omf_type(Id='Diagnostics.Storage.Counts', Name='Diagnostics.Storage.Counts')
class Counts:
    def __init__(
        self,
        Timestamp: datetime,
        TypeCount: int,
        StreamCount: int,
        StreamViewCount: int,
    ):
        self.__timestamp = Timestamp
        self.__type_count = TypeCount
        self.__stream_count = StreamCount
        self.__stream_view_count = StreamViewCount

    @omf_type_property(IsIndex=True)
    def Timestamp(self) -> datetime:
        return self.__timestamp

    @Timestamp.setter
    def Timestamp(self, value: datetime):
        self.__timestamp = value

    @omf_type_property(Format=OMFFormatCode.Int32)
    def TypeCount(self) -> int:
        return self.__type_count

    @omf_type_property(Format=OMFFormatCode.Int32)
    def StreamCount(self) -> int:
        return self.__stream_count

    @omf_type_property(Format=OMFFormatCode.Int32)
    def StreamViewCount(self) -> int:
        return self.__stream_view_count
