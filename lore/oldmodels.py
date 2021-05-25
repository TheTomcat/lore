# from datetime import datetime 

# from flask import current_app
# from werkzeug.security import generate_password_hash, check_password_hash

# from lore import db

# page_tags = db.Table(
#     'page_tags',
#     db.Column('page_id', db.Integer, db.ForeignKey('pages.page_id'), primary_key=True),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tags.tag_id'), primary_key=True)
# )

# page_links = db.Table('page_links',
#     db.Column('page_from', db.Integer, db.ForeignKey('pages.page_id'), primary_key=True),
#     db.Column('page_to', db.Integer, db.ForeignKey('pages.page_id'), primary_key=True)
# )

# # group_membership = db.Table('group_membership',
# #     db.Column('group_id', db.Integer, db.ForeignKey('groups.group_id'), primary_key=True),
# #     db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
# # )

# campaign_membership = db.Table('campaign_membership',
#     db.Column('campaign_id', db.Integer, db.ForeignKey('campaigns.campaign_id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
# )

# class Campaign(db.Model):
#     __tablename__ = "campaigns"
#     campaign_id = db.Column(db.Integer, primary_key=True)
#     #campaign_public_id = db.Column()
#     stub = db.Column(db.String, unique=True, index=True, nullable=False)
#     name = db.Column(db.String)

#     created_on = db.Column(db.DateTime, default=datetime.utcnow)
#     root_node_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
#     root_node = db.relationship('Page', foreign_keys='Campaign.root_node_id', post_update=True)

#     owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     owner = db.relationship('User', back_populates="owned_campaigns")

#     members = db.relationship("User", secondary=campaign_membership, back_populates="campaigns")

#     # media = db.relationship("Media", back_populates="campaign")
#     # groups = db.relationship("Group", back_populates="campaign")
#     pages = db.relationship("Page", foreign_keys='Page.campaign_id', back_populates="campaign")
#     # aliases = db.relationship("Alias", back_populates="campaign")
#     tags = db.relationship("Tag", back_populates="campaign")
#     # tables = db.relationship("Table", back_populates="campaign")

#     @classmethod
#     def get(cls, stub):
#         return cls.query.filter_by(stub=stub).first()

#     def get_page_from_stub(self, stub):
#         return Page.query.filter_by(stub=stub, campaign=self).first()

#     def get_alias_from_stub(self, stub):
#         return Alias.query.filter_by(stub=stub, campaign=self).first()

#     def get_page_and_alias(self, stub):
#         # TODO: Implement a join here on aliases.page_id==pages.page_id,
#         # find where page_stub or alias is stub (and campaign)
#         page = Page.query.filter_by(stub=stub, campaign=self).first()
#         if page:
#             return page, None
#         alias = Alias.query.filter_by(stub=stub, campaign=self).first()
#         if alias:
#             return alias.page, alias
#         return None

#     def get_page_from_alias_or_stub(self, stub):
#         return self.get_page_from_stub(stub) or self.get_alias_from_stub(stub=stub).page

#     def page_exists(self, stub):
#         return Page.query.filter_by(stub=stub, campaign=self).count() + \
#             Alias.query.filter_by(stub=stub, campaign=self).count() > 0

#     def get_tag(self, tag_or_tagname):
#         if isinstance(tag_or_tagname, Tag): # This is a tag
#             if tag_or_tagname.campaign == self: # And it is from this campaign
#                 return tag_or_tagname
#             else:
#                 raise ValueError(f"Tag {tag_or_tagname.name} <{tag_or_tagname.tag_id}> not part of campaign {self.name}.")
#         return Tag.query.filter_by(tag_name=tag_or_tagname, campaign=self).first()

#     def __init__(self, name, stub, owner):
#         self.name = name
#         self.stub = stub
#         self.created_on = datetime.utcnow()
#         self.owner = owner
#         self.members.append(owner)
#         self.create_default_groups()
#         self.generate_root_node()

#     def generate_root_node(self, node_name="Index", stub="Index"):
#         n = Page(title=node_name, stub=stub, campaign=self)
#         n.edited(self.owner)
#         self.root_node = n
#         return n

#     def create_default_groups(self):
#         admin = Group(name="Admin", campaign=self)
#         admin.add_user(self.owner)
#         self.groups.append(admin)
#         return admin

#     def add_user(self, user):
#         if user not in self.members:
#             self.members.append(user)
#             return True
#         return False
#     def remove_user(self, user):
#         if user in self.members:
#             self.members.remove(user) # Remove the user 
#             for group in self.groups:
#                 group.remove_user(user) # And remove from all permission groups
#             return True 
#         return False

# class Page(db.Model):
#     """A page in the wiki.

#     Fields:
#         page_id    (int): The internal id of the page
#         stub    (string): The url-safe version of the page title, to be found at baseurl.com/lore/stub
#         shared_id  (str): TODO: A public url to access the page baseurl.com/.../shared_id
#         permalink  (str): TODO: The permalink to this page. Immutable. Can be null. Respects permissions.
#         title   (string): The title of the page
#         icon            : TODO: To be implemented
#         body_md (string): Markdown text representing the body of the page
#         parent    (Page): The parent page, for displaying in the nav-tree
#         depth      (int): The depth in the tree of the page, zero is root and children are +1 from their parents
#         edited_on (date): The date the page was edited
#         edited_by (User): The user who edited the page (not enforced)
#         tags     ([Tag]): A list of tags given to the page
#         links   ([Page]): TODO: Populate this. A list of pages that this page links to in its body
#         aliases([Alias]): Any alternate names that this page can be found under

#     """
#     __tablename__ = 'pages'
#     page_id = db.Column(db.Integer, primary_key=True)

#     public_id = db.Column(db.String, index=True, nullable=True)
#     permalink = db.Column(db.String, index=True, nullable=True)

#     title = db.Column(db.String, nullable=False)
#     stub = db.Column(db.String, index=True, nullable=False)
#     icon = db.Column(db.String)

#     paragraphs = db.relationship("Paragraph", back_populates="page")

#     # Tree structure
#     parent_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
#     parent = db.relationship('Page', remote_side=[page_id])
#     order = db.Column(db.Integer, default=0)
#     children = db.relationship('Page')
#     depth = db.Column(db.Integer, default=0)

#     tags = db.relationship('Tag', secondary=page_tags, back_populates='pages')

#     links = db.relationship('Page', secondary=page_links,
#                             primaryjoin=page_id == page_links.c.page_to,
#                             secondaryjoin=page_id == page_links.c.page_from,
#                             backref='links_to')

#     aliases = db.relationship('Alias', back_populates='page')

#     # view_group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
#     # view_group = db.relationship("Group", foreign_keys=[view_group_id], backref="view_pages")
#     # edit_group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
#     # edit_group = db.relationship("Group", foreign_keys=[edit_group_id], backref="edit_pages")
#     # owner_group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
#     # owner_group = db.relationship("Group", foreign_keys=[owner_group_id], backref="owner_pages")

#     campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'), nullable=False)
#     campaign = db.relationship("Campaign", foreign_keys='Page.campaign_id', back_populates="pages")

#     # @classmethod
#     # def get_by_stub(cls, page_stub, campaign_or_stub):
#     #     # TODO: Change this to search in a joined table
#     #     if isinstance(campaign_or_stub, str):
#     #         campaign_or_stub = Campaign.get(campaign_or_stub)
#     #     return cls.query.filter_by(stub=page_stub, campaign=campaign_or_stub).first()

#     # def generate_shared_id(self):
#     #     self.shared_id = secrets.token_urlsafe(32)
#     #     return self.shared_id
    
#     # def get_permalink(self):
#     #     if self.permalink:
#     #         return self.permalink
#     #     self.permalink = secrets.token_urlsafe(32)
#     #     return self.permalink

#     # @classmethod
#     # def get_by_shared_id(cls, shared_id):
#     #     return cls.query.filter_by(shared_id=shared_id).first()

#     # @classmethod
#     # def get_by_permalink(cls, permalink):
#     #     return cls.query.filter_by(permalink=permalink).first()

#     # def set_permission_group(self, *, view_group=None, edit_group=None, owner_group=None):
#     #     if view_group is not None:
#     #         self.view_group = view_group
#     #     if edit_group is not None:
#     #         self.edit_group = edit_group
#     #     # if owner_group is not None:
#     #     #     self.owner_group = owner_group

#     # def get_permissions(self, user):
#     #     return {'edit': user in self.edit_group,
#     #             'view': user in self.view_group,
#     #             # 'owner': user in self.owner_group,
#     #             'superuser': user == self.campaign.owner,
#     #             }

#     # def can_view(self, user):
#     #     return user in self.view_group or user == self.campaign.owner
#     # def can_edit(self, user):
#     #     return user in self.edit_group or user == self.campaign.owner

#     # def get_nav_dict(self, depth=0):
#     #     if self.children:
#     #         output = []
#     #         for child in sorted(self.children, key=lambda x: x.order):
#     #             d = {'name':child.title, 
#     #                  'id':child.stub}
#     #             if len(child.children) == 0:
#     #                 d['children'] = []
#     #             elif len(child.children) > 0 and depth==0:
#     #                 d['load_on_demand'] = True
#     #             elif len(child.children) > 0 and depth != 0:
#     #                 d['children'] = child.get_nav_dict(depth=depth-1)
#     #                 d['load_on_demand'] = True
#     #             output.append(d)
#     #         return output
#     #     return []

#     def edited(self, user=None):
#         "Sets the date and user who edited the page."
#         self.edited_on = datetime.utcnow()
#         if user:
#             self.edited_by = user
#         return self.edited_on

#     def set_parent(self, parent):
#         """Set the parent of this page (i.e., move the page), adjusting the depth accordingly.
#         If parent is not supplied, sets the root node as parent"""
#         if parent is None:
#             parent = self.campaign.root_node
#         self.parent = parent
#         self.depth = parent.depth + 1
#         return self.depth

#     @classmethod
#     def create_page_as_child(cls, parent, title="", stub=""):
#         "Create a child beneath this page"
#         p = cls(title=title, stub=stub, parent=parent, depth=parent.depth+1, campaign=parent.campaign)
#         return p

#     def create_alias(self, alias_stub):
#         "Create an alias for this page"
#         return Alias(stub=alias_stub, page=self, campaign=self.campaign)
    
#     # def remove_alias_from_stub(self, alias_stub):
#     #     alias = self.campaign.get_alias_from_stub(alias_stub)
#     #     self.remove_alias(alias)

#     # def remove_alias(self, alias): 
#     #     # This is the only method that calls db.session.something so maybe should be rewritten?
#     #     try:
#     #         self.aliases.remove(alias)
#     #         db.session.delete(alias)
#     #         return True
#     #     except ValueError:
#     #         return False

#     def link(self, other):
#         # TODO: IMPLEMENT THIS
#         self.links.append(other)
    
#     # def tag(self, tagname):
#     #     tag = self.campaign.get_tag(tagname)
#     #     if tag and tag not in self.tags:
#     #         self.tags.append(tag)
#     #         return True
#     #     return False

#     # def untag(self, tagname):
#     #     tag = self.campaign.get_tag(tagname)
#     #     if tag and tag in self.tags:
#     #         self.tags.remove(tag)
#     #         return True
#     #     return False

#     # def hastag(self, tagname):
#     #     for tag in self.tags:
#     #         if tag.tag_name == tagname:
#     #             return True
#     #     return False

# class Paragraph(db.Model):
#     ## https://docs.sqlalchemy.org/en/14/orm/extensions/hybrid.html
#     __tablename__ = 'paragraphs'
#     section_id = db.Column(db.Integer, primary_key=True)
    
#     page_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
#     page = db.relationship("Page", back_populates="paragraphs")

#     body = db.Column(db.String)
#     order = db.Column(db.Integer)
        
#     # Tracking changes
#     edited_by_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
#     edited_by = db.relationship('User', back_populates='paragraphs')
#     edited_on = db.Column(db.DateTime, default=datetime.utcnow)
#     edit_comment = db.Column(db.String, default="")

# class Alias(db.Model):
#     __tablename__ = 'aliases'
#     alias_id = db.Column(db.Integer, primary_key=True)
#     stub = db.Column(db.String, unique=True, nullable=False)
    
#     page_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
#     page = db.relationship('Page', back_populates='aliases')

#     campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'), nullable=False)
#     campaign = db.relationship("Campaign", back_populates="aliases")

# class Tag(db.Model):
#     __tablename__ = 'tags'
#     tag_id = db.Column(db.Integer, primary_key=True)
#     tag_name = db.Column(db.String, unique=True, nullable=False)

#     parent_tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'))
#     child_tag = db.relationship('Tag')
#     parent_tag = db.relationship('Tag', remote_side=[tag_id])

#     pages = db.relationship('Page', secondary=page_tags, back_populates='tags')

#     campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'), nullable=False)
#     campaign = db.relationship("Campaign", back_populates="tags")

#     @classmethod
#     def create_tag_as_child(cls, parent, child_tag_name):
#         # TODO: Check the tag does not already exist
#         return cls(tag_name=child_tag_name, parent_tag=parent)

#     @classmethod
#     def create(cls, tag_name, campaign):
#         return cls(tag_name=tag_name, campaign=campaign)

# class User(db.Model):
    # __tablename__ = 'users'
    # user_id = db.Column(db.Integer, primary_key=True)

    # username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    # password_hash = db.Column(db.String(128))

    # last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # paragraphs = db.relationship('Paragraph', back_populates='edited_by')

    # owned_campaigns = db.relationship('Campaign', back_populates='owner')

    # campaigns = db.relationship("Campaign", secondary=campaign_membership, back_populates="members")

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)