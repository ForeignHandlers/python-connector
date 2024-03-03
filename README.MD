# Python Connector

This library acts as a plugin for [Foreign Handlers](https://github.com/ForeignHandlers/foreign-handlers), enabling the execution of Python functions within its ecosystem. It facilitates seamless integration by automatically generating TypeScript type annotations from Python function signatures.

## Installation

You can install Python Connector using pip:

```bash
pip install python-connector
```

## Usage

To use Python Connector, import the connect function and pass your desired Python function as an argument. Here's a basic example:

```python
from foreign_handlers import connect

def example(arg1, arg2):
    return arg1 + arg2

# Connect the function to Foreign Handlers
connect(example)
```

## Types

Python Connector can generate TypeScript type annotations based on Python function signatures. For example, consider the following Python function:

```python
def example(a: str, b: int) -> str:
    return a * b
```

This function corresponds to the following TypeScript type:

```ts
function example(a: string, b: number): string;
```

You can view the generated types by running the script with the `--types` argument.

It's important to note that only serializable JSON types are supported:

| Primitives | Data structures | Combined types |
| ---------- | --------------- | -------------- |
| str        | Dict            | Optional       |
| int        | List            | Tuple          |
| float      | Mapping         | Union          |
| bool       |                 | Literal        |
| Any        |                 |                |

However, if annotations are missing, the generated TypeScript type will default to Any.
