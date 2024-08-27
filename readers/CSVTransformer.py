import copy
import csv
import itertools
from datetime import datetime, timedelta
from typing import Any, get_args, get_origin, get_type_hints

from adh_sample_library_preview import SdsUom, UomValueInput

import global_settings

class CSVTransformer:
    def __init__(
        self,
        file: str,
        event_class: type,
        index_field: str = None,
        max_cache_length: int = 1000,
        units_of_measure: dict[str, SdsUom] = None,
        loop=True,
    ):
        self.__file = file
        self.__event_class = event_class
        self.__max_cache_length = max_cache_length
        self.__cache_index = 0
        self.__cache = []
        self.__index = 0
        self.__datetime_fields = set()
        self.__units_of_measure = units_of_measure
        self.__loop = loop
        self.__index_field = index_field
        self.__data_start = None
        self.__data_end = None
        self.__offset = None
        self.__populate_cache()
        self.__data_start = (
            self.__cache[0].get(self.__index_field) if index_field and not (global_settings.application_mode is global_settings.ApplicationMode.Setup
        or global_settings.application_mode is global_settings.ApplicationMode.Cleanup) else None
        )

    def __iter__(self):
        return self

    def get_data_start(self):
        return self.__data_start

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value: timedelta):
        self.__offset = value

    def __populate_cache(self):
        if (global_settings.application_mode is global_settings.ApplicationMode.Setup
        or global_settings.application_mode is global_settings.ApplicationMode.Cleanup):
            return

        self.__cache.clear()

        with open(self.__file, newline='') as file:
            # For longer files we can get the next chunk of data
            reader = csv.DictReader(file)
            reader = itertools.islice(reader, self.__cache_index, self.__cache_index + self.__max_cache_length)
            for row in reader:
                self.__cache.append(self.__transform_row(row))
                self.__data_end = self.__cache[-1].get(self.__index_field)
                self.__cache_index += 1

    def __transform_value(self, name: str, value: Any, value_type: type):
        try:
            if value_type == datetime:
                self.__datetime_fields.add(name)
                return datetime.fromisoformat(value)
            elif value == '' and (value_type == float or value_type == int):
                return None
            if get_origin(value_type) is UomValueInput:
                if self.__units_of_measure and name in self.__units_of_measure:
                    return UomValueInput(
                        self.__transform_value(
                            'Value',
                            value,
                            get_args(value_type)[0],
                        ),
                        self.__units_of_measure[name],
                    )
                else:
                    return UomValueInput(
                        self.__transform_value(
                            'Value',
                            value,
                            get_args(value_type)[0],
                        ),
                        None,
                    )
            return value_type(value)
        except:
            pass

        return value

    def __transform_row(self, row):
        if not row:
            return None
        new_row = {}
        properties = get_type_hints(self.__event_class)
        for name, value in row.items():
            new_row.update(
                {name: self.__transform_value(name, value, properties[name])}
            )
        return new_row

    def __next__(self):
        if self.__index >= len(self.__cache):
            self.__index = 0
            self.__populate_cache()
            # Determine what to do if we reached the end of the file
            if len(self.__cache) == 0 and self.__loop:
                self.__cache_index = 0
                self.__offset += self.__data_end - self.__data_start
                self.__populate_cache()

        if self.__index < len(self.__cache):
            row = self.__cache[self.__index]

            # Add time offset to datetime fields
            row_copy = copy.deepcopy(row)
            if self.__offset:
                for datetime_field in self.__datetime_fields:
                    row_copy[datetime_field] += self.__offset

            self.__index += 1
            return row_copy
        else:
            raise StopIteration
