from datetime import datetime

from lore import db, ma 
from lore.models.page import Page
from lore.models.alias import Alias
from lore.models.tag import Tag
from lore.models.secondary import campaign_membership


class Campaign(db.Model):
    __tablename__ = "campaigns"
    campaign_id = db.Column(db.Integer, primary_key=True)
    stub = db.Column(db.String, unique=True, index=True, nullable=False)
    name = db.Column(db.String)

    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    root_node_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
    root_node = db.relationship('Page', foreign_keys='Campaign.root_node_id', post_update=True)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    owner = db.relationship('User', back_populates="owned_campaigns")

    members = db.relationship("User", secondary=campaign_membership, back_populates="campaigns")

    pages = db.relationship("Page", foreign_keys='Page.campaign_id', back_populates="campaign")
    # aliases = db.relationship("Alias", back_populates="campaign")
    tags = db.relationship("Tag", back_populates="campaign")


    # media = db.relationship("Media", back_populates="campaign")
    # groups = db.relationship("Group", back_populates="campaign")
    # tables = db.relationship("Table", back_populates="campaign")

    # @classmethod
    # def get(cls, stub):
    #     return cls.query.filter_by(stub=stub).first()

    # def get_page_from_stub(self, stub):
    #     return Page.query.filter_by(stub=stub, campaign=self).first()

    # def get_alias_from_stub(self, stub):
    #     return Alias.query.filter_by(stub=stub, campaign=self).first()

    # def get_page_and_alias(self, stub):
    #     # TODO: Implement a join here on aliases.page_id==pages.page_id,
    #     # find where page_stub or alias is stub (and campaign)
    #     page = Page.query.filter_by(stub=stub, campaign=self).first()
    #     if page:
    #         return page, None
    #     alias = Alias.query.filter_by(stub=stub, campaign=self).first()
    #     if alias:
    #         return alias.page, alias
    #     return None

    # def get_page_from_alias_or_stub(self, stub):
    #     return self.get_page_from_stub(stub) or self.get_alias_from_stub(stub=stub).page

    # def page_exists(self, stub):
    #     return Page.query.filter_by(stub=stub, campaign=self).count() + \
    #         Alias.query.filter_by(stub=stub, campaign=self).count() > 0

    # def get_tag(self, tag_or_tagname):
    #     if isinstance(tag_or_tagname, Tag): # This is a tag
    #         if tag_or_tagname.campaign == self: # And it is from this campaign
    #             return tag_or_tagname
    #         else:
    #             raise ValueError(f"Tag {tag_or_tagname.name} <{tag_or_tagname.tag_id}> not part of campaign {self.name}.")
    #     return Tag.query.filter_by(tag_name=tag_or_tagname, campaign=self).first()

    def __init__(self, name, stub, owner):
        self.name = name
        self.stub = stub
        self.created_on = datetime.utcnow()
        self.owner = owner
        self.members.append(owner)
        # self.create_default_groups()
        self.generate_root_node()

    def generate_root_node(self, node_name="Index", stub="Index"):
        n = Page(title=node_name, stub=stub, campaign=self)
        n.edited(self.owner)
        self.root_node = n
        return n

    # def create_default_groups(self):
    #     admin = Group(name="Admin", campaign=self)
    #     admin.add_user(self.owner)
    #     self.groups.append(admin)
    #     return admin

    def add_user(self, user):
        if user not in self.members:
            self.members.append(user)
            return True
        return False
    def remove_user(self, user):
        if user in self.members:
            self.members.remove(user) # Remove the user 
            # for group in self.groups:
            #     group.remove_user(user) # And remove from all permission groups
            return True 
        return False

