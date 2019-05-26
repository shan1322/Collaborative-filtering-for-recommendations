from code.rank import Rank
import json

with open("../json/ratings.json") as ratings:
    ratings = json.load(ratings)
obj = Rank()


def predict(movie_name, rating):
    correlation_dict = obj.rank_users(movie_name, ratings)
    n = 0
    predicted_rating = 0
    for critic in correlation_dict.keys():
        if movie_name in rating[critic].keys():
            predicted_rating = predicted_rating + correlation_dict[critic] * rating[critic][movie_name]
            n = n + 1
    if n != 0:
        predicted_rating = predicted_rating / n
    return predicted_rating


print(predict('3', ratings))
