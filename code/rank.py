import math


class Rank:
    def __init__(self):
        self.number_of_critic = 5

    @staticmethod
    def sem_correlation(user_1, user_2):
        n = 0
        sum1, sum2, sum1s, sum2s, pum = 0, 0, 0, 0, 0
        for movie in user_1.keys():
            if movie in user_2.keys():
                n = n + 1
                sum1 = sum1 + user_1[movie]
                sum2 = sum2 + user_2[movie]
                sum1s = sum1s + user_1[movie] ** 2
                sum2s = sum2s + user_2[movie] ** 2
                pum = pum + user_1[movie] * user_2[movie]
        if n != 0:
            num = pum - (sum1 * sum2) / n
            den = math.sqrt((sum1s - pow(sum1, 2) / n) * (sum2s - pow(sum2, 2) / n))
            if den == 0:
                return 0
            else:
                r = num / den
                return r

    def rank_users(self, user_name, rating):
        rank_dict = {}
        for user in rating.keys():
            if user != user_name:
                sem_corr = self.sem_correlation(rating[user_name], rating[user])
                if sem_corr is not None:
                    rank_dict[user] = sem_corr

        sorted_list = sorted(rank_dict.items(), key=lambda kv: kv[1], reverse=True)[0:self.number_of_critic]
        sorted_dict = {}
        for element in sorted_list:
            sorted_dict[element[0]] = element[1]
        return sorted_dict
