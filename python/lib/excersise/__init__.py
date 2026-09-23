


__all__ = [
	"Exercise"
]



class Node:
	def __init__(self):
		self.children = []
		
	def __enter__(self):									return self
	def __exit__(self, exc_type, exc_value, traceback):		return False

	def print(self, text):
		self.children.append(PrintNode(text))

	def render(self, prefix="", is_last=True, spacing: tuple = None):
		if not spacing: spacing = (0,)
		result = []
		
		for i, child in enumerate(self.children):
			child_is_last = i == len(self.children) - 1
			result.extend(
				child.render(
					prefix, child_is_last, spacing[1:]
				)
			)

			if spacing[0] > 0 and not child_is_last:
				result.extend(
					[prefix + "│   "] * spacing[0]
				)
		
		return result



class NodeWithTitle(Node):
	def __init__(self, title):
		super().__init__()
		self.title = title

	def render(self, prefix="", is_last=True, spacing: tuple = None):
		if not spacing: spacing = (0,)
		connector = "└── " if is_last else "├── "

		result = [
			prefix + connector + self.title + ":"
		]
		child_prefix = prefix + (
			"	" if is_last else "│   "
		)
		
		result.extend(super().render(prefix=child_prefix, is_last=is_last, spacing=spacing))
		return result



class PrintNode:
	def __init__(self, text):
		self.text = text

	def render(self, prefix, is_last, spacing: tuple = (0,)):
		lines = self.text.splitlines()
		connector = "└── " if is_last else "├── "
		result = [prefix + connector + lines[0]]
		# continuation lines of the same print()
		continuation_prefix = prefix + (
			"	" if is_last else "│   "
		)
		for line in lines[1:]:
			result.append(continuation_prefix + line)
		return result



class Exercise(Node):
	def __init__(self, title, spacing: tuple = (0,)):
		super().__init__()
		self.title = title
		self.spacing = spacing

	def __enter__(self):
		print(self.title)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		for line in self.render(spacing=self.spacing):
			print(line)
		return False
	
	def subquestion(self, title):
		question = NodeWithTitle(title)
		self.children.append(question)
		return question