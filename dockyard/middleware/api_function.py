from functools import wraps

from ..dependency_injection import di

def api_function():
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with di.di_scope():
                return di.make_injected_call(func, *args, **kwargs)
        
        return inner
    return wrapper