from rply.token import BaseBox

class Data(BaseBox):
	def __init__(self, value):
		if value == "true":
			self.value = "True"
		elif value == "false":
			self.value = "False"
		elif value == "endl":
			self.value = r"'\n'"
		else:
			self.value = value
	def eval(self):
		return str(self.value)

class Concat():
	def __init__(self, left, right):
		self.value = f"{Data(left.value).eval()}, {Data(right.value).eval()}"
	def eval(self):
		return self.value