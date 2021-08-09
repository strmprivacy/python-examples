import asyncio
import json
import logging
import sys

from args import StreamMachineProperties
from client_builder import ClientBuilder


async def event_handler(event):
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
    client = ClientBuilder.create_stream_machine_client()
    await client.start_timers()
    await client.start_receiving_ws(True, event_handler)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    asyncio.run(main(StreamMachineProperties.from_args()))
