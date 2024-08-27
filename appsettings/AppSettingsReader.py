import json
import logging
from typing import Any

from .AppSettings import AppSettings


def readAppsettings() -> AppSettings:
    """Open and parse the appsettings.json file"""

    # Try to open the configuration file
    try:
        with open(
            'appsettings.json',
            'r',
        ) as f:
            return AppSettings.fromJson(json.load(f))
    except Exception as error:
        logging.ERROR(f'Error: {str(error)}')
        logging.ERROR(f'Could not open/read appsettings.json')
        exit()


def writeAppsettings(appsettings: AppSettings):
    """Open and write the appsettings.json file"""

    # Try to open the configuration file
    try:
        with open(
            'appsettings.json',
            'w',
        ) as f:
            f.write(appsettings.toJson())
    except Exception as error:
        logging.ERROR(f'Error: {str(error)}')
        logging.ERROR(f'Could not open/write appsettings.json')
        exit()
