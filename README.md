# Full Stack API Final Project

All backend code follows PEP8 style guidelines.
## Getting started
### Pre-requisites and Local Development
Developers using this project should have python3,pip and node installed on their local machines

#### Backend
From the backend folder run ```pip install -r requirements.txt``` All required packages are included in the requirements file.

To run the application run the following commands:
```
cd backend
Set FLASK_APP=flaskr
Set FLASK_ENV=development
python -m flask run
```
These commands put the application in development. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. if running locally on linux look for commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).
The application on `https://127.0.0.1:5000/` by default and is a proxy in the frontend configuration.


#### Frontend
From the frontend folder, run the following commands to start the client:
```
npm install // only once to install dependencies
npm start
```

By default, the frontend will run on localhost:3000.

### Tests
In order to run tests navigate to the backend folder and run the following commands:

```
dropdb -U postgres trivia_test
createdb -U postgres trivia_test
psql -U postgres trivia_test < trivia.psql
python test_flaskr.py
```
The first time you run the tests, omit the dropdb command.
All tests are kept in that file and should be maintained as updates are made to app functionality.

## API Documentation

### Getting started

- Base url: At present this app can only be run locally and is not hosted as base URL
  the backend is hosted at "https://127.0.0.1:5000", which is set as a proxy in the 
  frontend configuration

- Authentication: not applicable

### Error Handling
Erros are returnd as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
#### Response codes
 - 404: resource not found
 - 422: unprocessable
 - 400: bad request
 - 405: method not allowed

### Endpoints

#### GET /categories
- General:
	- Returns a list of categories and success value
- Sample: curl http://127.0.0.1:5000/categories
```
{                         
  "categories": {         
    "1": "Science",       
    "2": "Art",           
    "3": "Geography",     
    "4": "History",       
    "5": "Entertainment", 
    "6": "Sports"         
  },                      
  "sucess": true          
}                         
```


#### GET /questions
- General:
	- Returns a list of question objects,categories, success value, and total number of questions
	- Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: curl http://127.0.0.1:5000/questions
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Tom Cruise", 
      "category": "5", 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "4", 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": "2", 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 19
}
```
#### POST /questions

- General:
	- Creates a new question using the submitted question, answer, difficulty, and category. Returns the id of the created question, success value, total questions, category and questions list based on current page number to update the frontend.
- Sample: curl http://127.0.0.1:5000/questions?page=3 -X POST -H \"Content-Type: application/json\" -d '{\"question\":\" What boxers original name is Cassius Clay?\", \"answer\":\"Muhammed Ali\",\"difficulty\":\"1\", \"category\":\"4\"}'
```
curl http://127.0.0.1:5000/questions?page=1 -X POST -H "Content-Type: application/json" -d "{\"question\":\" What boxers original name is Cassius Clay?\", \"answer\":\"Muhammed Ali\",\"difficulty\":\"1\", \"category\":\"4\"}"
{
  "created": 1,
  "questions": [
    {
      "answer": "Muhammed Ali",
      "category": "4",
      "difficulty": 1,
      "id": 35,
      "question": " What boxers original name is Cassius Clay?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```
#### DELETE /questions/{question_id}

- General:
	- Deletes the question of the given ID if it exists. returns the success value, and question list based on current page number to update the frontend.

- Sample: curl -X DELETE http://127.0.0.1:5000/questions/4?page=1

```
{
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": "4",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "2",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": "2",
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ],
  "success": true
}
```

#### GET /categories/{category_id}/questions
- General:
	- takes category id and returns list of questions, number of total questions, list of categories and success value
- Sample: curl http://127.0.0.1:5000/categories/2/questions

```
{                                                                                    
  "categories": {                                                                    
    "1": "Science",                                                                  
    "2": "Art",                                                                      
    "3": "Geography",                                                                
    "4": "History",                                                                  
    "5": "Entertainment",                                                            
    "6": "Sports"                                                                    
  },                                                                                 
  "questions": [                                                                     
    {                                                                                
      "answer": "Escher",                                                            
      "category": "2",                                                               
      "difficulty": 1,                                                               
      "id": 16,                                                                      
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of opti
cal illusions?"                                                                      
    },                                                                               
    {                                                                                
      "answer": "Mona Lisa",                                                         
      "category": "2",                                                               
      "difficulty": 3,                                                               
      "id": 17,                                                                      
      "question": "La Giaconda is better known as what?"                             
    },                                                                               
    {                                                                                
      "answer": "One",                                                               
      "category": "2",                                                               
      "difficulty": 4,                                                               
      "id": 18,                                                                      
      "question": "How many paintings did Van Gogh sell in his lifetime?"            
    },                                                                               
    {                                                                                
      "answer": "Jackson Pollock",                                                   
      "category": "2",                                                               
      "difficulty": 2,                                                               
      "id": 19,                                                                      
      "question": "Which American artist was a pioneer of Abstract Expressionism, and
 a leading exponent of action painting?"                                             
    }                                                                                
  ],                                                                                 
  "success": true,                                                                   
  "total_questions": [                                                               
    {                                                                                
      "answer": "Escher",                                                            
      "category": "2",                                                               
      "difficulty": 1,                                                               
      "id": 16,                                                                      
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of opti
cal illusions?"                                                                      
    },                                                                               
    {                                                                                
      "answer": "Mona Lisa",                                                         
      "category": "2",                                                               
      "difficulty": 3,                                                               
      "id": 17,                                                                      
      "question": "La Giaconda is better known as what?"                             
    },                                                                               
    {                                                                                
      "answer": "One",                                                               
      "category": "2",                                                               
      "difficulty": 4,                                                               
      "id": 18,                                                                      
      "question": "How many paintings did Van Gogh sell in his lifetime?"            
    },                                                                               
    {                                                                                
      "answer": "Jackson Pollock",                                                   
      "category": "2",                                                               
      "difficulty": 2,                                                               
      "id": 19,                                                                      
      "question": "Which American artist was a pioneer of Abstract Expressionism, and
 a leading exponent of action painting?"                                             
    }                                                                                
  ]                                                                                  
}                                                                                    
```
#### POST /quizzes

- General:
	- returns a random question and success value based on the selected categorie
- Sample: curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d "{\"quiz_category\": {\"type\": \"Science\", \"id\": \"1\"}}"
```
{                                                                                 
  "question": {                                                                   
    "answer": "Blood",                                                            
    "category": "1",                                                              
    "difficulty": 4,                                                              
    "id": 22,                                                                     
    "question": "Hematology is a branch of medicine involving the study of what?" 
  },                                                                              
  "success": true                                                                 
}                                                                                 
```
## Deployment N/A

## Authors
Yours truly, Mohammed Alessa

## Acknowledgements
The awesome team at udacity