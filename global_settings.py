from enum import Enum

class ApplicationMode(Enum):
    Setup = 'Setup'
    Run = 'Run'
    SetupAndRun = 'SetupAndRun'
    Cleanup = 'Cleanup'

    def __str__(self):
        return self.value

application_mode = {}