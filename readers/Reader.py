from enum import Enum

from .event_readers import BackfillableEventReader, CSVEventReader
from .reference_data_readers import (
    BackfillableReferenceDataReader,
    CSVReferenceDataReader,
)
from .stream_readers import (
    BackfillableStreamReader,
    CSVStreamReader,
    RandomStreamReader,
)


class Reader(Enum):
    CSVStreamReader = CSVStreamReader
    RandomStreamReader = RandomStreamReader
    BackfillableStreamReader = BackfillableStreamReader
    CSVReferenceDataReader = CSVReferenceDataReader
    BackfillableReferenceDataReader = BackfillableReferenceDataReader
    CSVEventReader = CSVEventReader
    BackillableEventReader = BackfillableEventReader
