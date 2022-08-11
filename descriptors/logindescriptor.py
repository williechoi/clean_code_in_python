from typing import Callable
from functools import partial
from dataclasses import dataclass
from datetime import datetime


class BaseFieldTransformation:

    def __init__(self, transformation: Callable[[], str]) -> None:
        self._name = None
        self.transformation = transformation

    def __get__(self, instance, owner):
        if instance is None:
            return self

        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


ShowOriginal = partial(BaseFieldTransformation, transformation=lambda x: x)
HideField = partial(BaseFieldTransformation, transformation=lambda x: "**redacted**")
FormatTime = partial(BaseFieldTransformation, transformation=lambda ft: ft.strftime("%Y-%m-%d %H:%M"))


@dataclass
class LoginEvent:
    username: str = ShowOriginal()
    password: str = HideField()
    ip: str = ShowOriginal()
    timestamp: datetime = FormatTime()

    def serialize(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,
        }


le = LoginEvent("Hyungsuk Choi", "qwer1234", "127.0.0.1", datetime.utcnow())
print(vars(le))
print(le.serialize())
print(le.password)
