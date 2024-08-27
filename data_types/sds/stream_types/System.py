from datetime import datetime

from omf_sample_library_preview.Converters import omf_type, omf_type_property
from omf_sample_library_preview.Models import OMFFormatCode


@omf_type(Id='Diagnostics.System', Name='Diagnostics.System')
class System:
    def __init__(
        self,
        Timestamp: datetime,
        ProcessIdentifier: int,
        StartTime: datetime,
        WorkingSet: float,
        TotalProcessorTime: float,
        TotalUserProcessorTime: float,
        TotalPrivilegedProcessorTime: float,
        ThreadCount: int,
        HandleCount: int,
        ManagedMemorySize: float,
        PrivateMemorySize: float,
        PeakPagedMemorySize: float,
        StorageTotalSize: float,
        StorageFreeSpace: float,
    ):
        self.__timestamp = Timestamp
        self.__process_identifier = ProcessIdentifier
        self.__start_time = StartTime
        self.__working_set = WorkingSet
        self.__total_processor_time = TotalProcessorTime
        self.__total_user_processor_time = TotalUserProcessorTime
        self.__total_privileged_processor_time = TotalPrivilegedProcessorTime
        self.__thread_count = ThreadCount
        self.__handle_count = HandleCount
        self.__managed_memory_size = ManagedMemorySize
        self.__private_memory_size = PrivateMemorySize
        self.__peak_paged_memory_size = PeakPagedMemorySize
        self.__storage_total_size = StorageTotalSize
        self.__storage_free_space = StorageFreeSpace

    @omf_type_property(IsIndex=True)
    def Timestamp(self) -> datetime:
        return self.__timestamp

    @Timestamp.setter
    def Timestamp(self, value: datetime):
        self.__timestamp = value

    @omf_type_property(Format=OMFFormatCode.Int32)
    def ProcessIdentifier(self) -> int:
        return self.__process_identifier

    @omf_type_property()
    def StartTime(self) -> datetime:
        return self.__start_time

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='MB')
    def WorkingSet(self) -> float:
        return self.__working_set

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='s')
    def TotalProcessorTime(self) -> float:
        return self.__total_processor_time

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='s')
    def TotalUserProcessorTime(self) -> float:
        return self.__total_user_processor_time

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='s')
    def TotalPrivilegedProcessorTime(self) -> float:
        return self.__total_privileged_processor_time

    @omf_type_property(Format=OMFFormatCode.Int32)
    def ThreadCount(self) -> int:
        return self.__thread_count

    @omf_type_property(Format=OMFFormatCode.Int32)
    def HandleCount(self) -> int:
        return self.__handle_count

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='MB')
    def ManagedMemorySize(self) -> float:
        return self.__managed_memory_size

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='MB')
    def PrivateMemorySize(self) -> float:
        return self.__private_memory_size

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='MB')
    def PeakPagedMemorySize(self) -> float:
        return self.__peak_paged_memory_size

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='MB')
    def StorageTotalSize(self) -> float:
        return self.__storage_total_size

    @omf_type_property(Format=OMFFormatCode.Float64, Uom='MB')
    def StorageFreeSpace(self) -> float:
        return self.__storage_free_space
