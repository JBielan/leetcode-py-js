class Foo:
	def __init__(self):
		# those are labels checking whether the functions were executed
		self.first_check = False
		self.second_check = False

	def first(self, printFirst: 'Callable[[], None]') -> None:
		# just execute the first function
		printFirst()
		self.first_check = True

	def second(self, printSecond: 'Callable[[], None]') -> None:
		# this while loop runs continously to wait for first function to run
		while not self.first_check:
			continue

		# when it leaves the loop, second function can be run
		printSecond()
		self.second_check = True

	def third(self, printThird: 'Callable[[], None]') -> None:
		# analogously third function
		while not self.second_check:
			continue

		printThird()