class DescriptorWithName:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, value):
        if instance is None:
            return self

        print("getting %r attribute from %r" % (self.name, instance))
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DescriptorWithName2:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, value):
        if instance is None:
            return self

        print("getting %r attribute from %r" % (self.name, instance))
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ClientClass:
    descriptor = DescriptorWithName("descriptor")


class ClientClass2:
    # because of __set_name__ dunder method, we don't need to write the attribute name twice.
    descriptor = DescriptorWithName2()


client = ClientClass()
client.descriptor = "value"
print(client.descriptor)

client2 = ClientClass2()
client2.descriptor = "You are generous!"
print(client2.descriptor)
