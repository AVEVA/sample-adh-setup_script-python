from .Credentials import Credentials
import json
from dataclasses import dataclass, fields
from typing import Any

class Tenant:
    AuthenticationResource: str = "https://uswe.datahub.connect.aveva.com"
    NamespaceResource: str = None
    ApiVersion: str = "v1"
    TenantId: str = None
    NamespaceId: str = None
    SetupCredentials: Credentials = None
    RunCredentials: Credentials = None
    

    @staticmethod
    def fromJson(content: dict[str, Any]):
        result = Tenant()

        for field in fields(Tenant):
            if field.name in content:
                setattr(result, field.name, content.get(field.name))

        return result

    def toJson(self):
        return json.dumps(self.toDictionary(), indent=2)

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        for field in fields(Tenant):
            if getattr(self, field.name) != field.default:
                result[field.name] = getattr(self, field.name)

        return result