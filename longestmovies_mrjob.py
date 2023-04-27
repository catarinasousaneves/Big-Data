from mrjob.job import MRJob
from mrjob.step import MRStep
import csv


class LongestTitleMovies(MRJob):

	MIN_COUNT = 10
	SHOW_LIMIT = 10

	def movie_title(self, movie_id):
		'''
		Convert from movie id to movie title
		'''
		with open("u.item", "r", encoding="ISO-8859-1") as infile:
			reader = csv.reader(infile, delimiter='|')
			next(reader)
			for line in reader:
				if int(movie_id) == int(line[0]):
					return line[1]

	def steps(self):
		'''
		Pipeline of MapReduce tasks
		'''
		return [
			MRStep(mapper=self.mapper1, reducer=self.reducer1),
			MRStep(mapper=self.mapper3),
			MRStep(mapper=self.mapper4, reducer=self.reducer2)
		]

	def mapper1(self, _, line):
		(user_id, movie_id, rating, timestamp) = line.split('\t')
		movie_title = self.movie_title(movie_id)
		yield movie_id, (movie_title, rating)

	def reducer1(self, movie_id, values):
		sum_ratings, count = 0, 0
		movie_title = ""
		for movie_title, rating in values:
			sum_ratings += int(rating)
			count += 1
		if count >= self.MIN_COUNT:
			yield movie_id, (movie_title, sum_ratings/float(count))

	def mapper3(self, movie_id, value):
		(title, rating) = value
		if rating >= str(self.MIN_COUNT):
			yield movie_id, (title, rating)

	def mapper4(self, movie_id, value):
		(title, rating) = value
		yield len(title), (rating, title)

	def reducer2(self, length, values):
		i = 0
		for rating, title in sorted(values, reverse=True):
			i += 1
			if i <= self.SHOW_LIMIT:
				yield title, float(rating)

if __name__ == '__main__':
	LongestTitleMovies.run()

