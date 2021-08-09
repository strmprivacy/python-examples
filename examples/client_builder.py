import logging

from streammachine.driver import ClientConfig, StreamMachineClient

from args import StreamMachineProperties


class ClientBuilder(object):

    @staticmethod
    def create_stream_machine_client() -> StreamMachineClient:
        args = StreamMachineProperties.from_args()

        config = ClientConfig(log_level=logging.DEBUG)

        return StreamMachineClient(args.billing_id, args.client_id, args.client_secret, config)
