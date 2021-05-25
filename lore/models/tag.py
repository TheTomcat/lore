from lore import db
from lore.models.secondary import page_tags

class Tag(db.Model):
    __tablename__ = 'tags'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String, unique=True, nullable=False)

    parent_tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'))
    child_tag = db.relationship('Tag')
    parent_tag = db.relationship('Tag', remote_side=[tag_id])

    pages = db.relationship('Page', secondary=page_tags, back_populates='tags')

    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'), nullable=False)
    campaign = db.relationship("Campaign", back_populates="tags")

    @classmethod
    def create_tag_as_child(cls, parent, child_tag_name):
        # TODO: Check the tag does not already exist
        return cls(tag_name=child_tag_name, parent_tag=parent)

    @classmethod
    def create(cls, tag_name, campaign):
        return cls(tag_name=tag_name, campaign=campaign)
