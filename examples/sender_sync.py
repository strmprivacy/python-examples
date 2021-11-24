import logging
import random
import sys
import time
import uuid

from strmprivacy.driver.client.syncsender import SyncSender
from strmprivacy_io_strmprivacy_schemas_demo_v1.io.strmprivacy.schemas.demo.v1 import DemoEvent

from args import StrmPrivacyProperties


def create_avro_event():
    event = DemoEvent()

    event.strmMeta.eventContractRef = "strmprivacy/example/1.2.3"
    event.strmMeta.consentLevels = [random.randint(0, 3)]

    event.uniqueIdentifier = str(uuid.uuid4())
    event.someSensitiveValue = "A value that should be encrypted"
    event.consistentValue = "a-user-session"
    event.notSensitiveValue = "Hello from Python"

    return event


def main():
    props = StrmPrivacyProperties.from_args()
    logging.basicConfig(stream=sys.stderr)

    sender = SyncSender(props.billing_id, props.client_id, props.client_secret)
    sender.start()

    sender.wait_ready()

    while True:
        event = create_avro_event()
        r = sender.send_event(event)
        print(r)
        time.sleep(0.2)


if __name__ == '__main__':
    main()
