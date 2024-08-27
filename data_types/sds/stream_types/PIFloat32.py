from datetime import datetime

from omf_sample_library_preview.Converters import omf_type, omf_type_property
from omf_sample_library_preview.Models import OMFFormatCode


@omf_type(
    Id='PIFloat32',
    Name='PI Float32',
    Description='Represents a PI Data Archive float32 point type.',
)
class PIFloat32:
    def __init__(
        self,
        Timestamp: datetime,
        Value: float,
        IsQuestionable: bool = False,
        IsSubstituted: bool = False,
        IsAnnotated: bool = False,
        SystemStateCode: float = None,
        DigitalStateName: str = None,
    ):
        self.__timestamp = Timestamp
        self.__value = Value
        self.__is_questionable = IsQuestionable
        self.__is_substituted = IsSubstituted
        self.__is_annotated = IsAnnotated
        self.__system_state_code = SystemStateCode
        self.__digital_state_name = DigitalStateName

    @omf_type_property(IsIndex=True)
    def Timestamp(self) -> datetime:
        return self.__timestamp

    @Timestamp.setter
    def Timestamp(self, value: datetime):
        self.__timestamp = value

    @omf_type_property(Format=OMFFormatCode.Float32)
    def Value(self) -> float | None:
        return self.__value

    @omf_type_property()
    def IsQuestionable(self) -> bool:
        return self.__is_questionable

    @omf_type_property()
    def IsSubstituted(self) -> bool:
        return self.__is_substituted

    @omf_type_property()
    def IsAnnotated(self) -> bool:
        return self.__is_annotated

    @omf_type_property(Format=OMFFormatCode.Float32)
    def SystemStateCode(self) -> float | None:
        return self.__system_state_code

    @omf_type_property()
    def DigitalStateName(self) -> str:
        return self.__digital_state_name
