def introspection_info(obj):
    type_ = type(obj).__name__
    attribute = getattr(obj, "__dir__")
    methods = dir(obj)
    module = obj.__class__.__module__
    info = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module}
    return info


number_info = introspection_info(42)
print(number_info)
