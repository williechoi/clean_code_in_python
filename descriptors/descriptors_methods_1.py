# descriptors_methods_1.py

class DescriptorClass:
    """
    instance: client
    owner: ClientClass
    """
    def __get__(self, instance, owner):
        if instance is None:
            return f"{self.__class__.__name__}.{owner.__name__}"
        return f"value for {instance}"


class ClientClass:
    descriptor = DescriptorClass()


print(ClientClass.descriptor)
print(ClientClass().descriptor)
