from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass
class StrmPrivacyProperties(object):
    billing_id: str
    client_id: str
    client_secret: str

    @classmethod
    def from_args(cls):
        parser = ArgumentParser()
        parser.add_argument("--billing-id", dest="billing_id",
                            help="The client id for this input stream",
                            required=True
                            )
        parser.add_argument("--client-id", dest="client_id",
                            help="The client id for this input stream",
                            required=True
                            )
        parser.add_argument("--client-secret", dest="client_secret",
                            help="The client id for this input stream",
                            required=True
                            )

        args = parser.parse_args()

        return StrmPrivacyProperties(args.billing_id, args.client_id, args.client_secret)
