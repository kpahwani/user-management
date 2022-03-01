from datetime import datetime, timezone
from email.policy import default

from marshmallow import Schema, fields
from marshmallow.validate import OneOf

USER = 'user'
ADMIN = 'admin'
USER_TYPE = [USER, ADMIN]
    
        
class UserCreateSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    address_line_1 = fields.String(required=True)
    address_line_2 = fields.String()
    city = fields.String(required=True)
    state = fields.String(required=True)
    pincode = fields.Integer(required=True)
    
    
class UserSchema(Schema):
    _id = fields.Dict(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    type = fields.String(
        validate=OneOf(USER_TYPE),
        required=True
    )
    password = fields.String(required=True)
    address_line_1 = fields.String(required=True)
    address_line_2 = fields.String()
    city = fields.String(required=True)
    state = fields.String(required=True)
    pincode = fields.Integer(required=True)
    created_at = fields.Dict(required=True)
    