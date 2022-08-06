# descriptors_methods_3.py

class ProtectedAttribute:
    def __init__(self, requires_role=None) -> None:
        self.permission_required = requires_role
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, user, value):
        if value is None:
            raise ValueError(f"{self._name} can't be set to None")
        user.__dict__[self._name] = value

    def __delete__(self, user):
        if self.permission_required in user.permissions:
            user.__dict__[self._name] = None
        else:
            raise ValueError(f"User {user!s} doesn't have {self.permission_required} permission!")


class User:
    """Only users with "admin" privileges can remove their email address."""

    email = ProtectedAttribute(requires_role="admin")

    def __init__(self, username: str, email: str, permission_list: list = None) -> None:
        self.username = username
        self.email = email
        self.permissions = permission_list or []

    def __str__(self):
        return self.username


admin = User("root", "root@d.com", ["admin"])
user = User("user", "user1@d.com", ["email", "helpdesk"])

print(admin.email)
del admin.email
print(admin.email)

print(user.username)
admin.username = "admin1"
print(admin.username)
del admin.username
try:
    print(admin.username)
except AttributeError:
    pass

# user.email = None
# del user.email
print(user.email)
print(user.username)
user.username = "song1"
print(user.username)
del user.username
try:
    print(user.username)
except AttributeError:
    pass

