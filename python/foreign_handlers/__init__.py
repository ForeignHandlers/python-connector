from typing import Callable
from sys import argv
import asyncio

from foreign_handlers.types import send_types
from foreign_handlers.connector import execute_connector
from foreign_handlers.constants import TYPES_ARGV


def connect(function: Callable):
    if TYPES_ARGV in argv:
        send_types(function)
        return

    asyncio.run(execute_connector(function))
