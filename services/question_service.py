import json
import os

class QuestionService:
	def __init__(self, questions_file="questions.json"):
		self.questions_file = questions_file

	def load_questions(self):
		if not os.path.exists(self.questions_file):
			return []
		with open(self.questions_file, "r") as f:
			return json.load(f)
		
	def save_questions(self, questions):
		with open(self.questions_file, "w") as f:
			json.dump(questions, f, indent=2)

	def get_question_by_difficulty(self, difficulty):
		questions = self.load_questions()
		filtered = [q for q in questions if q["difficulty"] == difficulty]
		return filtered
	
	def update_difficulty(self, is_correct, current_difficulty):	
		difficulty_levels = ["easy", "medium", "hard"]
		current_index = difficulty_levels.index(current_difficulty)

		if is_correct:
			if current_index < len(difficulty_levels) - 1:
				return difficulty_levels[current_index + 1]
		else:
			if current_index > 0:
				return difficulty_levels[current_index - 1]
		
		return current_difficulty