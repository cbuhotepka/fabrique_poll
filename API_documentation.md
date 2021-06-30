# Fabrique polls

Polls is a simple API allowing consumers to view polls and vote in them.

## All Questions Collection [/api/all_questions]

### List All Questions [GET]

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

## Detailed question [/api/question_detail/{id}]

### Details of one question [GET]

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
        
## Question Update/Delete [/api/question_detail/{id}]

### Details of one question [PUT/DELETE]

Update or Delete question API by {id}
Each answer requires either:
- "id" - Add existing answer to this question
- "answer" - Create new answer with the text given
- both - Alter the existing answer

+ Response (application/json)

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
        
## Question Create [/api/question_create]

### Details of one question [POST]

Create new Question

+ Response (application/json)

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
        

## Detailed poll [/api/poll_detail/{id}]

### Details of one question [GET]

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
        
## Question Update/Delete [/api/question_detail/{id}]

### Details of one question [PUT/DELETE]

Update or Delete question API by {id}
Each answer requires either:
- "id" - Add existing answer to this question
- "answer" - Create new answer with the text given
- both - Alter the existing answer

+ Response (application/json)

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
        
## Question Create [/api/question_create]

### Details of one question [POST]

Create new Question

+ Response (application/json)

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

## All the user's answers [/api/answers_of_user/{id}]
        
### List All Questions [GET]

Show a list of all the questions user answered with their answers

+ Response (application/json)

        [
            {
                "user_id": 1,
                "question_id": 1,
                "answers": [
                    3
                ],
                "text_answer": ""
            }
        ]
        
## All the user's answers [/api/available_questions]
        
### Available questions [GET]

Show list of the questions available for the current user 

+ Response (application/json)

        [
            {
                "id": 2,
                "name": "What was the question?",
                "description": "",
                "type": "text",
                "start_date": "2021-06-28",
                "end_date": "2021-08-26",
                "answers": []
            }
        ]
        
## All the user's previous answers [/api/my_answers]
        
### Available questions [GET]

Show detailed list of current user's answered questions

+ Response 200 (application/json)

        [
            {
                "user_id": 1,
                "question": {
                    "id": 1,
                    "name": "What is the answer to the Ultimate Question of Life, the Universe, and Everything",
                    "description": "",
                    "type": "single",
                    "start_date": "2021-06-28",
                    "end_date": "2021-07-30",
                    "answers": [
                        {
                            "id": 1,
                            "answer": "Nothing"
                        },
                        {
                            "id": 2,
                            "answer": "Everything"
                        },
                        {
                            "id": 3,
                            "answer": "42"
                        }
                    ]
                },
                "answers": [
                    {
                        "id": 3,
                        "answer": "42"
                    }
                ],
                "text_answer": ""
            }
        ]

## Answer the question [/api/answer]

### Answer the question [POST]

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
