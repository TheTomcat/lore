# import os
# import unittest

# from config import basedir
# from lore import create_app, db


# class TestCase(unittest.TestCase):
#     def setUp(self):
#         app = create_app()
#         app.config['TESTING']=True
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
#         self.app = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
    
#     def test_