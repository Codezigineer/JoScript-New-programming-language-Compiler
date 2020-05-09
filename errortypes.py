class LinkerError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Linker Error: " + self.ErrorMsg);

class SyntaxError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Syntax Error: " + self.ErrorMsg);

class DuplicateError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Duplicate Error: " + self.ErrorMsg);

class MissingParenthisisError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Missing Parenthasis Error: " + self.ErrorMsg);

class IncorrectValueError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Incorrect Value Error: " + self.ErrorMsg);

class 