from dataclasses import dataclass
from typing import Any

from adh_sample_library_preview import (
    BaseEvent,
    EventType,
    PropertyTypeCode,
    PropertyTypeFlags,
    TypeProperty,
)

from ..AuthorizationTags import setup_authorization_tag

_event_properties = [
    TypeProperty(
        PropertyTypeCode.String, 'AcknowledgedBy', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.String, 'AcknowledgedDate', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.String, 'AreValuesCaptured', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'BearingATemperature', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'BearingBTemperature', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.String, 'CanBeAcknowledged', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'GearboxTemperature', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'Generator1Temperature', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'Generator2Temperature', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'HasChildren', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.String, 'InProblem', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.String, 'IsAcknowledged', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'IsLocked', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.String, 'IsAnnotated', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.Double, 'NacelleTemperature', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.String, 'OverheatedTemperatures', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'Path', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.String, 'Reason', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.String, 'Severity', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.String, 'TemplateName', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'TowerBase1Temperature', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'TurbineName', flags=PropertyTypeFlags.NoUom),
]

windtopia_high_turbine_temperature = EventType(
    _event_properties,
    setup_authorization_tag.Id,
    'Windtopia High Turbine Temperature',
    id='windtopiaHighTurbineTemperature',
    version=1,
)


@dataclass
class WindtopiaHighTurbineTemperature(BaseEvent):
    AcknowledgedBy: str = None
    AcknowledgedDate: str = None
    AreValuesCaptured: str = None
    BearingATemperature: float = None
    BearingBTemperature: float = None
    CanBeAcknowledged: str = None
    GearboxTemperature: float = None
    Generator1Temperature: float = None
    Generator2Temperature: float = None
    HasChildren: str = None
    InProblem: str = None
    IsAcknowledged: str = None
    IsLocked: str = None
    IsAnnotated: str = None
    NacelleTemperature: float = None
    OverheatedTemperatures: str = None
    Path: str = None
    Reason: str = None
    Severity: str = None
    TemplateName: str = None
    TowerBase1Temperature: float = None
    TurbineName: str = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'WindtopiaHighTurbineTemperature':
        base = BaseEvent.fromJson(content)
        result = WindtopiaHighTurbineTemperature()
        result.__dict__.update(base.__dict__)

        if 'acknowledgedBy' in content:
            result.AcknowledgedBy = content['acknowledgedBy']
        if 'acknowledgedDate' in content:
            result.AcknowledgedDate = content['acknowledgedDate']
        if 'areValuesCaptured' in content:
            result.AreValuesCaptured = content['areValuesCaptured']
        if 'bearingATemperature' in content:
            result.BearingATemperature = content['bearingATemperature']
        if 'bearingBTemperature' in content:
            result.BearingBTemperature = content['bearingBTemperature']
        if 'canBeAcknowledged' in content:
            result.CanBeAcknowledged = content['canBeAcknowledged']
        if 'gearboxTemperature' in content:
            result.GearboxTemperature = content['gearboxTemperature']
        if 'generator1Temperature' in content:
            result.Generator1Temperature = content['generator1Temperature']
        if 'generator2Temperature' in content:
            result.Generator2Temperature = content['generator2Temperature']
        if 'hasChildren' in content:
            result.HasChildren = content['hasChildren']
        if 'inProblem' in content:
            result.InProblem = content['inProblem']
        if 'isAcknowledged' in content:
            result.IsAcknowledged = content['isAcknowledged']
        if 'isLocked' in content:
            result.IsLocked = content['isLocked']
        if 'isAnnotated' in content:
            result.IsAnnotated = content['isAnnotated']
        if 'nacelleTemperature' in content:
            result.NacelleTemperature = content['nacelleTemperature']
        if 'overheatedTemperatures' in content:
            result.OverheatedTemperatures = content['overheatedTemperatures']
        if 'path' in content:
            result.Path = content['path']
        if 'reason' in content:
            result.Reason = content['reason']
        if 'severity' in content:
            result.Severity = content['severity']
        if 'templateName' in content:
            result.TemplateName = content['templateName']
        if 'towerBase1Temperature' in content:
            result.TowerBase1Temperature = content['towerBase1Temperature']
        if 'turbineName' in content:
            result.TurbineName = content['turbineName']

        return result

    def toDictionary(self) -> dict[str, Any]:
        result = super().toDictionary()

        if self.AcknowledgedBy is not None:
            result['acknowledgedBy'] = self.AcknowledgedBy
        if self.AcknowledgedDate is not None:
            result['acknowledgedDate'] = self.AcknowledgedDate
        if self.AreValuesCaptured is not None:
            result['areValuesCaptured'] = self.AreValuesCaptured
        if self.BearingATemperature is not None:
            result['bearingATemperature'] = self.BearingATemperature
        if self.BearingBTemperature is not None:
            result['bearingBTemperature'] = self.BearingBTemperature
        if self.CanBeAcknowledged is not None:
            result['canBeAcknowledged'] = self.CanBeAcknowledged
        if self.GearboxTemperature is not None:
            result['gearboxTemperature'] = self.GearboxTemperature
        if self.Generator1Temperature is not None:
            result['generator1Temperature'] = self.Generator1Temperature
        if self.Generator2Temperature is not None:
            result['generator2Temperature'] = self.Generator2Temperature
        if self.HasChildren is not None:
            result['hasChildren'] = self.HasChildren
        if self.InProblem is not None:
            result['inProblem'] = self.InProblem
        if self.IsAcknowledged is not None:
            result['isAcknowledged'] = self.IsAcknowledged
        if self.IsLocked is not None:
            result['isLocked'] = self.IsLocked
        if self.IsAnnotated is not None:
            result['isAnnotated'] = self.IsAnnotated
        if self.NacelleTemperature is not None:
            result['nacelleTemperature'] = self.NacelleTemperature
        if self.OverheatedTemperatures is not None:
            result['overheatedTemperatures'] = self.OverheatedTemperatures
        if self.Path is not None:
            result['path'] = self.Path
        if self.Reason is not None:
            result['reason'] = self.Reason
        if self.Severity is not None:
            result['severity'] = self.Severity
        if self.TemplateName is not None:
            result['templateName'] = self.TemplateName
        if self.TowerBase1Temperature is not None:
            result['towerBase1Temperature'] = self.TowerBase1Temperature
        if self.TurbineName is not None:
            result['turbineName'] = self.TurbineName

        return result
