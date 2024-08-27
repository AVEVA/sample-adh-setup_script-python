import json
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from adh_sample_library_preview import AssetType

from readers.event_readers.EventReader import EventReader
from readers.reference_data_readers import ReferenceDataReader
from readers.stream_readers.StreamReader import StreamReader

from .Credentials import Credentials
from .DataConfigurationReader import readDataConfiguration
from .DataType import DataType
from .HierarchyNode import HierarchyNode
from .Labels import Labels
from .Parameters import _get_parameter
from .Resource import Resource
from .Tenant import Tenant

@dataclass
class AppSettings:
    Tenants: list[Tenant] = None
    DataConfigurationPath: str = None
    Preview: bool = False
    Labels: 'Labels' = None
    ExcludedSetupResources: list['Resource'] = None
    ExcludedCleanupResources: list['Resource'] = None
    ExcludedDataTypes: list[DataType] = None
    StreamBackfillStart: datetime = None
    EventBackfillStart: datetime = None
    ReferenceDataBackfillStart: datetime = None
    AssetTypes: list[AssetType] = None
    Hierarchy: HierarchyNode = None
    SoloStreamReaders: list[StreamReader] = None
    SoloEventReaders: list[EventReader] = None
    SoloReferenceDataReaders: list[ReferenceDataReader] = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'AppSettings':
        result = AppSettings()

        if _get_parameter(content, 'Tenants', True):
            result.Tenants = []
            tenants = _get_parameter(content, 'Tenants', True)
            
            for tenant in tenants:
                tempTenant = Tenant()
                tempTenant.ApiVersion =tenant['ApiVersion']
                tempTenant.AuthenticationResource =tenant['AuthenticationResource']
                tempTenant.NamespaceId =tenant['NamespaceId']
                tempTenant.NamespaceResource =tenant['NamespaceResource']
                
                if 'RunCredentials' in tenant:
                    tempTenant.RunCredentials =Credentials.fromJson(tenant['RunCredentials'])

                if 'SetupCredentials' in tenant:
                    tempTenant.SetupCredentials =Credentials.fromJson(tenant['SetupCredentials'])
                    
                tempTenant.TenantId =tenant['TenantId']

                result.Tenants.append(tempTenant)

            # result.Tenants = []
            # for tenant in tenants:
            #     tempTenant:Tenant = Tenant.fromJson(json.dumps(tenant))
            #     result.Tenants.append(tempTenant)
            '''
            if _get_parameter(tenant, 'AuthenticationResource', False):
                result.AuthenticationResource = _get_parameter(tenant, 'AuthenticationResource', False)
            if _get_parameter(content, 'NamespaceResource', False):
                result.NamespaceResource = _get_parameter(content, 'NamespaceResource', False)
            if _get_parameter(content, 'ApiVersion', False):
                result.ApiVersion
            result.TenantId = _get_parameter(content, 'TenantId', True)
            result.NamespaceId = _get_parameter(content, 'NamespaceId', True)

            if _get_parameter(content, 'SetupCredentials', True):
                result.SetupCredentials = Credentials.fromJson(
                    _get_parameter(content, 'SetupCredentials', True)
                )

            if _get_parameter(content, 'RunCredentials', False):
                result.RunCredentials = Credentials.fromJson(
                    _get_parameter(content, 'RunCredentials', False)
                )'''

        if _get_parameter(content, 'DataConfigurationPath', True):
            result.DataConfigurationPath = _get_parameter(
                content, 'DataConfigurationPath', True
            )

            data_configuration = readDataConfiguration(result.DataConfigurationPath)
            result.AssetTypes = data_configuration.AssetTypes
            result.Hierarchy = data_configuration.Hierarchy
            data_configuration.Hierarchy.resolve_paths()
            result.SoloStreamReaders = data_configuration.SoloStreamReaders
            result.SoloEventReaders = data_configuration.SoloEventReaders
            result.SoloReferenceDataReaders = (
                data_configuration.SoloReferenceDataReaders
            )

        if _get_parameter(content, 'Preview', False):
            result.Preview = _get_parameter(content, 'Preview', False)

        if _get_parameter(content, 'Labels', False):
            result.Labels = Labels.fromJson(_get_parameter(content, 'Labels', False))
        else:
            result.Labels = Labels()

        if _get_parameter(content, 'ExcludedSetupResources', False):
            result.ExcludedSetupResources = []
            for resource in _get_parameter(content, 'ExcludedSetupResources', False):
                result.ExcludedSetupResources.append(Resource(resource))

        if _get_parameter(content, 'ExcludedCleanupResources', False):
            result.ExcludedCleanupResources = []
            for resource in _get_parameter(content, 'ExcludedCleanupResources', False):
                result.ExcludedCleanupResources.append(Resource(resource))

        if _get_parameter(content, 'ExcludedDataTypes', False):
            result.ExcludedDataTypes = []
            for resource in _get_parameter(content, 'ExcludedDataTypes', False):
                result.ExcludedDataTypes.append(DataType(resource))

        if _get_parameter(content, 'StreamBackfillStart', False):
            result.StreamBackfillStart = datetime.fromisoformat(
                _get_parameter(content, 'StreamBackfillStart', False)
            ).replace(
                tzinfo=timezone.utc
            )

        if _get_parameter(content, 'EventBackfillStart', False):
            result.EventBackfillStart = datetime.fromisoformat(
                _get_parameter(content, 'EventBackfillStart', False)
            ).replace(
                tzinfo=timezone.utc
            )

        if _get_parameter(content, 'ReferenceDataBackfillStart', False):
            result.ReferenceDataBackfillStart = datetime.fromisoformat(
                _get_parameter(content, 'ReferenceDataBackfillStart', False)
            ).replace(
                tzinfo=timezone.utc
            )

        return result

    def toJson(self):
        return json.dumps(self.toDictionary(), indent=2)

    def toDictionary(self) -> dict[str, Any]:
        result = {}
        
        if self.Tenants is not None:
            result['Tenants'] = []
            for tenant in self.Tenants:     
                #result['Tenants'].append(tenant.toDictionary())                    
                insideResult = {}
                if tenant.AuthenticationResource is not None:
                    insideResult['AuthenticationResource'] = tenant.AuthenticationResource

                if tenant.NamespaceResource is not None:
                    insideResult['NamespaceResource'] = tenant.NamespaceResource

                if tenant.ApiVersion is not None:
                    insideResult['ApiVersion'] = tenant.ApiVersion

                if tenant.TenantId is not None:
                    insideResult['TenantId'] = tenant.TenantId

                if tenant.NamespaceId is not None:
                    insideResult['NamespaceId'] = tenant.NamespaceId

                if tenant.SetupCredentials is not None:
                    insideResult['SetupCredentials'] = tenant.SetupCredentials.toDictionary()

                if tenant.RunCredentials is not None:
                    insideResult['RunCredentials'] = tenant.RunCredentials.toDictionary() 
                result['Tenants'].append(insideResult)      

        if self.DataConfigurationPath is not None:
            result['DataConfigurationPath'] = self.DataConfigurationPath

        if self.Preview is not None:
            result['Preview'] = self.Preview

        if self.Labels is not None:
            labels = self.Labels.toDictionary()
            if labels is not {}:
                result['Labels'] = labels

        if self.ExcludedSetupResources is not None:
            result['ExcludedSetupResources'] = [
                resource.value for resource in self.ExcludedSetupResources
            ]

        if self.ExcludedCleanupResources is not None:
            result['ExcludedCleanupResources'] = [
                resource.value for resource in self.ExcludedCleanupResources
            ]

        if self.ExcludedDataTypes is not None:
            result['ExcludedDataTypes'] = [
                data_type.value for data_type in self.ExcludedDataTypes
            ]

        if self.StreamBackfillStart is not None:
            result[
                'StreamBackfillStart'
            ] = self.StreamBackfillStart.isoformat()

        if self.EventBackfillStart is not None:
            result['EventBackfillStart'] = self.EventBackfillStart.isoformat()

        if self.ReferenceDataBackfillStart is not None:
            result[
                'ReferenceDataBackfillStart'
            ] = self.ReferenceDataBackfillStart.isoformat()

        return result
