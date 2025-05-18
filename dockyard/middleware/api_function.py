from functools import wraps

from ..dependency_injection import di
from ..enums.auth_mode import AuthMode
from ..service.user_context import UserContext

def api_function(allowed_auth_mode: AuthMode = AuthMode.Any):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with di.di_scope():
                user_context: UserContext = di.get_instance(UserContext)

                user_context.handle_auth(allowed_auth_mode)

                return di.make_injected_call(func, *args, **kwargs)
        
        return inner
    return wrapper