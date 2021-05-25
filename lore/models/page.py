from datetime import datetime
from lore import db, ma
from lore.models.alias import Alias
from lore.models.secondary import page_tags, page_links
from lore.models.paragraph import Paragraph

class Page(db.Model):
    """A page in the wiki.

    Fields:
        page_id    (int): The internal id of the page
        stub    (string): The url-safe version of the page title, to be found at baseurl.com/lore/stub
        shared_id  (str): TODO: A public url to access the page baseurl.com/.../shared_id
        permalink  (str): TODO: The permalink to this page. Immutable. Can be null. Respects permissions.
        title   (string): The title of the page
        icon            : TODO: To be implemented
        body_md (string): Markdown text representing the body of the page
        parent    (Page): The parent page, for displaying in the nav-tree
        depth      (int): The depth in the tree of the page, zero is root and children are +1 from their parents
        edited_on (date): The date the page was edited
        edited_by (User): The user who edited the page (not enforced)
        tags     ([Tag]): A list of tags given to the page
        links   ([Page]): TODO: Populate this. A list of pages that this page links to in its body
        aliases([Alias]): Any alternate names that this page can be found under

    """
    __tablename__ = 'pages'
    page_id = db.Column(db.Integer, primary_key=True)

    public_id = db.Column(db.String, index=True, nullable=True)
    permalink = db.Column(db.String, index=True, nullable=True)

    title = db.Column(db.String, nullable=False)
    stub = db.Column(db.String, index=True, nullable=False)
    icon = db.Column(db.String)

    paragraphs = db.relationship("Paragraph", back_populates="page")

    # Tree structure
    parent_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
    parent = db.relationship('Page', remote_side=[page_id])
    order = db.Column(db.Integer, default=0)
    children = db.relationship('Page')
    depth = db.Column(db.Integer, default=0)

    tags = db.relationship('Tag', secondary=page_tags, back_populates='pages')

    links = db.relationship('Page', secondary=page_links,
                            primaryjoin=page_id == page_links.c.page_to,
                            secondaryjoin=page_id == page_links.c.page_from,
                            backref='links_to')

    aliases = db.relationship('Alias', back_populates='page')

    # view_group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    # view_group = db.relationship("Group", foreign_keys=[view_group_id], backref="view_pages")
    # edit_group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    # edit_group = db.relationship("Group", foreign_keys=[edit_group_id], backref="edit_pages")
    # owner_group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    # owner_group = db.relationship("Group", foreign_keys=[owner_group_id], backref="owner_pages")

    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'), nullable=False)
    campaign = db.relationship("Campaign", foreign_keys='Page.campaign_id', back_populates="pages")

    # @classmethod
    # def get_by_stub(cls, page_stub, campaign_or_stub):
    #     # TODO: Change this to search in a joined table
    #     if isinstance(campaign_or_stub, str):
    #         campaign_or_stub = Campaign.get(campaign_or_stub)
    #     return cls.query.filter_by(stub=page_stub, campaign=campaign_or_stub).first()

    # def generate_shared_id(self):
    #     self.shared_id = secrets.token_urlsafe(32)
    #     return self.shared_id
    
    # def get_permalink(self):
    #     if self.permalink:
    #         return self.permalink
    #     self.permalink = secrets.token_urlsafe(32)
    #     return self.permalink

    # @classmethod
    # def get_by_shared_id(cls, shared_id):
    #     return cls.query.filter_by(shared_id=shared_id).first()

    # @classmethod
    # def get_by_permalink(cls, permalink):
    #     return cls.query.filter_by(permalink=permalink).first()

    # def set_permission_group(self, *, view_group=None, edit_group=None, owner_group=None):
    #     if view_group is not None:
    #         self.view_group = view_group
    #     if edit_group is not None:
    #         self.edit_group = edit_group
    #     # if owner_group is not None:
    #     #     self.owner_group = owner_group

    # def get_permissions(self, user):
    #     return {'edit': user in self.edit_group,
    #             'view': user in self.view_group,
    #             # 'owner': user in self.owner_group,
    #             'superuser': user == self.campaign.owner,
    #             }

    # def can_view(self, user):
    #     return user in self.view_group or user == self.campaign.owner
    # def can_edit(self, user):
    #     return user in self.edit_group or user == self.campaign.owner

    # def get_nav_dict(self, depth=0):
    #     if self.children:
    #         output = []
    #         for child in sorted(self.children, key=lambda x: x.order):
    #             d = {'name':child.title, 
    #                  'id':child.stub}
    #             if len(child.children) == 0:
    #                 d['children'] = []
    #             elif len(child.children) > 0 and depth==0:
    #                 d['load_on_demand'] = True
    #             elif len(child.children) > 0 and depth != 0:
    #                 d['children'] = child.get_nav_dict(depth=depth-1)
    #                 d['load_on_demand'] = True
    #             output.append(d)
    #         return output
    #     return []

    def edited(self, user=None):
        "Sets the date and user who edited the page."
        self.edited_on = datetime.utcnow()
        if user:
            self.edited_by = user
        return self.edited_on

    def set_parent(self, parent):
        """Set the parent of this page (i.e., move the page), adjusting the depth accordingly.
        If parent is not supplied, sets the root node as parent"""
        if parent is None:
            parent = self.campaign.root_node
        self.parent = parent
        self.depth = parent.depth + 1
        return self.depth

    @classmethod
    def create_page_as_child(cls, parent, title="", stub=""):
        "Create a child beneath this page"
        p = cls(title=title, stub=stub, parent=parent, depth=parent.depth+1, campaign=parent.campaign)
        return p

    def create_alias(self, alias_stub):
        "Create an alias for this page"
        return Alias(stub=alias_stub, page=self, campaign=self.campaign)
    
    def create_paragraph(self, title="", body=""):
        order = max([i.order for i in self.paragraphs])
        pp = Paragraph(title=title, body=body, order=order+1, page=self)
    
    def normalise_paragraph_order(self):
        for i, paragraph in enumerate(self.paragraphs):
            paragraph.order = i

    @property
    def has_children(self):
        return len(self.children) > 0

    # def as_tree(self, return_children=True):
    #     return {
    #     'page_id': self.page_id,
    #     'children':[i.as_tree(False) for i in self.children] if return_children else [], 
    #     'has_children': len(self.children) > 0,
    #     'get_children': ma.URLFor('api.get_page_tree', values={'pk':'<page_id>','_external':False})
    #     }
           
    # def remove_alias_from_stub(self, alias_stub):
    #     alias = self.campaign.get_alias_from_stub(alias_stub)
    #     self.remove_alias(alias)

    # def remove_alias(self, alias): 
    #     # This is the only method that calls db.session.something so maybe should be rewritten?
    #     try:
    #         self.aliases.remove(alias)
    #         db.session.delete(alias)
    #         return True
    #     except ValueError:
    #         return False

    def link(self, other):
        # TODO: IMPLEMENT THIS
        self.links.append(other)
    
    # def tag(self, tagname):
    #     tag = self.campaign.get_tag(tagname)
    #     if tag and tag not in self.tags:
    #         self.tags.append(tag)
    #         return True
    #     return False

    # def untag(self, tagname):
    #     tag = self.campaign.get_tag(tagname)
    #     if tag and tag in self.tags:
    #         self.tags.remove(tag)
    #         return True
    #     return False

    # def hastag(self, tagname):
    #     for tag in self.tags:
    #         if tag.tag_name == tagname:
    #             return True
    #     return False
