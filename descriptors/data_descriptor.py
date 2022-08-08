class DataDescriptor:

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return 42

    def __set__(self, instance, value):
        print("setting %s.descriptor to %s" % (instance, value))
        instance.__dict__["descriptor"] = value

        # ---- this line will result in infinite recursion... ----
        # setattr(instance, "descriptor", value)


class ClientClass:
    descriptor = DataDescriptor()


print(ClientClass.descriptor)
client = ClientClass()
print(client.descriptor)

client.descriptor = 8080

# data descriptor value is fetched.
print(client.descriptor)
print(vars(client))
print(client.__dict__["descriptor"])

del client.descriptor