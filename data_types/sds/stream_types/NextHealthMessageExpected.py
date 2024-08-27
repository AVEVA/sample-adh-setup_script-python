from datetime import datetime

from omf_sample_library_preview.Converters import omf_type, omf_type_property


@omf_type()
class NextHealthMessageExpected:
    def __init__(self, Timestamp: datetime, NextHealthMessageExpected: datetime):
        self.__timestamp = Timestamp
        self.__next_health_message_expected = NextHealthMessageExpected

    @omf_type_property(IsIndex=True)
    def Timestamp(self) -> datetime:
        return self.__timestamp

    @Timestamp.setter
    def Timestamp(self, value: datetime):
        self.__timestamp = value

    @omf_type_property()
    def NextHealthMessageExpected(self) -> datetime:
        return self.__next_health_message_expected
