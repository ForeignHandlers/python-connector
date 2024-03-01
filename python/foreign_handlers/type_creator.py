from typing import Callable, Any, Dict
from .utilities import (
    get_type_value,
    get_typing_instance,
    is_typing_instance,
    is_class,
)
from .constants import (
    PRIMITIVE_TYPES_MAPPER,
    SUPPORTED_TYPES,
    SUPPORTED_COMPLEX_TYPES,
)
from .converters import convert


def get_annotations(func: Callable):
    annotations = func.__annotations__

    for key, value in annotations.items():
        if is_typing_instance(value):
            annotations[key] = get_typing_instance(value)
        elif is_class(value):
            annotations[key] = value.__name__
        else:
            raise ValueError("Unknown annotation")

    return annotations


def convert_annotations_to_typescript_types(annotations: Dict[str, Any]):
    types = {}

    for key, value in annotations.items():
        type_basic = get_type_value(value)

        if type_basic not in SUPPORTED_TYPES:
            raise ValueError(f"Unsupported type {value}. Key: {key}.")

        if value in PRIMITIVE_TYPES_MAPPER:
            types[key] = PRIMITIVE_TYPES_MAPPER[value]

        if type_basic in SUPPORTED_COMPLEX_TYPES:
            types[key] = convert(value)

    return types
