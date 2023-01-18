#!/usr/bin/env python3

import json
import logging
import sys
from typing import Dict, Union

from argdantic import ArgParser

from src.cirrus.aws import BaseAwsWrapper
from src.cirrus.compressor import ZStandard

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger("botocore").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)


class Publisher(BaseAwsWrapper):
    """Extend aws cli object and add send versioned sns behavior."""

    def __init__(
        self,
        profile_name: str,
        arn_name: str,
    ):
        super().__init__(profile_name)
        self.ARN = arn_name

    def send_versioned_sns(self, message: Union[Dict, str], version, sdlc_env):
        """Send versioned sns behavior."""
        if isinstance(message, Dict):
            message = json.dumps({"default": json.dumps(message)})
            struct = "json"
        else:
            struct = "string"

        return self.sns.publish(
            TargetArn=self.ARN,
            Message=message,
            MessageStructure=struct,
            MessageAttributes={
                "CirrusVersion": {"DataType": "String", "StringValue": version},
                "SDLCEnv": {"DataType": "String", "StringValue": sdlc_env},
            },
        )


parser = ArgParser()


@parser.command()
def publish(profile: str):
    """Publish a test message to SNS."""
    s = Publisher(
        profile_name=profile, arn_name="arn:aws:sns:us-west-2:024726604032:AshtonTest"
    )

    v1_message = {"foo": "bar"}

    res = s.send_versioned_sns(v1_message, "v1.1.0", "PROD")
    print(res)

    zstd = ZStandard()
    v2_message = zstd.compress(v1_message)
    res = s.send_versioned_sns(v2_message.decode("utf-8"), "v2.1.0", "DEV")
    print(res)


if __name__ == "__main__":
    parser()
