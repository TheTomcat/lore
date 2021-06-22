from marshmallow import fields, INCLUDE
from marshmallow.exceptions import ValidationError
from werkzeug.security import generate_password_hash

from lore import ma
from lore.stub.stub import validate_stub, StubError, HashError

from lore.models.alias import Alias
from lore.models.campaign import Campaign
from lore.models.page import Page
from lore.models.paragraph import Paragraph
from lore.models.tag import Tag
from lore.models.user import User

class StubField(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return validate_stub(value)
        except StubError as e:
            raise ValidationError("Invalid stub") from e

class UID(fields.Field):
    def __init__(self, hasher=None, *args, **kwargs):
        self._hasher=hasher
        super().__init__(*args, **kwargs)
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return self._hasher.decode(value)[0]
        except HashError as e:
            raise IndexError("Hash error") from e
    def _serialize(self, value, attr, obj, **kwargs):
        try:
            return self._hasher.encode(value)
        except HashError as e:
            raise IndexError("Hash error") from e

class CampaignSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Campaign
    stub = StubField()
    uid = fields.String()
    # campaign_id = UID(hasher=Campaign._hasher)

class Password(fields.Field):
    def _deserialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return generate_password_hash(value)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        load_only = ['password_hash']
        model = User
        unknown=INCLUDE
    password_hash = Password(data_key='password')
    _links = ma.Hyperlinks({
        'self':ma.URLFor('api.get_user', values={'pk':'<user_id>', '_external':False})
    })
    # campaign=ma.URLFor('api.get_campaign', values={'pk':'<campaign_id>', 'external':False})

class AliasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Alias

class ParagraphSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Paragraph
    # paragraph_id = UID()
    _links = ma.Hyperlinks({
        'self':ma.URLFor('api.get_paragraph', values={'pk':'<paragraph_id>', '_external':False})
    })

class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag

class PageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Page
    # page_id = UID()
    _links = ma.Hyperlinks({
        'self':ma.URLFor('api.get_page', values={'pk':'<page_id>', '_external':False})
    })
    stub = StubField()
    paragraphs = fields.Nested(ParagraphSchema, many=True, only=('paragraph_id', 'order', 'title'))
    children = fields.Nested(lambda: PageSchema(only=('page_id','title','stub')))
    parent = fields.Nested(lambda: PageSchema(only=('page_id','title','stub'))) 

class PageParagraphSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Page
    # page_id = UID()
    paragraphs = fields.Nested(ParagraphSchema, many=True)
    stub = StubField()
    children = fields.Nested(lambda: PageSchema(only=('page_id','title','stub')))
    parent = fields.Nested(lambda: PageSchema(only=('page_id','title','stub'))) 

campaign_schema = CampaignSchema()
campaigns_schema = CampaignSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

alias_schema = AliasSchema()
aliases_schema = AliasSchema(many=True)

page_schema = PageParagraphSchema()
pages_schema = PageSchema(many=True)

paragraph_schema = ParagraphSchema()
paragraphs_schema = ParagraphSchema(many=True)

tag_schema = TagSchema()
tags_schema = TagSchema(many=True)