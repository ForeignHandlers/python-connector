PRIMITIVE_TYPES_MAPPER = {
    "str": "string",
    "int": "number",
    "float": "number",
    "bool": "boolean",
    "Any": "any",
}

SUPPORTED_COMPLEX_TYPES = [
    "List",
    "Dict",
    "Mapping",
    "Tuple",
    "Union",
    "Optional",
    "Literal",
]

SUPPORTED_PRIMITIVE_TYPES = PRIMITIVE_TYPES_MAPPER.keys()


SUPPORTED_TYPES = [*SUPPORTED_PRIMITIVE_TYPES, *SUPPORTED_COMPLEX_TYPES]

TYPES_ARGV = "--types"

UID = "__uid"

RETURN = "return"
