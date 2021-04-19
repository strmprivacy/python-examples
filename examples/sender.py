import asyncio
import logging
import sys

from clickstream.io.streammachine.public_schemas.clickstream import ClickstreamEvent

from streammachine.driver import StreamMachineClient, ClientConfig, StreamMachineEvent, current_time_millis, \
    SerializationType

from args import StreamMachineProperties

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class Sender(object):
    """
    An Asynchronous generator that periodically creates an event and sends it to streammachine
    """

    def __init__(self, billing_id, client_id, client_secret):
        self._config = ClientConfig(log_level=logging.DEBUG)
        self._client = StreamMachineClient(billing_id, client_id, client_secret, self._config)
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
    event = ClickstreamEvent()
    event.abTests = ["abc"]
    event.eventType = "button x clicked"
    event.customer.id = "integration-test"
    event.referrer = "https://www.streammachine.io"
    event.userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    event.producerSessionId = "session-01"
    event.conversion = 1

    event.strmMeta.timestamp = current_time_millis()
    event.strmMeta.schemaId = "clickstream"
    event.strmMeta.nonce = 0
    event.strmMeta.consentLevels = [0, 1, 2]
    event.url = "https://portal.streammachine.io"

    return event


async def main(props):
    sender = Sender(props.billing_id, props.client_id, props.client_secret)
    await sender.start_timers()  # re-authorization jwt tokens

    async for response in sender:
        if response == 204:  # event correctly accepted by endpoint
            log.info(f"Event sent, response {response}")
        else:
            log.error(f"Something went wrong while trying to send event to Stream Machine, response: {response}")

        await asyncio.sleep(0.2)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    asyncio.run(main(StreamMachineProperties.from_args()))
