from flask import url_for
from flask_testing import TestCase

from app import app, db, Register

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        #Pass in testing configuration
        app.config.update(SQLALchemy_DATABASE_URI = "sqlite:///test.db",
            SECRET_KEY = 'TEST_SECRET',
            DEBUG = True,
            WTF_CSRF_ENABLED = False
            )
        return app
    
    def setUp(self):
        # Will be called before every test
        # Create table
        db.create_all()

        #Create test registree
        sample1 = Register(name='MissWoman')

        # save users to database
        db.session.add(sample1)
        db.session.commit()
    
    def tearDown(self):
        #Will be called after every test

        db.session.remove()
        db.drop_all()

#Test class for testing that homepage loads
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_home_result(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'MissWoman', response.data)
    
# Test adding
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(url_for('home'), data = dict(name='MrMan'),follow_redirects=True)
        self.assertIn(b'MrMan',response.data)