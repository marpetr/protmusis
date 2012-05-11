import threading

class State(object):
	def __init__(self):
		self.lock = threading.RLock()
		self.events = []
		self.state = 'idle'
		self.answer_set = {}
	
	def show_question(self, question, seconds):
		with self.lock:
			evt = {}
			if self.state != 'question_input':
				evt['type'] = 'QUESTION_INPUT'
			self.state = 'question_input'
			self.question_id = question.id
			
			
	
	def current_state(self):
		return {}
	
	def changeset(self, since):
		with self.lock:
			return self.events[since:]
	

state = State()

data_updated = threading.Condition()
