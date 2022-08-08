class NonDataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42


class ClientClass:
    descriptor = NonDataDescriptor()


print(ClientClass.descriptor)

client = ClientClass()
print('============== Phase A ====================')
print(client.descriptor)
print(vars(client))


print('============== Phase B ====================')
client.descriptor = 400
print(client.descriptor)
print(vars(client))

print('============== Phase C ====================')
del client.descriptor
print(client.descriptor)
