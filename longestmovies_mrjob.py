from mrjob.job import MRJob
from mrjob.step import MRStep
import csv


class LongestTitleMovies(MRJob):

	MIN_COUNT = 10
	SHOW_LIMIT = 10

    def movie_title(self, movie_id):
        # open the file using the absolute path
        with open("/root/u.item", "r", encoding="ISO-8859-1") as infile:
            for line in infile:
                fields = line.split("|")
                if fields[0] == movie_id:
                    return fields[1]
            return "Movie ID not found"

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(reducer=self.reducer2)
        ]

    def mapper1(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split("\t")
        yield movie_id, len(self.movie_title(movie_id))

    def reducer1(self, key, values):
        yield None, (max(values), self.movie_title(key))

    def reducer2(self, _, values):
        sorted_values = sorted(values, reverse=True)
        for value in sorted_values:
            yield value[1], value[0]

if __name__ == '__main__':
    LongestTitleMovies.run()


