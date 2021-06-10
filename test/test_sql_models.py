import unittest

from flask import Flask
from flask_testing import TestCase

from lore import create_app, db
from lore.config import TestConfig
from lore.models.user import User
from lore.models.campaign import Campaign
# https://stackoverflow.com/questions/52742657/flask-application-factory-testing

class LoreTestCase(TestCase):
    def create_app(self):
        app = create_app(config_class=TestConfig)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class UserModelTest(LoreTestCase):
    def test_add_a_user(self):
        "Test adding a user"
        u = User(username="test", email="test@test.com")
        u.set_password("verystrong")
        db.session.add(u)
        db.session.commit()
        u1 = User.query.first()
        self.assertEqual(u, u1)

    def test_unique_params_for_user(self):
        "Test that unique parameters are enforced"
        u = User(username="test",email="test@test.com")
        same_username = User(username="test",email="test1@test.com")
        same_email = User(username="test1",email="test@test.com")
        db.session.add(u)
        db.session.commit()
        db.session.add(same_username)
        self.assertRaises(Exception, db.session.commit)
        db.session.rollback()
        db.session.add(same_email)
        self.assertRaises(Exception, db.session.commit)
        
    def test_password_equality(self):
        "Test that password matching works"
        u = User(username="test", email="test@test.com")
        u.set_password('verystrong')
        self.assertTrue(u.check_password('verystrong'))
        self.assertFalse(u.check_password('asdfasdf'))
    
class CampaignModelTest(LoreTestCase):
    def test_create_campaign(self):
        "Test that campaign adding works"
        u = User(username="test",email="test@test.com")
        u.set_password("verystrong")
        c = Campaign(name="testcampaign",stub="testcampaign",owner=u)
        db.session.add(u)
        db.session.add(c)
        db.session.commit()
        c1 = Campaign.query.first()
        self.assertEqual(c, c1)
    def test_campaign_stub_uniqueness(self):
        "Test that stub uniqueness is enforced"
        u = User(username="test",email="test@test.com")
        u.set_password("verystrong")
        c = Campaign(name="testcampaign",stub="testcampaign",owner=u)
        d = Campaign(name="testcampaign2", stub="testcampaign", owner=u)
        db.session.add(u)
        db.session.add_all((c,d))
        self.assertRaises(Exception,db.session.commit)

    def test_get_by_stub(self):
        pass
    def test_get_by_uid(self):
        pass
    def test_campaign_root_node(self):
        pass
    def test_user_campaign_membership(self):
        pass
    def test_change_campaign_ownership(self):
        "Test that you can't delete the owner of a campaign"
        u = User(username="test",email="test@test.com")
        u.set_password("verystrong")
        c = Campaign(name="testcampaign",stub="testcampaign",owner=u)
        db.session.add_all((u, c))
        db.session.commit()
        u2 = User(username="test2", email="asdfas@aasdf.com")
        db.session.add(u2)
        c.change_ownership(u2)
        db.session.commit()
        self.assertEqual(u2.owned_campaigns[0], c)
        self.assertEqual(c.owner, u2)        
    
    def test_delete_owner(self):
        "Test that you can't delete the owner of a campaign"
        u = User(username="test",email="test@test.com")
        u.set_password("verystrong")
        c = Campaign(name="testcampaign",stub="testcampaign",owner=u)
        db.session.add_all((u, c))
        db.session.commit()
        self.assertRaises(ValueError, c.remove_user, u)


class PageModelTest(LoreTestCase):
    def test_create_page(self):
        pass
    def test_page_stub_uniqueness(self):
        pass
    def test_page_tree_structure(self):
        pass
    

# REM Create some users
# http -b post http://127.0.0.1:5000/user username=testus2er email=test2user1@test.com password=verystrong
# http -b get http://127.0.0.1:5000/user


# user = {'username':'',
#         'email':'',
#         'password':''}

# # Create a user
# Get the user id we just created
# Modify the email address
# Change the password
# Login the user

# Create a new campaign
# - required: name, user, 