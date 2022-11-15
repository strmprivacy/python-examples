import asyncio
import logging
import random
import uuid

from strmprivacy.driver import SerializationType
from strmprivacy_io_strmprivacy_schemas_demo_v1.io.strmprivacy.schemas.demo.v1 import DemoEvent

from client_builder import ClientBuilder

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class Sender(object):
    """
    An Asynchronous generator that periodically creates an event and sends it to STRM Privacy
    """

    def __init__(self):
        self._client = ClientBuilder.create_strm_privacy_client()

    def __aiter__(self):
        return self

    async def __anext__(self):
        event = create_avro_event()
        return await self._client.send(event, SerializationType.AVRO_BINARY)

    async def start_timers(self):
        await self._client.start_timers()


def create_avro_event():
    event = DemoEvent()

    event.strmMeta.eventContractRef = "strmprivacy/example/1.3.0"
    event.strmMeta.consentLevels = [random.randint(0, 3)]

    event.uniqueIdentifier = str(uuid.uuid4())
    event.someSensitiveValue = "A value that should be encrypted"
    event.consistentValue = "a-user-session"
    event.notSensitiveValue = "Hello from Python"

    return event


async def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    sender = Sender()
    await sender.start_timers()  # re-authorization jwt tokens

    logger.info("Started async sender. Only error responses are logged by the client.")

    count = 0

    async for response in sender:
        if response != 204:
            log.error(f"Something went wrong while trying to send event to STRM Privacy, response: {response}")
        await asyncio.sleep(0.2)

        count += 1
        if count % 5 == 0:
            logger.info("Sent %s events", count)


if __name__ == '__main__':
    asyncio.run(main())
