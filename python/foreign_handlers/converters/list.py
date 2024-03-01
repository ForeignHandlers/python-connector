from ..constants import (
    PRIMITIVE_TYPES_MAPPER,
)


def convert_list(type: str) -> str:
    brackets_start = 0

    try:
        brackets_start = type.index("[")
    except ValueError:
        return "any[]"

    type_arg = type[brackets_start + 1 : -1]

    if type_arg not in PRIMITIVE_TYPES_MAPPER:
        raise ValueError(f"List argument must be a primitive. Type: {type}.")

    return f"{PRIMITIVE_TYPES_MAPPER[type_arg]}[]"
