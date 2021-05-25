from marshmallow import fields, INCLUDE
from marshmallow.decorators import pre_load
from werkzeug.security import generate_password_hash, check_password_hash

from lore import ma

from lore.models.alias import Alias
from lore.models.campaign import Campaign
from lore.models.page import Page
from lore.models.paragraph import Paragraph
from lore.models.tag import Tag
from lore.models.user import User

class CampaignSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Campaign

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

class PageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Page

# class PageTreeChildNodeSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Page
#     page_id = ma.auto_field()
#     has_children = fields.Boolean()
#     _get_children = ma.URLFor('api.get_page_tree', values={'pk':'<page_id>', '_external':False})

# class PageTreeSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Page
#     page_id = ma.auto_field()
#     children = fields.List(fields.Nested(PageTreeChildNodeSchema))
#     has_children = fields.Boolean()
#     _get_children = ma.URLFor('api.get_page_tree', values={'pk':'<page_id>', '_external':False})

class ParagraphSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Paragraph

class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag

campaign_schema = CampaignSchema()#trict=True)
campaigns_schema = CampaignSchema(many=True)

user_schema = UserSchema()#trict=True)
users_schema = UserSchema(many=True)

alias_schema = AliasSchema()#trict=True)
aliases_schema = AliasSchema(many=True)

page_schema = PageSchema()#trict=True)
pages_schema = PageSchema(many=True)
# page_tree_schema = PageTreeSchema()

paragraph_schema = ParagraphSchema()#trict=True)
paragraphs_schema = ParagraphSchema(many=True)

tag_schema = TagSchema()#trict=True)
tags_schema = TagSchema(many=True)