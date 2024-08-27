from abc import ABC, abstractmethod
from collections.abc import Iterator
from datetime import datetime

from adh_sample_library_preview import BaseReferenceData

from ..GraphData import GraphData
from .ReferenceDataReader import ReferenceDataReader


class BackfillableReferenceDataReader(ReferenceDataReader, ABC):
    @abstractmethod
    def read_backfill(
        self, start_time: datetime, end_time: datetime
    ) -> Iterator[GraphData[BaseReferenceData]]:
        pass
