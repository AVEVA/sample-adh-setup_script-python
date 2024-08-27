from enum import Enum

from .event_types import (
    DoubleEvent,
    OnOffEvent,
    WindtopiaAutoStop,
    WindtopiaHighTurbineTemperature,
    WindtopiaLowProduction,
    double_event_type,
    on_off_event_type,
    windtopia_auto_stop,
    windtopia_high_turbine_temperature,
    windtopia_low_production,
)


class EventTypeEnum(Enum):
    DoubleEvent = (DoubleEvent, double_event_type)
    OnOffEvent = (OnOffEvent, on_off_event_type)
    WindtopiaAutoStop = (WindtopiaAutoStop, windtopia_auto_stop)
    WindtopiaHighTurbineTemperature = (
        WindtopiaHighTurbineTemperature,
        windtopia_high_turbine_temperature,
    )
    WindtopiaLowProduction = (WindtopiaLowProduction, windtopia_low_production)
