import logging
import sys
import time

from clickstream.io.streammachine.public_schemas.clickstream import ClickstreamEvent
from streammachine.driver import StreamMachineEvent, current_time_millis
from streammachine.driver.client.syncsender import SyncSender

from args import StreamMachineProperties


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


def main():
    props = StreamMachineProperties.from_args()
    logging.basicConfig(stream=sys.stderr)

    sender = SyncSender(props.billing_id, props.client_id, props.client_secret)
    sender.start()

    sender.wait_ready()

    while True:
        event = create_avro_event()
        sender.send_event(event)
        time.sleep(0.2)


if __name__ == '__main__':
    main()
