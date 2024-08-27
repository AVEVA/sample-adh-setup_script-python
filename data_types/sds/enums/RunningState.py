from omf_sample_library_preview.Models import OMFEnumType, OMFEnumValue

running_state = OMFEnumType(
    'RunningState', [OMFEnumValue('Off', 0), OMFEnumValue('On', 1)]
)
