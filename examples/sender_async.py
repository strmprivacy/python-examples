import asyncio
import logging
import sys

from streammachine.driver import SerializationType
from streammachine_io_streammachine_schemas_demo_v1.io.streammachine.schemas.demo.v1 import DemoEvent

from client_builder import ClientBuilder

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class Sender(object):
    """
    An Asynchronous generator that periodically creates an event and sends it to streammachine
    """

    def __init__(self):
        self._client = ClientBuilder.create_stream_machine_client()

    def __aiter__(self):
        return self

    async def __anext__(self):
        event = create_avro_event()
        return await self._client.send(event, SerializationType.AVRO_BINARY)

    async def start_timers(self):
        await self._client.start_timers()


def create_avro_event():
    event = DemoEvent()

    event.strmMeta.eventContractRef = "streammachine/example/1.2.3"
    event.strmMeta.consentLevels = [0]

    event.unique_identifier = "string"
    event.some_sensitive_value = "A value that should be encrypted"
    event.consistent_value = "a-user-session"
    event.not_sensitive_value = "Anyone is free to see this text."

    return event


async def main():
    sender = Sender()
    await sender.start_timers()  # re-authorization jwt tokens

    async for response in sender:
        if response == 204:  # event correctly accepted by endpoint
            log.info(f"Event sent, response {response}")
        else:
            log.error(f"Something went wrong while trying to send event to Stream Machine, response: {response}")

        await asyncio.sleep(0.2)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    asyncio.run(main())
