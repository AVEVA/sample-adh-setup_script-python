from typing import Any


def _get_parameter(content: dict[str, Any], parameter: str, required: bool) -> Any:
    if required and parameter not in content:
        raise TypeError(f'None type is not a valid {parameter}')

    if required and not content.get(parameter, None):
        raise ValueError(f'None is not a valid value for {parameter}')

    return content.get(parameter, None)
