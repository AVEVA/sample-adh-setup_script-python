import json
from dataclasses import dataclass
from typing import Any

from adh_sample_library_preview import AssetType

from readers import Reader
from readers.event_readers.EventReader import EventReader
from readers.reference_data_readers import ReferenceDataReader
from readers.stream_readers.StreamReader import StreamReader

from .HierarchyNode import HierarchyNode


@dataclass
class DataConfiguration:
    AssetTypes: list[AssetType] = None
    Hierarchy: HierarchyNode = None
    SoloStreamReaders: list[StreamReader] = None
    SoloEventReaders: list[EventReader] = None
    SoloReferenceDataReaders: list[ReferenceDataReader] = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'DataConfiguration':
        result = DataConfiguration()

        asset_types = content.get('AssetTypes', None)
        if asset_types:
            result.AssetTypes = [
                AssetType.fromJson(asset_type) for asset_type in asset_types
            ]

        hierarchy = content.get('Hierarchy', None)
        if hierarchy:
            result.Hierarchy = HierarchyNode.fromJson(hierarchy)

        solo_stream_readers = []
        if 'SoloStreamReaders' in content:
            for stream_reader in content['SoloStreamReaders']:
                reader_type = Reader[stream_reader['Reader']]
                solo_stream_readers.append(reader_type.value.fromJson(stream_reader))
        result.SoloStreamReaders = solo_stream_readers

        solo_event_readers = []
        if 'SoloEventReaders' in content:
            for event_reader in content['SoloEventReaders']:
                reader_type = Reader[event_reader['Reader']]
                solo_event_readers.append(reader_type.value.fromJson(event_reader))
        result.SoloEventReaders = solo_event_readers

        solo_reference_data_readers = []
        if 'SoloReferenceDataReaders' in content:
            for event_reader in content['SoloReferenceDataReaders']:
                reader_type = Reader[event_reader['Reader']]
                solo_reference_data_readers.append(
                    reader_type.value.fromJson(event_reader)
                )
        result.SoloReferenceDataReaders = solo_reference_data_readers

        return result

    def toJson(self):
        return json.dumps(self.toDictionary(), indent=2)

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.AssetTypes is not None:
            result['AssetTypes'] = [
                asset_type.toDictionary() for asset_type in self.AssetTypes
            ]

        if self.Hierarchy is not None:
            result['Hierarchy'] = self.Hierarchy.toDictionary()

        if self.SoloStreamReaders is not None:
            result['SoloStreamReaders'] = [
                stream_reader.toDictionary() for stream_reader in self.SoloStreamReaders
            ]

        if self.SoloEventReaders is not None:
            result['SoloEventReaders'] = [
                event_reader.toDictionary() for event_reader in self.SoloEventReaders
            ]

        if self.SoloReferenceDataReaders is not None:
            result['SoloReferenceDataReaders'] = [
                reference_data_reader.toDictionary()
                for reference_data_reader in self.SoloReferenceDataReaders
            ]

        return result
