from flask_openapi3 import OpenAPI, Info

basic = {
  "type": "http",
  "scheme": "basic"
}

info = Info(title='Dockyard Docker Registry', version='0.1.0')

security_schemas = {'basic':basic}

app = OpenAPI(__name__, info=info, security_schemes=security_schemas)