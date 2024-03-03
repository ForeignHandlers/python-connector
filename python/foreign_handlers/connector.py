from typing import Callable
from sys import stdin, stdout, stderr
from contextlib import redirect_stdout
from io import StringIO

import asyncio
import json

from foreign_handlers.constants import UID


async def execute_connector(function: Callable):
    for line in stdin:
        args = json.loads(line)

        if UID not in args.keys():
            stderr.write(f"Request doesn't contain '${UID}'")
            stderr.flush()

            return

        __uid = args.pop(UID)

        temp_stdout = StringIO()

        with redirect_stdout(temp_stdout):
            if asyncio.iscoroutinefunction(function):
                result = await function(**args)
            else:
                result = function(**args)

        stdout.write(json.dumps({f"{__uid}": result}))
        stdout.flush()
