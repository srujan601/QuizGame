# Quiz Application

This project is a simple True/False quiz application written in Python. It presents users with a series of questions, allows them to input their answers, and tracks their score.

## Project Structure

- **`question_model.py`**: Defines the `Question` class which models a question with its text and answer.
- **`quiz_brain.py`**: Contains the `QuizBrain` class that handles the logic of the quiz, including:
  - Checking if there are still questions left (`still_has_question` method).
  - Presenting the next question to the user (`nextQuestion` method).
  - Checking the user's answer and updating the score (`check_answer` method).
- **`data.py`**: Contains the list of question data (question text and correct answers).
- **`main.py`**: The main file that runs the quiz game. It imports the `Question`, `QuizBrain` classes and `question_data`, then creates a quiz from the questions.

## Files

- **`question_model.py`**

```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
