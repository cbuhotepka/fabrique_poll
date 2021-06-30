# Fabrique polls

Polls is a simple API allowing consumers to view polls and vote in them.

## Questions API

### List All Questions [/api/all_questions] [GET]

Detailed questions API contains all the possible answer_IDs and their text-interpretations

+ Response (application/json)

        [
            {
                "id": 1,
                "question": "What is the answer to the Universe?",
                "type": "single",
                "answers": [
                    {
                        "id": 7,
                        "answer": "Nothing else"
                    },
                    {
                        "id": 8,
                        "answer": "Everything else"
                    },
                    {
                        "id": 9,
                        "answer": "42"
                    }
                ],
                "poll": 1
            }
        ]

### Detailed question [/api/question_detail/{id}] [GET]

Detailed question API by {id} contains all the possible answer_IDs and their text-interpretations

+ Response (application/json)

        {
            "id": 1,
            "question": "What is the answer to the Universe?",
            "type": "single",
            "answers": [
                {
                    "id": 7,
                    "answer": "Nothing else"
                },
                {
                    "id": 8,
                    "answer": "Everything else"
                },
                {
                    "id": 9,
                    "answer": "42"
                }
            ],
            "poll": 1
        }

### Question Update/Delete [/api/question_detail/{id}] [PUT/DELETE]

Update or Delete question API by {id}
Each answer requires either:
- "id" - Add existing answer to this question
- "answer" - Create new answer with the text given
- both - Alter the existing answer

+ Request (application/json)

        {
            "question": "What is the answer to the Universe?",
            "type": "single",
            "answers": [
                {
                    "id": 7
                },
                {
                    "answer": "Everything else"
                },
                {
                    "id": 9,
                    "answer": "42"
                }
            ],
            "poll": 1
        }

### Question Create [/api/question_create] [POST]

Create new Question

+ Request (application/json)

        {
            "question": "What is the answer to the Universe?",
            "type": "single",
            "answers": [
                {
                    "id": 7
                },
                {
                    "answer": "Everything else"
                },
                {
                    "id": 9,
                    "answer": "42"
                }
            ],
            "poll": 1
        }
        
## Polls API

### Detailed poll [/api/poll_detail/{id}] [GET]

Detailed poll API by {id} with all of the questions

+ Response (application/json)

        {
            "id": 1,
            "name": "New Poll",
            "description": "Description",
            "start_date": "2021-06-29",
            "end_date": "2021-08-13",
            "questions": [
                {
                    "id": 1,
                    "question": "What is the answer to the Universe?",
                    "type": "single",
                    "answers": [
                        {
                            "id": 7,
                            "answer": "Nothing else"
                        },
                        {
                            "id": 8,
                            "answer": "Everything else"
                        },
                        {
                            "id": 9,
                            "answer": "42"
                        }
                    ],
                    "poll": 1
                },
                {
                    "id": 2,
                    "question": "What was the question?",
                    "type": "text",
                    "answers": [],
                    "poll": 1
                }
            ]
        }

### Poll Update/Delete [/api/question_detail/{id}] [PUT/DELETE]

Update or Delete Poll API by {id}
Contains IDs of its questions

+ Request (application/json)

        {
            "name": "New Poll",
            "description": "Description",
            "end_date": "2021-08-13",
            "questions": [
                1,
                2
            ]
        }

### Poll Create [/api/poll_create] [POST]

Create new Poll
"start_date" created automatically

+ Response (application/json)

        {
            "name": "New Poll",
            "description": "Description",
            "end_date": "2021-08-13",
            "questions": [
                1,
                2
            ]
        }
        
### All the current user's previous answers [/api/my_answers] [GET]

Show a list of all Polls with current user's answered questions

+ Response 200 (application/json)

        [
            {
                "id": 3,
                "name": "Third try Poll",
                "description": "Description",
                "questions": [
                    {
                        "question": "Yet another question",
                        "answer": [
                            {
                                "choice_answers": [
                                    "Nothing else",
                                    "42"
                                ],
                                "text_answer": ""
                            }
                        ]
                    }
                ]
            }
        ]
        
### All the user's answers [/api/answers_of_user/{id}] [GET]

Show a list of all Polls with user's {id} answered questions

+ Response 200 (application/json)

        [
            {
                "id": 1,
                "name": "New Poll",
                "description": "Description",
                "questions": [
                    {
                        "question": "What is the answer to the Universe?",
                        "answer": []
                    },
                    {
                        "question": "What was the question?",
                        "answer": [
                            {
                                "choice_answers": [],
                                "text_answer": "Dont know"
                            }
                        ]
                    }
                ]
            }
        ]
        
### Available questions [/api/available_polls] [GET]

Show a list of all the Polls available for the current User

+ Response 200 (application/json)

        [
            {
                "id": 1,
                "name": "New Poll",
                "description": "Description",
                "questions": [
                    {
                        "question": "What is the answer to the Universe?"
                    },
                    {
                        "question": "What was the question?"
                    }
                ]
            }
        ]

## Answer 
        
### Answer the question [api/answer] [POST]

Create the answer {answers/text_answer} on the question {question_id} from user {user_id}
If user_id is not provided, create the answer of the current user by their session_key.
Raises an error if provided with the answer type unconsistent with the question type; if provided with both "answers" and "text_answer"; or if the answer already exists.

+ Request (application/json)

        {
            "user_id": 1,
            "question_id": 1,
            "answers": [3]
        }
        
        or
        
        {
            "question_id": 1,
            "text_answer": "I'm fine"
        }

+ Response (application/json)

        {"result": "ok"}
        
        or
        
        ["Answer already exists"]
        
        or
        
        ["There shouldn't be text answer in a single-answer question"]
     
