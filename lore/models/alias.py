from lore import db

class Alias(db.Model):
    __tablename__ = 'aliases'
    alias_id = db.Column(db.Integer, primary_key=True)
    stub = db.Column(db.String, unique=True, nullable=False)
    
    page_id = db.Column(db.Integer, db.ForeignKey('pages.page_id'))
    page = db.relationship('Page', back_populates='aliases')

    @property
    def campaign_id(self):
        return self.page.campaign_id

    #campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'), nullable=False)
    #campaign = db.relationship("Campaign", back_populates="aliases")
