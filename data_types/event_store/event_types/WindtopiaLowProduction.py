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
    TypeProperty(PropertyTypeCode.Double, 'ActivePower', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.Double,
        'ActivePower10minrollingavg',
        flags=PropertyTypeFlags.NoUom,
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'AdjustedWindSpeed', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.String, 'AreValuesCaptured', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'AveragePrice', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'AverageWindSpeed', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.String, 'CanBeAcknowledged', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'ExpectedPower', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double,
        'ExpectedPower10minrollingavg',
        flags=PropertyTypeFlags.NoUom,
    ),
    TypeProperty(PropertyTypeCode.String, 'HasChildren', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.String, 'IsAcknowledged', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'IsAnnotated', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.String, 'IsLocked', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.String, 'Manufacturer', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.String, 'OperatingState', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'Path', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.String, 'PowerRated', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.Double, 'Price', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.Double, 'RevenueDelta', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'Severity', flags=PropertyTypeFlags.NoUom),
    TypeProperty(
        PropertyTypeCode.String, 'TemplateName', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(
        PropertyTypeCode.Double, 'TotalRevenueLoss', flags=PropertyTypeFlags.NoUom
    ),
    TypeProperty(PropertyTypeCode.String, 'Turbine', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.String, 'WindFarm', flags=PropertyTypeFlags.NoUom),
    TypeProperty(PropertyTypeCode.Double, 'WindSpeed', flags=PropertyTypeFlags.NoUom),
]

windtopia_low_production = EventType(
    _event_properties,
    setup_authorization_tag.Id,
    'Windtopia Low Production',
    id='windtopiaLowProduction',
    version=1,
)


@dataclass
class WindtopiaLowProduction(BaseEvent):
    AcknowledgedBy: str = None
    AcknowledgedDate: str = None
    ActivePower: float = None
    ActivePower10minrollingavg: float = None
    AdjustedWindSpeed: float = None
    AreValuesCaptured: str = None
    AveragePrice: float = None
    AverageWindSpeed: float = None
    CanBeAcknowledged: str = None
    ExpectedPower: float = None
    ExpectedPower10minrollingavg: float = None
    HasChildren: str = None
    IsAcknowledged: str = None
    IsAnnotated: str = None
    IsLocked: str = None
    Manufacturer: str = None
    OperatingState: str = None
    Path: str = None
    PowerRated: str = None
    Price: float = None
    RevenueDelta: float = None
    Severity: str = None
    TemplateName: str = None
    TotalRevenueLoss: float = None
    Turbine: str = None
    WindFarm: str = None
    WindSpeed: float = None

    @staticmethod
    def fromJson(content: dict[str, Any]) -> 'WindtopiaLowProduction':
        base = BaseEvent.fromJson(content)
        result = WindtopiaLowProduction()
        result.__dict__.update(base.__dict__)

        if 'acknowledgedBy' in content:
            result.AcknowledgedBy = content['acknowledgedBy']
        if 'acknowledgedDate' in content:
            result.AcknowledgedDate = content['acknowledgedDate']
        if 'activePower' in content:
            result.ActivePower = content['activePower']
        if 'activePower10minrollingavg' in content:
            result.ActivePower10minrollingavg = content['activePower10minrollingavg']
        if 'adjustedWindSpeed' in content:
            result.AdjustedWindSpeed = content['adjustedWindSpeed']
        if 'areValuesCaptured' in content:
            result.AreValuesCaptured = content['areValuesCaptured']
        if 'averagePrice' in content:
            result.AveragePrice = content['averagePrice']
        if 'averageWindSpeed' in content:
            result.AverageWindSpeed = content['averageWindSpeed']
        if 'canBeAcknowledged' in content:
            result.CanBeAcknowledged = content['canBeAcknowledged']
        if 'expectedPower' in content:
            result.ExpectedPower = content['expectedPower']
        if 'expectedPower10minrollingavg' in content:
            result.ExpectedPower10minrollingavg = content[
                'expectedPower10minrollingavg'
            ]
        if 'hasChildren' in content:
            result.HasChildren = content['hasChildren']
        if 'isAcknowledged' in content:
            result.IsAcknowledged = content['isAcknowledged']
        if 'isAnnotated' in content:
            result.IsAnnotated = content['isAnnotated']
        if 'isLocked' in content:
            result.IsLocked = content['isLocked']
        if 'manufacturer' in content:
            result.Manufacturer = content['manufacturer']
        if 'operatingState' in content:
            result.OperatingState = content['operatingState']
        if 'path' in content:
            result.Path = content['path']
        if 'powerRated' in content:
            result.PowerRated = content['powerRated']
        if 'price' in content:
            result.Price = content['price']
        if 'revenueDelta' in content:
            result.RevenueDelta = content['revenueDelta']
        if 'severity' in content:
            result.Severity = content['severity']
        if 'templateName' in content:
            result.TemplateName = content['templateName']
        if 'totalRevenueLoss' in content:
            result.TotalRevenueLoss = content['totalRevenueLoss']
        if 'turbine' in content:
            result.Turbine = content['turbine']
        if 'windFarm' in content:
            result.WindFarm = content['windFarm']
        if 'windSpeed' in content:
            result.WindSpeed = content['windSpeed']

        return result

    def toDictionary(self) -> dict[str, Any]:
        result = super().toDictionary()

        if self.AcknowledgedBy is not None:
            result['acknowledgedBy'] = self.AcknowledgedBy
        if self.AcknowledgedDate is not None:
            result['acknowledgedDate'] = self.AcknowledgedDate
        if self.ActivePower is not None:
            result['activePower'] = self.ActivePower
        if self.ActivePower10minrollingavg is not None:
            result['activePower10minrollingavg'] = self.ActivePower10minrollingavg
        if self.AdjustedWindSpeed is not None:
            result['adjustedWindSpeed'] = self.AdjustedWindSpeed
        if self.AreValuesCaptured is not None:
            result['areValuesCaptured'] = self.AreValuesCaptured
        if self.AveragePrice is not None:
            result['averagePrice'] = self.AveragePrice
        if self.AverageWindSpeed is not None:
            result['averageWindSpeed'] = self.AverageWindSpeed
        if self.CanBeAcknowledged is not None:
            result['canBeAcknowledged'] = self.CanBeAcknowledged
        if self.ExpectedPower is not None:
            result['expectedPower'] = self.ExpectedPower
        if self.ExpectedPower10minrollingavg is not None:
            result['expectedPower10minrollingavg'] = self.ExpectedPower10minrollingavg
        if self.HasChildren is not None:
            result['hasChildren'] = self.HasChildren
        if self.IsAcknowledged is not None:
            result['isAcknowledged'] = self.IsAcknowledged
        if self.IsAnnotated is not None:
            result['isAnnotated'] = self.IsAnnotated
        if self.IsLocked is not None:
            result['isLocked'] = self.IsLocked
        if self.Manufacturer is not None:
            result['manufacturer'] = self.Manufacturer
        if self.OperatingState is not None:
            result['operatingState'] = self.OperatingState
        if self.Path is not None:
            result['path'] = self.Path
        if self.PowerRated is not None:
            result['powerRated'] = self.PowerRated
        if self.Price is not None:
            result['price'] = self.Price
        if self.RevenueDelta is not None:
            result['revenueDelta'] = self.RevenueDelta
        if self.Severity is not None:
            result['severity'] = self.Severity
        if self.TemplateName is not None:
            result['templateName'] = self.TemplateName
        if self.TotalRevenueLoss is not None:
            result['totalRevenueLoss'] = self.TotalRevenueLoss
        if self.Turbine is not None:
            result['turbine'] = self.Turbine
        if self.WindFarm is not None:
            result['windFarm'] = self.WindFarm
        if self.WindSpeed is not None:
            result['windSpeed'] = self.WindSpeed

        return result
