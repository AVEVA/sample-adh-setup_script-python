from enum import Enum


class Resource(Enum):
    Community = 'Community'
    Roles = 'Roles'
    Streams = 'Streams'
    Assets = 'Assets'
    DataViews = 'DataViews'
    Enumerations = 'Enumerations'
    ReferenceDataTypes = 'ReferenceDataTypes'
    EventTypes = 'EventTypes'
    OMFConnection = 'OMFConnection'
    Client = 'Client'


preview_resources = [
    Resource.Enumerations,
    Resource.ReferenceDataTypes,
    Resource.EventTypes,
]

all_resources = [
    Resource.Community,
    Resource.Roles,
    Resource.Streams,
    Resource.Assets,
    Resource.DataViews,
    Resource.Enumerations,
    Resource.ReferenceDataTypes,
    Resource.EventTypes,
    Resource.OMFConnection,
    Resource.Client,
]
