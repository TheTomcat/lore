from datetime import datetime

from lore import db

class Paragraph(db.Model):
    ## https://docs.sqlalchemy.org/en/14/orm/extensions/hybrid.html
    __tablename__ = 'paragraphs'
    paragraph_id = db.Column(db.Integer, primary_key=True)
    
    page_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
    page = db.relationship("Page", back_populates="paragraphs")

    title = db.Column(db.String)
    body = db.Column(db.String)
    order = db.Column(db.Integer)
    style = db.Column(db.String)
        
    # Tracking changes
    edited_by_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    edited_by = db.relationship('User', back_populates='paragraphs')
    edited_on = db.Column(db.DateTime, default=datetime.utcnow)
    edit_comment = db.Column(db.String, default="")

    @property
    def campaign_id(self):
        return self.page.campaign_id
    
    @classmethod
    def get(cls, page_id):
        return cls.query.filter_by(page_id=page_id).first()
    
    def update(self, body, user):
        self.body = body
        self.edited_on = datetime.utcnow()
        self.edited_by_id = user

    def can(self, user, permission):
        return self.page.can(user, permission)