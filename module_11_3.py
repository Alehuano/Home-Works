import inspect


def introspection_info(obj):
    type_obj = type(obj).__name__  # тип объекта
    attr_obj = [attr for attr in dir(obj) if callable(getattr(obj, attr))]  # атрибуты объекта
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method))]  # методы объекта
    module_obj = inspect.getmodule(obj)  # модуль, в котором находится объект

    info_obj = {'type': type_obj, 'attributes': attr_obj, 'methods': methods_obj, 'module': module_obj}

    return info_obj


number_info = introspection_info(42)
print(number_info)
