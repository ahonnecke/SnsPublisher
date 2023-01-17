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

    Usage:
    https://i.imgur.com/t3MX46M.png

    Messages:
    https://i.imgur.com/t8koC6S.png

    Message One:
    {
      "Type" : "Notification",
      "MessageId" : "2023301a-1a24-528f-aae4-6c5b3e4ebe63",
      "TopicArn" : "arn:aws:sns:us-west-2:024726604032:AshtonTest",
      "Message" : "{\"foo\": \"bar\"}",
      "Timestamp" : "2023-01-17T22:33:14.087Z",
      "SignatureVersion" : "1",
      "Signature" : "lkgFqfZqfGR2YDoxvhoFTZ26Hm3FFwYOtIRPviEi53KJd3D0kSJMo8yITx0xc2KW4byPM3+9uL4mS5udTB6PqcnXpYMe6pm10de8sYucGFSHCWpfj6Rq0dIergHFoL2a03f8jRpSL1wcJfutkP0+Tvtsw4lqOtjjqCv0DcV8k9thLWrCSABMIBW52Xi+c6gSk4mseilud63FG/bqYCzSrDC3s8wHehrRD49qf5WS5Fa/I8nWAgz0yCOT/obdtucHRWkkB0OzMHICVyJFtBdPrxgNYDEJnEfBiXHOSfI48b7fCSzNL0WKCz8lTzyaE0MuHDLc7hWX2tEWnSKyt8jmxw==",
      "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
      "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:024726604032:AshtonTest:f1abc4f3-7665-4968-b39c-8a4c6f082d9b",
      "MessageAttributes" : {
        "SDLCEnv" : {"Type":"String","Value":"PROD"},
        "CirrusVersion" : {"Type":"String","Value":"v1.1.0"}
      }
    }

    Message Two:
    {
      "Type" : "Notification",
      "MessageId" : "78dfd581-54c7-56dc-9903-89c070ad0a30",
      "TopicArn" : "arn:aws:sns:us-west-2:024726604032:AshtonTest",
      "Message" : "{\"foo\": \"bar\"}",
      "Timestamp" : "2023-01-17T22:33:14.134Z",
      "SignatureVersion" : "1",
      "Signature" : "2v+nzp6rJR0xOoG+29YH/cBrPx7Mg+nKpljyhaH0esJKBxwaaJJSTBg6t4AG7zHaG7pvbp0BAOJ7jaBR0a+yywJJ5YUNAEHSDGcPGeM9zxpJoy3vyjM8bfZs1vozhwrEoY0HVtstm07n4Xsv+aiApY5sn1EI8l10Vua8eCB/w7tAs+0Q9wmj2EvYwSA8QsIQQR0he2m4o2boXRO15mL576qNup63SagX60f9zQRYxL7PJhXiBjY5yy8w1OUWK358W56fwnWDUXCJt7/MWINRKQatWuHs++x7yCK+jElahQNOA47vh/XQKHC1UjZEUL8rAxO7Gw3BOEfJyHnp1s+ZOw==",
      "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
      "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:024726604032:AshtonTest:f1abc4f3-7665-4968-b39c-8a4c6f082d9b",
      "MessageAttributes" : {
        "SDLCEnv" : {"Type":"String","Value":"DEV"},
        "CirrusVersion" : {"Type":"String","Value":"v2.1.0"}
      }
    }
    """
    s = Publisher(profile_name=profile)

    test_message = {"foo": "bar"}

    res = s.send_versioned_sns(test_message, "v1.1.0", "PROD")
    print(res)

    res = s.send_versioned_sns(test_message, "v2.1.0", "DEV")
    print(res)


if __name__ == "__main__":
    parser()
