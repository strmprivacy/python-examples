import logging
import random
import sys
import time
import uuid

from streammachine.driver.client.syncsender import SyncSender
from streammachine_io_streammachine_schemas_demo_v1.io.streammachine.schemas.demo.v1 import DemoEvent

from args import StreamMachineProperties


def create_avro_event():
    event = DemoEvent()

    event.strmMeta.eventContractRef = "streammachine/example/1.2.3"
    event.strmMeta.consentLevels = [random.randint(0, 3)]

    event.unique_identifier = str(uuid.uuid4())
    event.some_sensitive_value = "A value that should be encrypted"
    event.consistent_value = "a-user-session"
    event.not_sensitive_value = "Anyone is free to see this text."

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
