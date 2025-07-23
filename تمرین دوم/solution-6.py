class Mock:
    def __init__(self):
        self._methods = {}

    def __getattr__(self, name):
        if name in self._methods:
            return self._methods[name]
        else:
            def method(*args, **kwargs):
                print(f"Called method '{name}' with args: {args} and kwargs: {kwargs}")
                return None
            return method

    def __setattr__(self, name, value):
        if name == '_methods':
            super().__setattr__(name, value)
        else:
            self._methods[name] = value

mock = Mock()

mock.method_1 = lambda x: x * 2

result = mock.method_1(10)
print(f"Result: {result}")
