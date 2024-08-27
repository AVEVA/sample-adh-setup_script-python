from enum import Enum


class DataType(Enum):
    Stream = "Stream"
    Event = "Event"
    ReferenceData = "ReferenceData"


preview_data_types = [
    DataType.Event,
    DataType.ReferenceData,
]

all_data_types = [
    DataType.Stream,
    DataType.Event,
    DataType.ReferenceData,
]
