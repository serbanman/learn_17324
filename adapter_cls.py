class AdapterCls:
    @classmethod
    def write(cls, data):
        print(f'mocking the write: {data}')
        print('ha ha im not doing anything')
        return None

    @classmethod
    def read(cls):
        print('abracarabra im gonna reach out and grab ya')
        return None
