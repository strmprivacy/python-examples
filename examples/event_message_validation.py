import json
import os
from io import BytesIO

from fastavro.validation import validate
from streammachine_io_streammachine_schemas_demo_v1.io.streammachine.schemas.demo.v1 import DemoEvent
from streammachine_io_streammachine_schemas_demo_v1.schema_classes import __read_file
from streammachine_io_streammachine_schemas_demo_v1.schema_classes import __file__ as schema_classes_file

event = DemoEvent()

event.strmMeta.eventContractRef = "streammachine/example/1.2.3"
event.strmMeta.consentLevels = None

event.uniqueIdentifier = "string"
event.someSensitiveValue = "A value that should be encrypted"
event.consistentValue = "a-user-session"
event.notSensitiveValue = "Hello from Python"

schema = json.loads(__read_file(os.path.join(os.path.dirname(schema_classes_file), "schema.avsc")))

validate(event, schema)
