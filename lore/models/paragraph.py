from datetime import datetime

from lore import db

class Paragraph(db.Model):
    ## https://docs.sqlalchemy.org/en/14/orm/extensions/hybrid.html
    __tablename__ = 'paragraphs'
    section_id = db.Column(db.Integer, primary_key=True)
    
    page_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
    page = db.relationship("Page", back_populates="paragraphs")

    title = db.Column(db.String)
    body = db.Column(db.String)
    order = db.Column(db.Integer)
        
    # Tracking changes
    edited_by_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    edited_by = db.relationship('User', back_populates='paragraphs')
    edited_on = db.Column(db.DateTime, default=datetime.utcnow)
    edit_comment = db.Column(db.String, default="")

    @property
    def campaign_id(self):
        return self.page.campaign_id
