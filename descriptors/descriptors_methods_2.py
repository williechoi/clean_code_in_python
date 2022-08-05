from typing import Any, Callable
import re


class Validation:
    def __init__(self, validation_function: Callable[[Any], bool], error_msg: str) -> None:
        self.validation_function = validation_function
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_msg}")


class Field:
    def __init__(self, *validations):
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self._name]

    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value


class ClientClass:
    descriptor = Field(
        Validation(lambda x: str.isdigit(str(x)), "is not a number"),
        Validation(lambda x: re.match(r"(\d{8})|(\d{4}-\d{2}-\d{2})", str(x)) is not None, "is not a valid date-like integer")
    )


client = ClientClass()
client.descriptor = 20210101
print(client.descriptor)

client.descriptor = "20221202"
print(client.descriptor)

client.descriptor = "invalid value"

