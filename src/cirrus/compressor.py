"""Compression and decompression functionality."""
import base64
import json
from functools import cached_property
from typing import Dict, Union

import zstandard


class ZStandard:
    """Cache zstd decompressor and exposing decoding.

    This object caches the zstd objects.  It does not create the objects on import,
    this is done intentionally so that if there is an error when attempting to
    create the object it doesn't happen on imported, because
    that makes debugging really hard.
    """

    LEVEL = 9

    @cached_property
    def decompressor(self):
        """Cache zstd decompressor."""
        return zstandard.ZstdDecompressor()

    @cached_property
    def compressor(self):
        """Cache zstd compressor."""
        return zstandard.ZstdCompressor(level=self.LEVEL)

    def decompress(self, raw_input: str) -> str:
        """Decompress and decompress raw_input."""
        base64_decompressd = base64.b64decode(raw_input)
        return self.decompressor.decompress(base64_decompressd).decode()

    def compress(self, raw_input: Union[str, Dict]) -> str:
        """Decompress and decompress raw_input, if it's encoded."""
        if isinstance(raw_input, Dict):
            return self._compress_dict(raw_input)
        elif isinstance(raw_input, str):
            return self._compress_str(raw_input)
        else:
            raise TypeError("Attempt to compress unsupported type")

    def _compress_str(self, raw_input: str) -> str:
        """Decompress and decompress raw_input, if it's encoded."""
        return base64.b64encode(self.compressor.compress((raw_input).encode("utf-8")))

    def _compress_dict(self, _dict: Dict) -> str:
        """Decompress and decompress raw_input, if it's encoded."""
        return self._compress_str(json.dumps(_dict))

    def decompress_or_not(self, raw_input: str) -> str:
        """Decompress and decompress raw_input, if it's encoded."""
        try:
            # Attempt a b64 decompress, if this fails return the raw input
            return self.decompress(raw_input)
        except Exception:
            return raw_input
