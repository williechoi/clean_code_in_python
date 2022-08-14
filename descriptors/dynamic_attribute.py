class DynamicAttributes:

    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"
        raise AttributeError(f"{self.__class__.__name__} has no attribute {attr}")


dyn = DynamicAttributes("value")
print(dyn.attribute)

print(dyn.fallback_test)

dyn.__dict__["fallback_new"] = "new value"
print(dyn.fallback_new)

print(getattr(dyn, "something", "default"))
