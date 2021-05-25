from lore import db

page_tags = db.Table(
    'page_tags',
    db.Column('page_id', db.Integer, db.ForeignKey('pages.page_id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.tag_id'), primary_key=True)
)

page_links = db.Table('page_links',
    db.Column('page_from', db.Integer, db.ForeignKey('pages.page_id'), primary_key=True),
    db.Column('page_to', db.Integer, db.ForeignKey('pages.page_id'), primary_key=True)
)

# group_membership = db.Table('group_membership',
#     db.Column('group_id', db.Integer, db.ForeignKey('groups.group_id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
# )

campaign_membership = db.Table('campaign_membership',
    db.Column('campaign_id', db.Integer, db.ForeignKey('campaigns.campaign_id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
)