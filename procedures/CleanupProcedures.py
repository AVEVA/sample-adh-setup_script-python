import time

from contextlib import suppress

from adh_sample_library_preview import (
    ADHClient,
    AssetType,
    DataViewShape,
    EventType,
    ReferenceDataType,
    SdsError,
    SdsSummaryType,
)
from adh_sample_library_preview.Assets import Asset
from omf_sample_library_preview.Client import OMFClient
from omf_sample_library_preview.Services import ContainerService, TypeService

from readers.event_readers import EventReader
from readers.reference_data_readers import ReferenceDataReader
from readers.stream_readers import StreamReader


def deleteCommunity(adh_client: ADHClient, community_name: str):
    community = next(
        iter(
            [
                community
                for community in adh_client.Communities.getCommunities(count=1000)
                if community.Name.casefold() == community_name.casefold()
            ]
        ),
        None,
    )
    if not community:
        return

    adh_client.Communities.deleteCommunity(community.Id)


def deleteRoles(adh_client: ADHClient, role_names: list[str]):
    roles = adh_client.Roles.getRoles(count=1000)
    for role_name in role_names:
        for role in roles:
            if role.Name == role_name:
                adh_client.Roles.deleteRole(role.Id)
                continue


def deleteClient(adh_client: ADHClient, client_name: str):
    client_credentials_path = f'{adh_client.baseClient.uri_API}/Tenants/{adh_client.baseClient.tenant}/ClientCredentialClients'
    response = adh_client.baseClient.request(
        'GET', client_credentials_path, params={'count': 1000}
    )
    adh_client.baseClient.checkResponse(response, f'Failed to get Clients.')

    client_id = next(
        iter(
            [
                client['Id']
                for client in response.json()
                if client['Name'].casefold() == client_name.casefold()
            ]
        ),
        None,
    )

    if not client_id:
        return

    response = adh_client.baseClient.request(
        'DELETE', f'{client_credentials_path}/{client_id}'
    )
    adh_client.baseClient.checkResponse(
        response, f'Failed to Delete Client {client_id}.'
    )


def deleteOMFConnection(
    adh_client: ADHClient, namespace_id: str, omf_connection_name: str
):
    omf_connections_path = f'{adh_client.baseClient.uri_API}/Tenants/{adh_client.baseClient.tenant}/Namespaces/{namespace_id}/OmfConnections'
    response = adh_client.baseClient.request('GET', omf_connections_path)
    adh_client.baseClient.checkResponse(response, f'Failed to get OMF Connections.')

    omf_connection_id = next(
        iter(
            [
                omf_connection['Id']
                for omf_connection in response.json()['Results']
                if omf_connection['Name'].casefold() == omf_connection_name.casefold()
            ]
        ),
        None,
    )

    if not omf_connection_id:
        return

    response = adh_client.baseClient.request(
        'DELETE', f'{omf_connections_path}/{omf_connection_id}'
    )
    adh_client.baseClient.checkResponse(
        response, f'Failed to Delete OMF Connection {omf_connection_id}.'
    )


def deleteTypes(adh_client: ADHClient, omf_client: OMFClient, stream_readers: list[StreamReader]):
    type_service = TypeService(omf_client)
    type_set = set()
    for stream_reader in stream_readers:
        type_set.add(stream_reader.get_type())
    type_service.deleteTypes(list(type_set))
    
    # Wait until all types are deleted by checking for the last in the list
    type_id = list(type_set)[-1].Id
    type = None
    try:
        type = adh_client.Types.getType(omf_client.NamespaceId, type_id)
    except SdsError:
        type = None
        pass
    while type:
        time.sleep(5)
        try:
            type = adh_client.Types.getType(omf_client.NamespaceId, type_id)
        except SdsError:
            type = None
            pass


def deleteStreams(omf_client: OMFClient, stream_readers: list[StreamReader]):
    container_service = ContainerService(omf_client)
    container_set = set()
    for stream_reader in stream_readers:
        container_set.add(stream_reader.get_stream())
    container_service.deleteContainers(list(container_set))


def deleteAssetTypes(
    adh_client: ADHClient, namespace_id: str, asset_types: list[AssetType]
):
    if asset_types:
        for asset_type in asset_types:
            with suppress(SdsError):
                adh_client.AssetTypes.deleteAssetType(namespace_id, asset_type.Id)


def deleteAssets(adh_client: ADHClient, namespace_id: str, assets: list[Asset]):
    with suppress(SdsError):
        for asset in assets:
            adh_client.Assets.deleteAsset(namespace_id, asset.Id)


def deleteAssetTypeDataViews(
    adh_client: ADHClient,
    namespace_id: str,
    asset_types: list[AssetType],
    summary_type: SdsSummaryType = None,
    shape: DataViewShape = DataViewShape.Standard,
):
    if asset_types:
        for asset_type in asset_types:
            data_view_id = f'{asset_type.Id} Asset Analysis'
            if summary_type:
                data_view_id = f'{data_view_id} - {summary_type.name}'
            if shape is DataViewShape.Narrow:
                data_view_id = f'{data_view_id} - Narrow'
            else:
                data_view_id = f'{data_view_id} - Standard'

            with suppress(SdsError):
                adh_client.DataViews.deleteDataView(namespace_id, data_view_id)


def deleteReferenceData(
    adh_client: ADHClient,
    namespace_id: str,
    reference_data_readers: list[ReferenceDataReader],
):
    type_set = set()
    for reference_data_reader in reference_data_readers:
        type_set.add(reference_data_reader.get_type())

    type: ReferenceDataType
    for type in type_set:
        reference_data = adh_client.ReferenceData.getReferenceData(
            namespace_id, type.Id, count=2000
        )
        while len(reference_data) > 0:
            for reference_datum in reference_data:
                adh_client.ReferenceData.deleteReferenceData(
                    namespace_id, type.Id, reference_datum['id']
                )

            reference_data = adh_client.ReferenceData.getReferenceData(
                namespace_id, type.Id, count=2000
            )


def deleteEvents(
    adh_client: ADHClient,
    namespace_id: str,
    event_readers: list[EventReader],
):
    type_set = set()
    for event_reader in event_readers:
        type_set.add(event_reader.get_type())

    type: EventType
    for type in type_set:
        events = adh_client.Events.getEvents(namespace_id, type.Id, count=2000)
        while len(events) > 0:
            for event in events:
                adh_client.Events.deleteEvent(namespace_id, type.Id, event['id'])

            events = adh_client.Events.getEvents(namespace_id, type.Id, count=2000)
