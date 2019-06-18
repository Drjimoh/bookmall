#from django.test import TestCase

# Create your tests here.

class Child:
	def __init__(self, name, food):
		super().__init__(name)

	def eating(self, food):
		super().eating(food)


class Parent(Child):
	def __init__(self, name):
		print(name + ' created')

	def eating(self, food):
		print(food + ' is not my favorite')

class Child:
	def __init__(self, name, food):
		super().__init__()

	def eating(self, food):
		super().pell(self)

class Newest(Child):

	def nothing(self):
		pass
	def pell(self):
		print('pella pella')

X= Newest('newset', 'yam').eating('yellp')

'''class Onobola(Child):
	def eating(self, food):
		super().eating('yam')'''


