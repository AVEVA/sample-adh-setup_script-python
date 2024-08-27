from datetime import datetime

from omf_sample_library_preview.Converters import omf_type, omf_type_property


@omf_type()
class DeviceStatus:
    def __init__(self, Time: datetime, DeviceStatus: str):
        self.__time = Time
        self.__device_status = DeviceStatus

    @omf_type_property(IsIndex=True)
    def Time(self) -> datetime:
        return self.__time

    @Time.setter
    def Time(self, value: datetime):
        self.__time = value

    @omf_type_property()
    def EventRate(self) -> str:
        return self.__device_status
