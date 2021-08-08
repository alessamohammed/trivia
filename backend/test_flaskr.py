import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question':'which country has the most reserve oil',
            'answer':'venezuela',
            'difficulty':'2',
            'category':'4'
        }
        self.new_search = {
            'searchTerm': 'country'
        }
        self.invalid_search = {
            'searchTerm': 'applejacks'
        }
        self.new_quiz = {
            'quiz_category': {
            'type': 'Science',
            'id': '1'
            
        }
        }
        self.invalid_quiz = {
            'quiz_category': {
            'type': 'horror',
            'id': '10000'
            
        }
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_retrieve_question_success(self):
        """test the retreving of all questions paginated"""
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    def test_retrieve_question_fail(self):
        """test beoynd valid page"""
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'resource not found')
    
    def test_delete_question_success(self):
        """test if a valid book is deleted"""
        res = self.client().delete('/questions/5')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
    
    def test_delete_question_fail(self):
        """test deleting invalid book"""
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
    
    def test_create_question_success(self):
        """test creating a new question"""
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['questions']))
    
    def test_create_question_fail(self):
        """test if question creating method is failed"""
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_search_question_success(self):
        """test if searching question by key word will return the required fields"""
        res = self.client().post('/questions', json=self.new_search)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(len(data['questions']),2)
        self.assertEqual(data['total_questions'],2)

    def test_search_question_fail(self):
        """test if searching question by invalid key word will return the required fields"""
        res = self.client().post('/questions', json=self.invalid_search)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(len(data['questions']),0)
        self.assertEqual(data['total_questions'],0)

    def test_retrieve_questions_categories_success(self):
        """test getting questions by categorie"""
        res = self.client().get('/categories/4/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(len(data['questions']),4)
        self.assertEqual(len(data['total_questions']), 4)
    
    def test_retrieve_questions_categories_fail(self):
        """test getting questions by invalid categorie"""
        res = self.client().get('/categories/99/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        #self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(len(data['questions']),0)
        self.assertEqual(len(data['total_questions']), 0)
    
    def test_post_quizzes_success(self):
        """test starting the quiz"""
        res = self.client().post('/quizzes', json=self.new_quiz)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['question'])
    
    def test_post_quizzes_fail(self):
        """test starting the quiz with invalid categorie"""
        res = self.client().post('/quizzes', json=self.invalid_quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()