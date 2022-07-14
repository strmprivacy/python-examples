import logging

from strmprivacy.driver import ClientConfig, StrmPrivacyClient

from args import StrmPrivacyProperties


class ClientBuilder(object):

    @staticmethod
    def create_strm_privacy_client() -> StrmPrivacyClient:
        args = StrmPrivacyProperties.from_args()

        config = ClientConfig(
            log_level=logging.DEBUG,
        )

        return StrmPrivacyClient(args.client_id, args.client_secret, config)
