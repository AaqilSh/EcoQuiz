import json

class QuestionService:
	def __init__(self, questions_file="questions.json"):
		self.questions_file = questions_file

	def load_questions(self):
		if not os.path.exists(self.questions_file):
			return []
		with open(self.questions_file, "r") as f:
			return json.load(f)