import hashlib
from datetime import datetime, timezone

from bson import json_util
from flask import g
from service.shared.resources import rebar, registry
from service.validators.register_user_schema import (USER, UserCreateSchema,
                                                     UserSchema)


def encryptString(str):
    return hashlib.md5(str.encode("utf-8")).hexdigest()

# Fix handeler validation schema
@registry.handles(
    rule="/register",
    endpoint="register_user",
    method="POST",
    request_body_schema=UserCreateSchema(),
    marshal_schema=UserSchema()
)
def register_user():
    data = rebar.validated_body
    data["created_at"] = datetime.now().replace(tzinfo=timezone.utc)
    data["type"] = USER
    data ["password"] = encryptString(data ["password"])
    user = g.database.users.insert(data)
    return json_util.dumps(g.database.users.find_one({"_id" : user}))
