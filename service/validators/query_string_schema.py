from marshmallow import Schema, fields
from main import app

class SkipLimitSchema(Schema):
    limit = fields.Integer(default=app.config.get("DEFAULT_PAGE_LIMIT", 100))
    skip = fields.Integer(default=app.config.get("DEFAULT_PAGE_OFFSET", 0))
