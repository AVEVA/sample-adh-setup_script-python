import json
import time
from datetime import datetime, timedelta, timezone

from adh_sample_library_preview import (
    AccessControlList,
    ADHClient,
    AssetType,
    Community,
    CommunityInput,
    DataItemResourceType,
    DataView,
    DataViewShape,
    EventType,
    Field,
    FieldSet,
    FieldSource,
    Query,
    ReferenceDataType,
    Role,
    RoleScope,
    SdsError,
    SdsSummaryType,
    SdsTypeCode,
    SummaryDirection,
)
from adh_sample_library_preview.Asset import Asset
from omf_sample_library_preview.Client import OMFClient
from omf_sample_library_preview.Services import ContainerService, TypeService

from appsettings import HierarchyNode
from readers.event_readers import EventReader
from readers.reference_data_readers import ReferenceDataReader
from readers.stream_readers import StreamReader


def createCommunity(
    adh_client: ADHClient,
    community_name: str,
    community_description: str,
    community_contact_email: str,
) -> Community:
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
        community_input = CommunityInput(
            community_name, community_description, contact_email=community_contact_email
        )
        community = adh_client.Communities.createCommunity(community_input)

    return community


def createRoles(
    adh_client: ADHClient,
    role_names: tuple[str, str, str],
    role_descriptions: tuple[str, str, str],
) -> tuple[Role, Role, Role]:
    roles = []
    for i in range(len(role_names)):
        roles.append(
            adh_client.Roles.createRole(
                Role(
                    name=role_names[i],
                    description=role_descriptions[i],
                    role_scope=RoleScope.Tenant,
                )
            )
        )
    return tuple(roles)


def createClient(
    adh_client: ADHClient,
    role_ids: list[str],
    client_name: str,
    client_secret_description: str,
) -> dict[str, str]:
    client_credentials_path = f'{adh_client.baseClient.uri_API}/Tenants/{adh_client.baseClient.tenant}/ClientCredentialClients'

    # Check for existing client
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

    if client_id:
        return {'Id': client_id}

    body = {
        'AccessTokenLifetime': 3600,
        'Id': None,
        'Name': client_name,
        'RoleIds': role_ids,
        'SecretDescription': client_secret_description,
        'SecretExpirationDate': (
            datetime.now(timezone.utc) + timedelta(days=365)
        ).isoformat(),
    }
    response = adh_client.baseClient.request(
        'POST', client_credentials_path, data=json.dumps(body)
    )
    adh_client.baseClient.checkResponse(response, f'Failed to create Client.')
    client = response.json()
    return {
        'Id': client['Client']['Id'],
        'Secret': client['Secret'],
    }


def createSecret(
    adh_client: ADHClient, client_id: str, client_secret_description: str
) -> str:
    client_credentials_secret_path = f'{adh_client.baseClient.uri_API}/Tenants/{adh_client.baseClient.tenant}/ClientCredentialClients/{client_id}/Secrets'
    body = {
        'Description': client_secret_description,
        'Expiration': (datetime.now(timezone.utc) + timedelta(days=365)).isoformat(),
        'Expires': True,
    }
    response = adh_client.baseClient.request(
        'POST', client_credentials_secret_path, data=json.dumps(body)
    )
    adh_client.baseClient.checkResponse(response, f'Failed to create Client.')
    secret = response.json()['Secret']
    return secret


def _getOMFConnectionState(
    adh_client: ADHClient, namespace_id: str, omf_connection_id: str
):
    omf_connection_path = f'{adh_client.baseClient.uri_API}/Tenants/{adh_client.baseClient.tenant}/Namespaces/{namespace_id}/OmfConnections/{omf_connection_id}'
    response = adh_client.baseClient.request('GET', omf_connection_path)
    adh_client.baseClient.checkResponse(response, f'Failed to get OMF Connection.')

    return response.json()['State']


def createOmfConnection(
    adh_client: ADHClient,
    namespace_id: str,
    client_id: str,
    omf_connection_name: str,
    omf_connection_description: str,
):
    omf_connections_path = f'{adh_client.baseClient.uri_API}/Tenants/{adh_client.baseClient.tenant}/Namespaces/{namespace_id}/OmfConnections'

    # Check if OMF Connection already exists
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

    if omf_connection_id:
        return

    body = {
        'Name': omf_connection_name,
        'Description': omf_connection_description,
        'ClientIds': [client_id],
    }
    response = adh_client.baseClient.request(
        'POST', omf_connections_path, data=json.dumps(body)
    )
    adh_client.baseClient.checkResponse(response, f'Failed to create OMF Connection.')

    omf_connection_id = response.json()['Id']

    # Wait until OMF Connection is active
    while (
        _getOMFConnectionState(adh_client, namespace_id, omf_connection_id) != 'Active'
    ):
        time.sleep(5)


def createTypes(
    adh_client: ADHClient,
    omf_client: OMFClient,
    stream_readers: list[StreamReader],
):
    type_service = TypeService(omf_client)
    type_set = set()
    for stream_reader in stream_readers:
        type_set.add(stream_reader.get_type())
    type_service.createTypes(list(type_set))

    # Wait until all types are created by checking for the last in the list
    type_id = list(type_set)[-1].Id
    type = None
    try:
        type = adh_client.Types.getType(omf_client.NamespaceId, type_id)
    except SdsError:
        pass
    while not type:
        time.sleep(5)
        try:
            type = adh_client.Types.getType(omf_client.NamespaceId, type_id)
        except SdsError:
            pass


def setTypeACLs(
    adh_client: ADHClient,
    namespace_id: str,
    stream_readers: list[StreamReader],
    acl: AccessControlList,
):
    type_set = set()
    for stream_reader in stream_readers:
        type_set.add(stream_reader.get_type())

    for type in type_set:
        try: 
            adh_client.Types.updateAccessControl(namespace_id, type.Id, acl)
        except:
            print(f"Error setting ACLs on {type.Id}.  Retrying."  )
            time.sleep(5)            
            try: 
                adh_client.Types.updateAccessControl(namespace_id, type.Id, acl)
            except:
                print(f"Failure setting ACLs on {type.Id}."  )
                pass


def createStreams(
    adh_client: ADHClient, omf_client: OMFClient, stream_readers: list[StreamReader]
):
    container_service = ContainerService(omf_client)
    container_set = set()
    for stream_reader in stream_readers:
        container_set.add(stream_reader.get_stream())
    container_set = list(container_set)
    for i in range(0, len(container_set), 1000):
        container_service.createContainers(container_set[i : i + 1000])

    # Wait until all streams are created by checking for the last in the list
    stream_id = list(container_set)[-1].Id
    stream = None
    try:
        stream = adh_client.Streams.getStream(omf_client.NamespaceId, stream_id)
    except SdsError:
        pass
    while not stream:
        time.sleep(5)
        try:
            stream = adh_client.Streams.getStream(omf_client.NamespaceId, stream_id)
        except SdsError:
            pass


def setStreamACLs(
    adh_client: ADHClient,
    namespace_id: str,
    stream_readers: list[StreamReader],
    acl: AccessControlList,
):
    container_set = set()
    for stream_reader in stream_readers:
        container_set.add(stream_reader.get_stream())

    for container in container_set:
        adh_client.Streams.updateAccessControl(namespace_id, container.Id, acl)


def createAssetTypes(
    adh_client: ADHClient,
    namespace_id: str,
    acl: AccessControlList,
    asset_types: list[AssetType],
) -> list[AssetType]:
    created_asset_types = []
    if asset_types and asset_types != []:
        for asset_type in asset_types:
            created_asset_types.append(
                adh_client.AssetTypes.createOrUpdateAssetType(namespace_id, asset_type)
            )
            adh_client.AssetTypes.updateAccessControl(namespace_id, asset_type.Id, acl)

    return created_asset_types


def createAssets(
    adh_client: ADHClient,
    namespace_id: str,
    acl: AccessControlList,
    assets: list[Asset],
) -> list[Asset]:
    assets = [
        adh_client.Assets.createOrUpdateAsset(
            namespace_id,
            asset,
        )
        for asset in assets
    ]
    for asset in assets:
        adh_client.Assets.updateAccessControl(namespace_id, asset.Id, acl)

    return assets


def createAssetRule(
    adh_client: ADHClient,
    namespace_id: str,
    acl: AccessControlList,
    hierarchy: HierarchyNode,
):
    pass


def createAssetTypeDataViews(
    adh_client: ADHClient,
    namespace_id: str,
    acl: AccessControlList,
    asset_types: list[AssetType],
    summary_type: SdsSummaryType = None,
    shape: DataViewShape = DataViewShape.Standard,
):
    if not asset_types:
        return

    for asset_type in asset_types:
        query_id = 'AssetTypeQuery'
        query = Query(
            query_id, DataItemResourceType.Asset, f'assetTypeId:{asset_type.Id}'
        )

        index_field = Field(FieldSource.NotApplicable, label='Timestamp')

        summary_direction = SummaryDirection.Backward if summary_type else None

        property_data_fields = [
            Field(
                FieldSource.PropertyId,
                ['Value'],
                [type_reference.StreamReferenceName],
                '{IdentifyingValue} '
                + type_reference.StreamReferenceName
                + ' Value {SummaryType} {Uom}',
                summary_type=summary_type,
                summary_direction=summary_direction,
            )
            for type_reference in asset_type.TypeReferences
        ]
        metadata_data_fields = [
            Field(
                FieldSource.Metadata, ['site'], label='{IdentifyingValue} site {Uom}'
            ),
            Field(
                FieldSource.Metadata,
                ['__Path'],
                label='{IdentifyingValue} __Path {Uom}',
            ),
        ]
        name_data_fields = [Field(FieldSource.Name, label='{IdentifyingValue} Name')]
        data_field_set = [
            FieldSet(
                query_id, property_data_fields + metadata_data_fields + name_data_fields
            )
        ]

        grouping_fields = [Field(FieldSource.Id, label='{IdentifyingValue} Id')]

        data_view_id = f'{asset_type.Id} Asset Analysis'
        data_view_description = f'{asset_type.Name} Asset Data View'
        if summary_type:
            data_view_id = f'{data_view_id} - {summary_type.name}'
            data_view_description = f'{data_view_description} - {summary_type.name}'
        if shape is DataViewShape.Narrow:
            data_view_id = f'{data_view_id} - Narrow'
            data_view_description = f'{data_view_description} - Narrow'
        else:
            data_view_id = f'{data_view_id} - Standard'
            data_view_description = f'{data_view_description} - Standard'

        data_view = DataView(
            data_view_id,
            data_view_id,
            description=data_view_description,
            queries=[query],
            index_field=index_field,
            data_field_sets=data_field_set,
            grouping_fields=grouping_fields,
            index_type_code=SdsTypeCode.DateTime,
            shape=shape,
        )
        data_view = adh_client.DataViews.postDataView(namespace_id, data_view)
        adh_client.DataViews.updateAccessControl(namespace_id, data_view.Id, acl)


def createAuthorizationTags(
    adh_client: ADHClient,
    namespace_id: str,
    event_readers: list[EventReader],
    reference_data_readers: list[ReferenceDataReader],
):
    authorization_tag_set = set()
    for event_reader in event_readers:
        authorization_tags = event_reader.get_authorization_tags()
        for authorization_tag in authorization_tags:
            authorization_tag_set.add(authorization_tag)

    for reference_data_reader in reference_data_readers:
        authorization_tags = reference_data_reader.get_authorization_tags()
        for authorization_tag in authorization_tags:
            authorization_tag_set.add(authorization_tag)

    for authorization_tag in authorization_tag_set:
        adh_client.AuthorizationTags.getOrCreateAuthorizationTag(
            namespace_id, authorization_tag.Id, authorization_tag
        )

    adh_client.GraphQL.checkForSchemaChanges(namespace_id)


def createEnumerations(
    adh_client: ADHClient,
    namespace_id: str,
    event_readers: list[EventReader],
    reference_data_readers: list[ReferenceDataReader],
):
    enumeration_set = set()
    for event_reader in event_readers:
        enumerations = event_reader.get_enumerations()
        for enumeration in enumerations:
            enumeration_set.add(enumeration)

    for reference_data_reader in reference_data_readers:
        enumerations = reference_data_reader.get_enumerations()
        for enumeration in enumerations:
            enumeration_set.add(enumeration)

    for enumeration in enumeration_set:
        adh_client.Enumerations.getOrCreateEnumeration(
            namespace_id, enumeration.Id, enumeration
        )
    adh_client.GraphQL.checkForSchemaChanges(namespace_id)


def createReferenceDataTypes(
    adh_client: ADHClient,
    namespace_id: str,
    reference_data_readers: list[ReferenceDataReader],
):
    type_set = set()
    for reference_data_reader in reference_data_readers:
        type_set.add(reference_data_reader.get_type())

    type: ReferenceDataType
    for type in type_set:
        adh_client.ReferenceDataTypes.getOrCreateReferenceDataType(
            namespace_id, type.Id, type
        )

    adh_client.GraphQL.checkForSchemaChanges(namespace_id)


def createEventTypes(
    adh_client: ADHClient, namespace_id: str, event_readers: list[EventReader]
):
    type_set = set()
    for event_reader in event_readers:
        type_set.add(event_reader.get_type())

    type: EventType
    for type in type_set:
        adh_client.EventTypes.getOrCreateEventType(namespace_id, type.Id, type)

    adh_client.GraphQL.checkForSchemaChanges(namespace_id)
