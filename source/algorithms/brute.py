import random

from algorithm import algorithm

class brute(algorithm):
	def __init__(self, set_actions, init_str = []):
		super(brute, self).__init__(set_actions)
		self.sLen = 0
		self.local_space = []
		self.local_space = self.generate_next_strings()
		self.space_index = 0
		self.space_scores = []
		self.move = 0
		self.max = 0

	def generate_next_strings(self):
		all_strings = self.local_space
		if len(all_strings) == 0:
			for i in range(len(self.possible_actions)):
				all_strings.append([self.possible_actions[i]])
		else:
			new_strings = []
			for j in range(len(all_strings)):
				if(len(all_strings[j]) == self.sLen):
					for k in range(len(self.possible_actions)):
						new_strings.append(all_strings[j] + [self.possible_actions[k]])
			all_strings = all_strings + new_strings

		self.sLen += 1
		return all_strings


	def process_score(self, score):
		print ("String: " + str([h.__name__[0] for h in self.local_space[self.space_index]]))

		self.space_scores.append(score)
		self.space_index += 1
		self.move = 0

		if(self.max < score):
			self.max = score
			return [(0, score, self.local_space[self.space_index-1])]

		if self.space_index >= len(self.local_space):
			if(len(self.local_space[self.space_index - 1]) < 10): #prevent algorithm from stopping too early if string is too short
				self.local_space = self.generate_next_strings()

		return [(1, score, self.local_space[self.space_index-1])]

	def get_action(self, obs):
		curr_str = self.local_space[self.space_index]
		a = curr_str[self.move % len(curr_str)]
		self.move += 1
		return a(obs)
