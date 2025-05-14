from ...application import app, security_schemas
from ...middleware.api_function import api_function
from ...models.errors.error_response import ErrorResponse
from ...models.paths.name_path import NamePath
from ...models.tags.tag_list import TagList
from ...utils import http

@app.get('/v2/<path:name>/tags/list',
         security=security_schemas,
         responses={
             200: TagList,
             404: ErrorResponse
        })
@api_function()
def docker_registry_v2_name_tags_list(path: NamePath):
    return http.ok(TagList(name=path.name,tags=['latest']))