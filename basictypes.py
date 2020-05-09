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

class ImportModuleError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Import/Module Error: " + self.ErrorMsg);

class IndexOutOfRangeError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Index Out Of Range Error: " + self.ErrorMsg);

class UnterminatedStringError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Unterminated String Error: " + self.ErrorMsg);

class UnterminatedBlockError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Unterminated Block Error: " + self.ErrorMsg);

class UnknownBoolError:
	def __init__(self, errorMsg):
		self.ErrorMsg = errorMsg;
		print("Boolean error: " + self.ErrorMsg);

# More Errors Coming Soon...

class Type:
	def __init__(self, args, kkwargs):
		return self;

class Object(Type):
	def __init__(self):
		return self;

class File(Object, Type):
	def __init__(self, filePath):
		return open(filePath)
	
	def read(filePath):
		return open(filePath, 'r');
	
	def write(filePath, whatToWrite):
		return open(filePath, 'w').write(whatToWrite);
	
	def append(filePath, whatToApppend):
		return open(filePath, 'a').write(whatToApppend);
	
	def create(filePath):
		return open(filePath, 'x');
	


class Module:
	def __init__(self, moduleName=str, moduleFilesPath=[str], linkerPath=str, modulePath=str, moduleIsSingleFile=bool):
		linker = open(linkerPath, 'r');
		linker.link = [[modulePath, open()]]
		self.module = open(modulePath);
		self.linker = linker;
		self.modulename = moduleName;
		while moduleFilesPath == [str]:
			self.module = [open(moduleFilesPath[range(999999999999999999999999999999999999999999999999999999999999999999)]), 'r']

class Bool:
	def __init__(self, boolvalue=str):

		self.true = 1;
		self.false = 0;

		if( boolvalue == "true" ):
			return self.true;
		
		if( boolvalue == "true" ):
			return self.false;
		
		if( boolvalue != "true" and boolvalue != "false" ):
			return UnknownBoolError("Not a Valid Boolean.");

class Void:
	def __init__(self):
		return;

class Class(Type):
	def __init__(self):
		return 0;

class Struct(Type):
	def __init__(self):
		return 1;

class Enum(Type):
	def __init__(self, enumvalues=list):
		return enumvalues;

class TypeAlias:
	def __init__(self, original=Type):
		self = original;
		self.original = original;

		return self;

class Literal(Type):
	def __init__(self, T):
		return T;

class String(Type, Literal):

	T = Literal("");

	def __init__(self, string_t=T):
		return string_t;

class Int(Type, Literal):

	T = Literal(0);

	def __init__(self, int_t=T):
		return int_t;

class Dictionary(Type, Literal):

	T = Literal([
		"",
		""
	])

	def __init__(self, dict_t=T):
		return dict_t;

class Array(Type, Literal):

	T = Literal([any])

	def __init__(self, array_t=T):
		return array_t;

class JSON(Type, Literal, Array, Dictionary):

	T = Literal({
		Dictionary(Array([
			String, String
		],
		
		[
			String, String
		],

		[
			String, String
		],
		))
	});

	def __init__(self, json_t=T):
		return json_t;

	def format(json=T):
		return JSON(json);
	

