from zzcodecs import *


class Factory:
    def __init__(self, codec_name):
        self.codec_name = codec_name
        self.codec_cls = self._get_codec_cls()

    def _get_codec_cls(self):
        for codec_cls in ABCCodec.__subclasses__():
            if codec_cls.name == self.codec_name:
                return codec_cls()
        raise NotImplementedError(f"Couldn't find decoding class for {self.codec_name}")

    def decode(self, file):
        return self.codec_cls.decode(file)

    def save(self, file):
        return self.codec_cls.save(file)
