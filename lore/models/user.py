from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from lore import db
from lore.models.secondary import campaign_membership

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    is_activated = db.Column(db.Boolean, default=False)

    paragraphs = db.relationship('Paragraph', back_populates='edited_by')
    owned_campaigns = db.relationship('Campaign', back_populates='owner')
    campaigns = db.relationship("Campaign", secondary=campaign_membership, back_populates="members")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def delete(self):
        self.is_active = False

    @classmethod
    def create_dummy_data(cls):
        users = ["Aaron Aaronsson",
                 "Belinda Baghurst",
                 "Charlie Chapman",
                 "Dorothy Dolittle",
                 "Ebinezer Egghurst",
                 "Frances Ferdinand",
                 "Gary Gygax",
                 "Heather Hobson",
                 "Irwin Ipping",
                 "Jolene Jameson"]
        for user in users:
            lcase = user.replace(" ","").lower()
            u = cls(username = lcase,
                    email = f'{lcase}@test.com',
                    is_active=True)
            u.set_password('verystrong')
            yield u
