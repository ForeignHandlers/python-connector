from typing import Any


def is_class(value: Any) -> bool:
    return str(value).startswith("<class")


def is_typing_instance(value: Any) -> bool:
    return str(value).split(".")[0] == "typing"


def get_typing_instance(value: Any) -> str:
    return str(value).replace("typing.", "", -1)


def get_type_value(value: Any) -> str:
    return value.split("[")[0]
