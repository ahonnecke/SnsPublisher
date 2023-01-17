#!/usr/bin/env python3

import json
import logging
import sys
from abc import ABC
from functools import cached_property
from subprocess import PIPE, Popen
from typing import Dict

import boto3
from argdantic import ArgParser

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger("botocore").setLevel(logging.ERROR)

LOGGER = logging.getLogger(__name__)


class BaseAwsWrapper(ABC):
    """Base aws class with shared functionality."""

    def __init__(self, profile_name: str):
        """Initialize the baseaws object."""
        self.region = "us-west-2"
        self.profile_name = profile_name

        if not self.is_logged_in():
            LOGGER.error("Please log in to AWS cli")
            sys.exit(1)

    def cli_execute(self, command):
        """Shell out and exectute a command."""
        with Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE) as process:
            output, err = process.communicate(
                b"input data that is passed to subprocess' stdin"
            )
            if err:
                LOGGER.error(err.decode("utf-8"))

        return output.decode("utf-8")

    def aws_cli_execute(self, command):
        """Shell out and exectute an AWS command."""
        command.insert(0, f"--profile={self.profile_name}")
        command.insert(0, "aws")
        return self.cli_execute(command)

    @cached_property
    def identity(self) -> dict:
        # TODO make use boto3?????
        if identity := self.aws_cli_execute(["sts", "get-caller-identity"]):
            return json.loads(identity)
        return {}

    @cached_property
    def config_identity(self):
        return self.aws_cli_execute(["configure", "list"]).split("\n")

    def is_logged_in(self) -> bool:
        """
        Check to see if the user is logged in to AWS
        """
        return bool(self.identity)

    @cached_property
    def session(self):
        return boto3.Session(profile_name=self.profile_name)

    @cached_property
    def sns(self):
        return self.session.client("sns", region_name=self.region)


class Publisher(BaseAwsWrapper):
    ARN = "arn:aws:sns:us-west-2:024726604032:AshtonTest"

    def send_versioned_sns(self, message: Dict, version, sdlc_env):
        return self.sns.publish(
            TargetArn=self.ARN,
            Message=json.dumps({"default": json.dumps(message)}),
            MessageStructure="json",
            MessageAttributes={
                "CirrusVersion": {"DataType": "String", "StringValue": version},
                "SDLCEnv": {"DataType": "String", "StringValue": sdlc_env},
            },
        )


parser = ArgParser()


@parser.command()
def publish(profile: str):
    """
    Publish a test message to SNS.
    """
    s = Publisher(profile_name=profile)

    test_message = {"foo": "bar"}

    res = s.send_versioned_sns(test_message, "v1.1.0", "PROD")
    print(res)

    res = s.send_versioned_sns(test_message, "v2.1.0", "DEV")
    print(res)


if __name__ == "__main__":
    parser()
