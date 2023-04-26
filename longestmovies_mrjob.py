from mrjob.job import MRJob
from mrjob.step import MRStep

class LongestTitleMovies(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_rating,
                   reducer=self.reducer_rating_count),
            MRStep(mapper=self.mapper_movie_title,
                   reducer=self.reducer_movie_title)
        ]
    
    def mapper_rating(self, _, line):
        user_id, movie_id, rating, _ = line.split('\t')
        yield movie_id, int(rating)
    
    def reducer_rating_count(self, movie_id, ratings):
        ratings_list = list(ratings)
        if len(ratings_list) >= 10:
            yield movie_id, sum(ratings_list)
    
    def mapper_movie_title(self, movie_id, total_rating):
        with open('u.item', 'r', encoding="ISO-8859-1") as f:
            for line in f:
                data = line.split('|')
                if data[0] == movie_id:
                    yield None, (total_rating, data[1])
    
    def reducer_movie_title(self, _, total_rating_title_pairs):
        pairs_sorted = sorted(total_rating_title_pairs, reverse=True)
        for i in range(min(10, len(pairs_sorted))):
            yield pairs_sorted[i][1], pairs_sorted[i][0]

if __name__ == '__main__':
    LongestTitleMovies.run()





