import movielens

#recommender object
recommender = movielens.MovieLensRecommender()

recommended_movies = recommender.recommend(user_id, num_movies=10)

#print recommended movies
for movie in recommended_movies:
    print(movie.title)
