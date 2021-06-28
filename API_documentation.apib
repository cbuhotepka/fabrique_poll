# Fabrique polls

Polls is a simple API allowing consumers to view polls and vote in them.

## All Questions Collection [/api/all_questions]

### List All Questions [GET]

Detailed question API contains all the possible answer_IDs and their text-interpretations

+ Response 200 (application/json)

        [
            {
                "id": 1,
                "name": "What is the answer to the Ultimate Question of Life, the Universe, and Everything",
                "description": "Try 42",
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
            }
        ]
        
## All the user's answers [/api/answers_of_user/{id}]
        
### List All Questions [GET]

Show a list of all the questions user answered with their answers

+ Response 200 (application/json)

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

+ Response 200 (application/json)

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

+ Response 200 (application/json)

        {"result": "ok"}
or
        ["Answer already exists"]
or
        ["There shouldn't be text answer in a single-answer question"]
