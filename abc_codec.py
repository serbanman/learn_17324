from abc import ABCMeta, abstractmethod, abstractproperty


class ABCCodec(metaclass=ABCMeta):
    name: str

    @property
    @abstractmethod
    def some_codec_info(self):
        raise NotImplementedError

    def decode(self, file):
        print(f'Using the {self.name} codec')
        data = file.read()
        # do something

    def save(self, file):
        file.write(self.some_codec_info)


