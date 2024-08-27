import json
from dataclasses import dataclass
from typing import Any

from .Parameters import _get_parameter


@dataclass
class Credentials:
    ClientId: str = None
    ClientSecret: str = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'Credentials':
        result = Credentials()

        result.ClientId = _get_parameter(content, 'ClientId', True)
        if _get_parameter(content, 'ClientSecret', False):
            result.ClientSecret = _get_parameter(content, 'ClientSecret', False)

        return result

    def toJson(self):
        return json.dumps(self.toDictionary(), indent=2)

    def toDictionary(self) -> dict[str, Any]:
        result = {}

        if self.ClientId is not None:
            result['ClientId'] = self.ClientId

        if self.ClientSecret is not None:
            result['ClientSecret'] = self.ClientSecret

        return result
