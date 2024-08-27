import json
from dataclasses import dataclass, fields
from typing import Any


@dataclass
class Labels:
    CommunityName: str = 'Setup Script Community'
    CommunityDescription: str = 'Setup Script Community'
    CommunityContactEmail: str = None
    CustomAdministratorRoleName: str = 'Setup Administrator'
    CustomAdministratorRoleDescription: str = 'Setup Administrator Role'
    CustomContributorRoleName: str = 'Setup Contributor'
    CustomContributorRoleDescription: str = 'Setup Contributor Role'
    CustomViewerRoleName: str = 'Setup Viewer'
    CustomViewerRoleDescription: str = 'Setup Viewer Role'
    RoleDescription: str = 'Setup Script Role'
    ClientName: str = 'Setup Script Client'
    ClientSecretDescription: str = 'Client Secret for Setup Script'
    OMFConnectionName: str = 'Setup Script OMF Client'
    OMFConnectionDescription: str = 'OMF Connection for Setup Script'

    @staticmethod
    def fromJson(content: dict[str, Any]):
        result = Labels()

        for field in fields(Labels):
            if field.name in content:
                setattr(result, field.name, content.get(field.name))

        return result

    def toJson(self):
        return json.dumps(self.toDictionary(), indent=2)

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        for field in fields(Labels):
            if getattr(self, field.name) != field.default:
                result[field.name] = getattr(self, field.name)

        return result
