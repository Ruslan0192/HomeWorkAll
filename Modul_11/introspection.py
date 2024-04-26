
import inspect
from pprint import pprint


def introspection_info(obj):
    obj_info = {}
    obj_info['type'] = type(obj)
    obj_info['attributes'] = dir(obj)
    obj_info['methods'] = inspect.getmembers(obj)
    obj_info['module'] = __name__
    return obj_info

number_info = introspection_info(42)
pprint(number_info)
