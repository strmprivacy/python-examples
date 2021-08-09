# Stream Machine Python Driver Examples

This repository consists of three parts, `sender-async.py`, `sender_sync.py`, and `receiver.py`. All require you to provide a `billingId` (your customer identifier), a `clientId` (which identifies the stream you're sending data to or consuming data from), and a `clientSecret`.

In order to run the examples, make sure to provide these properties as arguments. For convenience, a `Makefile` is also provided, which can be used to run the respective targets. You'll be asked for the required inputs.

## Installation

Before you can run the examples, ensure to run `make install-dependencies`, which installs the dependencies in the `requirements.txt`.

## Important remarks

Ensure that the following `strmMeta` schema properties are filled out:

- `eventContractRef`: should be a full reference to the Event Contract that you want to use for the events you're sending. Example: `streammachine/example/1.2.3`
- `consentLevels`: should be the consent levels that are applicable for the event being sent. Typically, this matches the consent given by the end user.

## Need help?

See our [documentation](https://docs.streammachine.io) or [reach out to us](https://docs.streammachine.io/docs/latest/contact/index.html).

