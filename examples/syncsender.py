# Ugly hack to allow absolute import from the root folder
# whatever its name is. Please forgive the heresy.
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "examples"

import sys
import time
import logging

from examples.args import StreamMachineProperties
from streammachine.driver import StreamMachineEvent, current_time_millis, SerializationType
from streammachine.driver.client.syncsender import SyncSender
from streammachine.schema.avro.io.streammachine.schema.avro.strm_avro.v1 import StrmEvent


def create_avro_event() -> StreamMachineEvent:
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


def main():
    props = StreamMachineProperties.from_args()
    logging.basicConfig(stream=sys.stderr)

    sender = SyncSender(props.billing_id, props.client_id, props.client_secret)
    sender.start()

    sender.wait_ready()

    while True:
        event = create_avro_event()
        sender.send_event(event)
        time.sleep(0.03)


if __name__ == '__main__':
    main()
