from enum import Enum

from .stream_types import (
    Counts,
    DeviceStatus,
    IngressRate,
    NextHealthMessageExpected,
    PIDigital,
    PIFloat32,
    PIFloat64,
    PIInt16,
    PIInt32,
    Running,
    System,
    TimeIndexedDouble,
    TimeIndexedInt64,
    TimeIndexedString,
)


class StreamTypeEnum(Enum):
    StreamTypeCounts = Counts
    StreamTypeDeviceStatus = DeviceStatus
    StreamTypeIngressRate = IngressRate
    StreamTypeNextHealthMessageExpected = NextHealthMessageExpected
    StreamTypePIDigital = PIDigital
    StreamTypePIFloat32 = PIFloat32
    StreamTypePIFloat64 = PIFloat64
    StreamTypePIInt16 = PIInt16
    StreamTypePIInt32 = PIInt32
    StreamTypeRunning = Running
    StreamTypeSystem = System
    StreamTypeTimeIndexedDouble = TimeIndexedDouble
    StreamTypeTimeIndexedInt64 = TimeIndexedInt64
    StreamTypeTimeIndexedString = TimeIndexedString
