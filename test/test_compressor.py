#!/usr/bin/env python3

import json
from uuid import uuid4

from src.cirrus.compressor import ZStandard


def test_json(message):
    zstd = ZStandard()

    output = json.loads(zstd.decompress(zstd.compress(message)))
    assert output == message, "Zstd compression and decompression are not equivalent."


def test_string():
    zstd = ZStandard()

    message = str(uuid4())  # Use UUID so it's unique

    output = zstd.decompress(zstd.compress(message))
    assert output == message, "Zstd compression and decompression are not equivalent."
