from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass
class StrmPrivacyProperties(object):
    client_id: str
    client_secret: str
    gateway_host: str
    auth_host: str


    @classmethod
    def from_args(cls):
        parser = ArgumentParser()
        parser.add_argument("--client-id", dest="client_id",
                            help="The client id for this input stream",
                            required=True
                            )
        parser.add_argument("--client-secret", dest="client_secret",
                            help="The client id for this input stream",
                            required=True
                            )
        parser.add_argument("---id", dest="billing_id",
                            help="The client id for this input stream",
                            required=False
                            )
        parser.add_argument("--gateway-host", dest="gateway_host",
                            default="events.strmprivacy.io",
                            help="The gateway host for sending events",
                            required=False
                            )
        parser.add_argument("--auth-host", dest="auth_host",
                            default="accounts.strmprivacy.io",
                            help="The url host for the authentication",
                            required=False
                            )
        args = parser.parse_args()

        return StrmPrivacyProperties(args.client_id, args.client_secret, args.gateway_host, args.auth_host)
