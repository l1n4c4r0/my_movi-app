from fastapi import HTTPException

class MovieDirector:
    def __init__(self):
        self.movie_directors = []

    def get_movie_director_by_id(self, movie_director_id):
        for movie_director in self.movie_directors:
            if movie_director["id"] == movie_director_id:
                return movie_director
        return None

    def create_movie_director(self, movie_director):
        self.movie_directors.append(movie_director)
        return movie_director

    def update_movie_director(self, movie_director_id, updated_movie_director):
        for movie_director in self.movie_directors:
            if movie_director["id"] == movie_director_id:
                movie_director.update(updated_movie_director)
                return movie_director
        return None

    def delete_movie_director(self, movie_director_id):
        for movie_director in self.movie_directors:
            if movie_director["id"] == movie_director_id:
                self.movie_directors.remove(movie_director)
                return
        return None

