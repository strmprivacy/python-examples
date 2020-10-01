# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "examples"

import asyncio
import logging
import sys

from examples.args import StreamMachineProperties
from streammachine.driver import StreamMachineClient, ClientConfig, StreamMachineEvent, current_time_millis, SerializationType
from streammachine.schema.avro.io.streammachine.schema.avro.strm_avro.v1 import StrmEvent


class Sender(object):
    """
    An Asynchronous generator that periodically creates an event and sends it to streammachine
    """

    def __init__(self, billing_id, client_id, client_secret):
        self._config = ClientConfig(log_level=logging.DEBUG)
        self._client = StreamMachineClient( billing_id, client_id, client_secret, self._config )
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

    def __aiter__(self):
        return self

    async def __anext__(self):
        event = create_avro_event()
        return await self._client.send(event, SerializationType.AVRO_BINARY)

    async def start_timers(self):
        await self._client.start_timers()


def create_avro_event() -> StreamMachineEvent:
    """
    create a dummy event
    :return:
    """
    event = StrmEvent()
    event.abtests = ["abc"]
    event.customer.id = "integration-test"
    event.sessionId = "session-01"
    event.strmMeta.timestamp = current_time_millis()
    event.strmMeta.schemaId = "schema_avro"
    event.strmMeta.nonce = 1
    event.strmMeta.keyLink = 2
    event.strmMeta.consentLevels = [0, 1, 2]
    event.url = "bananas"
    return event


async def main(props):
    sender = Sender(props.billing_id, props.client_id, props.client_secret)
    await sender.start_timers()  # re-authorization jwt tokens
    async for event in sender:
        if event == 204:  # event correctly accepted by endpoint
            print(".", end='', flush=True)
        else:
            print()
            print("event", event)

        await asyncio.sleep(0.2)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    asyncio.run(main(StreamMachineProperties.from_args()))
