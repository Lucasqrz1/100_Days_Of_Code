from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


#Creating the question bank
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

#Asking the questions
#Checking if the answer was correct
#Checking if we're the end of the quiz


