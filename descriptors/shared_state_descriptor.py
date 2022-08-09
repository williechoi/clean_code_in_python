# shared State descriptor
# Acts like a Singleton Object

class SharedDataDescriptor:
    def __init__(self, initial_value, name=None):
        self.value = initial_value
        self._name = name

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # return instance.__dict__[self._name]
        return self.value

    def __set__(self, instance, value):
        # instance.__dict__[self._name] = value
        self.value = value


class ClientClass:
    descriptor = SharedDataDescriptor("OK")


client1 = ClientClass()
print(client1.descriptor)

client2 = ClientClass()
print(client2.descriptor)

client1.descriptor = "FAIL"
print(client1.descriptor)
print(client2.descriptor)

client2.descriptor = "PASS"
print(client1.descriptor)
print(client2.descriptor)
