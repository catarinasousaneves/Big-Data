from mrjob.job import MRJob
from mrjob.step import MRStep

class LongestTitleMovies(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_movie_title,
                   reducer=self.reducer_movie_title),
            MRStep(mapper=self.mapper_output,
                   reducer=self.reducer_output)
        ]

    def mapper_movie_title(self, _, line):
        fields = line.split('\t')
        movie_id = fields[1]
        with open('/mnt/tmp/hadoop-yarn/staging/current/usercache/hadoop/appcache/application_1619080447239_0001/container_1619080447239_0001_01_000002/u.item', 'r', encoding="ISO-8859-1") as f:
            for row in f:
                movie_data = row.split('|')
                if movie_data[0] == movie_id:
                    movie_title = movie_data[1]
                    yield len(movie_title), movie_title

    def reducer_movie_title(self, length, titles):
        yield length, next(titles)

    def mapper_output(self, length, title):
        yield length, title

    def reducer_output(self, length, titles):
        for title in titles:
            yield length, title

if __name__ == '__main__':
    LongestTitleMovies.run()
