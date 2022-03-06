from datetime import datetime, timezone
from marshmallow import Schema, fields
from service.validators.register_user_schema import UserSchema

class ListOfUserSchema(Schema):
    users = fields.List(fields.Nested(UserSchema))
