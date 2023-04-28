from mrjob.job import MRJob
from mrjob.step import MRStep


class LongestTitleMovies(MRJob):

    MIN_COUNT = 10
    SHOW_LIMIT = 10

    def movie_title(self, movie_id):
        with open("/root/u.item", "r", encoding="ISO-8859-1") as infile:
            for line in infile:
                fields = line.split('|')
                if fields[0] == movie_id:
                    return fields[1]
        return None

    def mapper1(self, _, line):
        user_id, movie_id, rating, timestamp = line.split('\t')
        yield movie_id, 1

    def reducer1(self, movie_id, counts):
        total_count = sum(counts)
        if total_count >= self.MIN_COUNT:
            yield None, (total_count, self.movie_title(movie_id))

    def reducer2(self, _, values):
        for count, title in sorted(values, reverse=True)[:self.SHOW_LIMIT]:
            yield (title, count), None

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(reducer=self.reducer2)
        ]


if __name__ == '__main__':
    LongestTitleMovies.run()


