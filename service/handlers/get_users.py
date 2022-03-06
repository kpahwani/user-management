from bson import json_util
from flask import g
from service.shared.resources import rebar, registry
from service.validators.query_string_schema import SkipLimitSchema
from service.validators.get_user_schema import ListOfUserSchema

@registry.handles(
    rule="/users",
    endpoint="get_users",
    method="GET",
    query_string_schema=SkipLimitSchema(),
    # marshal_schema=ListOfUserSchema()
)
def register_user():
    validated_query_param = rebar.validated_args
    limit = validated_query_param['limit']
    skip = validated_query_param['skip']
    users = g.database.users.find().skip(skip).limit(limit)
    return json_util.dumps({
        "users": users
    })
