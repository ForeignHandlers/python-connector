import re
from typing import List

from .constants import EXCLUDE_COMPLEX_TYPES_REGEXP
from foreign_handlers.constants import (
    PRIMITIVE_TYPES_MAPPER,
    SUPPORTED_COMPLEX_TYPES,
    SUPPORTED_PRIMITIVE_TYPES,
)
from foreign_handlers.utilities import get_type_value


def convert(type: str) -> str:
    if type.startswith("Dict") or type.startswith("Mapper"):
        return convert_dict(type)

    if type.startswith("List"):
        return convert_list(type)

    if type.startswith("Tuple"):
        return convert_tuple(type)

    if type.startswith("Union"):
        return convert_union(type)

    return ""


def convert_python_to_typescript(types_string: str) -> List[str]:
    ts_types = []
    type_args = re.split(EXCLUDE_COMPLEX_TYPES_REGEXP, types_string)

    for type_arg in type_args:
        type_value_basic = get_type_value(type_arg)

        if type_arg in PRIMITIVE_TYPES_MAPPER:
            ts_types.append(PRIMITIVE_TYPES_MAPPER[type_arg])
            continue

        if type_value_basic in SUPPORTED_COMPLEX_TYPES:
            ts_types.append(convert(type_arg))
            continue

        raise ValueError(f"Unsupported type found during conversion. Type: {type_arg}.")

    return ts_types


def convert_dict(type: str) -> str:
    brackets_start = 0

    try:
        brackets_start = type.index("[")
    except ValueError:
        return "Record<string, unknown>"

    type_args = type[brackets_start + 1 : -1].split(", ", 1)

    if type_args[0] not in SUPPORTED_PRIMITIVE_TYPES:
        raise ValueError(f"Dict key must be a primitive. Type: {type}.")

    if len(type_args) == 1:
        return f"Record<{PRIMITIVE_TYPES_MAPPER[type_args[0]]}, unknown>"

    type_value_basic = get_type_value(type_args[1])

    if type_args[1] in SUPPORTED_PRIMITIVE_TYPES:
        return f"Record<{PRIMITIVE_TYPES_MAPPER[type_args[0]]}, {PRIMITIVE_TYPES_MAPPER[type_args[1]]}>"

    if type_value_basic in SUPPORTED_COMPLEX_TYPES:
        return (
            f"Record<{PRIMITIVE_TYPES_MAPPER[type_args[0]]}, {convert(type_args[1])}>"
        )

    raise ValueError(f"Dict value is not supported.Type: {type}.")


def convert_tuple(type: str) -> str:
    brackets_start = 0

    try:
        brackets_start = type.index("[")
    except ValueError:
        raise ValueError("Don't use tuple type without arguments")

    ts_types = convert_python_to_typescript(type[brackets_start + 1 : -1])

    types_string = ", ".join(ts_types)

    return f"[{types_string}]"


def convert_union(type: str) -> str:
    brackets_start = 0

    try:
        brackets_start = type.index("[")
    except ValueError:
        raise ValueError("Don't use union type without arguments")

    ts_types = convert_python_to_typescript(type[brackets_start + 1 : -1])

    if len(ts_types) < 2:
        raise ValueError("Union must have 2 or more arguments")

    return " | ".join(ts_types)


def convert_list(type: str) -> str:
    brackets_start = 0

    try:
        brackets_start = type.index("[")
    except ValueError:
        return "any[]"

    type_arg = type[brackets_start + 1 : -1]

    if type_arg in SUPPORTED_PRIMITIVE_TYPES:
        return f"{PRIMITIVE_TYPES_MAPPER[type_arg]}[]"

    type_value_basic = get_type_value(type_arg)

    if type_value_basic in SUPPORTED_COMPLEX_TYPES:
        return f"{convert(type_arg)}[]"

    raise ValueError(f"List value is not supported. Type: {type}.")
