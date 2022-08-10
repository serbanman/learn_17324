from abc_codec import ABCCodec


class FLACCodec(ABCCodec):
    name = 'FLAC'

    @property
    def some_codec_info(self):
        return 'flac bla bla'


class ALACCodec(ABCCodec):
    name = 'ALAC'

    @property
    def some_codec_info(self):
        return 'alac bla bla'


class TAKCodec(ABCCodec):
    name = 'TAK'

    @property
    def some_codec_info(self):
        return 'tak bla bla'


class OFRCodec(ABCCodec):
    name = 'OFR'

    @property
    def some_codec_info(self):
        return 'ofr bla bla'


class WVCodec(ABCCodec):
    name = 'WV'

    @property
    def some_codec_info(self):
        return 'wv bla bla'


class WMALCodec(ABCCodec):
    name = 'WMAL'

    @property
    def some_codec_info(self):
        return 'wmal bla bla'


class MPEG4Codec(ABCCodec):
    name = 'MPEG-4'

    @property
    def some_codec_info(self):
        return 'mpeg4 bla bla'


class HEVCCodec(ABCCodec):
    name = 'HEVC'

    @property
    def some_codec_info(self):
        return 'hevc bla bla'


class H262Codec(ABCCodec):
    name = 'H.262'

    @property
    def some_codec_info(self):
        return 'h262 bla bla'


class H263Codec(ABCCodec):
    name = 'H.263'

    @property
    def some_codec_info(self):
        return 'h263 bla bla'


class VCBCodec(ABCCodec):
    name = 'VCB'

    @property
    def some_codec_info(self):
        return 'vcb bla bla'
