class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    obj_module = obj.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': obj_module}
    return info

my_object = MyClass(10)
object_info = introspection_info(my_object)
print(object_info)