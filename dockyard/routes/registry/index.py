from ...application import app, security_schemas
from ...middleware.api_function import api_function, AuthMode

from ...utils import http

@app.get('/v2/',
         security=security_schemas,
         responses={
             200: None,
             401: None
         })
@api_function(allowed_auth_mode=AuthMode.Docker)
def docker_registry_v2():
    return http.ok({}, headers={
    })