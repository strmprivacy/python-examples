# Stream Machine Python Driver Examples

This repository consists of three parts, `sender.py`, `syncsender.py`, and `receiver.py`. All require you to provide a `billingId` (your customer identifier), a `clientId` (which identifies the stream you're sending data to or consuming data from), and a `clientSecret`.

In order to run the examples, make sure to provide these properties as arguments. For convenience, a `Makefile` is also provided, which can be used to run the respective targets. You'll be asked for the required inputs.

## Installation

Before you can run the examples, ensure to run `make install-dependencies`, which installs the dependencies in the `requirements.txt`.

## Important remarks

Ensure that the `strmMeta` schema properties are filled out correctly, especially the `schemaId`. This must match the name of the schema that you are using (in this example, it's `clickstream`).

Note: we're working on removing some parts of the `strmMeta`, as they are error prone (such as the `schemaId`).

## Need help?

See our [documentation](https://docs.streammachine.io) or [reach out to us](https://docs.streammachine.io/docs/0.1.0/contact/index.html).

