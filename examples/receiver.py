# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "examples"

import asyncio
import logging
import json
import sys

from examples.args import StreamMachineProperties
from streammachine.driver import StreamMachineClient, ClientConfig


async def eventHandler(event):
    """
    callback handler for the events from Streammachine

    :param event: this is either json event, or a base64 encoded avro binary, depending on the
    first parameter of StreamMachineClient.start_receiving_sse.

    Decoding an Avro binary is not yet supported.
    """
    print(json.loads(event))


async def main(props):
    """
    Your async main code that instantiates the client, starts its re-authorization timer, and installs a callback
    """
    config = ClientConfig(log_level=logging.DEBUG)
    client = StreamMachineClient( props.billing_id, props.client_id, props.client_secret, config )
    await client.start_timers()
    await client.start_receiving_sse(True, eventHandler)


if __name__ == '__main__':

    logging.basicConfig(stream=sys.stderr)
    asyncio.run(main(StreamMachineProperties.from_args()))
