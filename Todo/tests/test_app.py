from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Tasks

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///todo.db",
            SECRET_KEY = 'TEST_SECRET',
            DEBUG = True,
            WTF_CSRF_ENABLED = False
            )
        return app
    
    def setUp(self):
        #There are no tables at this point
        db.create_all()

        #generic entry to test with
        todo = Tasks(name='Do Something')
        db.session.add(todo)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
#Specific test classes
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Do Something', response.data)
    
    def test_completed(self):
        task = Tasks.query.first()
        response = self.client.get(url_for('complete',ID=task.id))
        self.assertNotIn(b'Do Something', response.data)
    
    def test_delete(self):
        task = Tasks.query.first()
        response = self.client.get(url_for('delete', ID=task.id))
        self.assertNotIn(b'Do Something', response.data)
    
    def test_update(self):
        task = Tasks.query.first()
        new_task ="Do Something Else"
        response = self.client.post(url_for('update', ID=task.id), data = dict(task_name=new_task), follow_redirects=True)
        self.assertIn(b'Do Something Else', response.data)
    
    def test_incomplete(self):
        task = Tasks.query.first()
        task.completed = True
        response = self.client.get(url_for('incomplete', ID=task.id), follow_redirects= True)
        self.assertIn(b'Do Something', response.data)