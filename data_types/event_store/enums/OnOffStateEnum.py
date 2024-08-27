from enum import Enum

from adh_sample_library_preview import Enumeration, EnumerationState

on_off_state_enumeration = Enumeration(
    [EnumerationState(name='on', code=1), EnumerationState(name='off', code=2)],
    '',
    'onOffState',
    id='onOffState',
)


class OnOffStateEnum(Enum):
    on = '1'
    off = '2'
