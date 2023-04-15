from Cast.Data import Data


class User:

    def __init__(self):
        self.data = None

    def can_get_data(self):
        self.data = Data()

    def open_rival_scores(self):
        self.data.open_rival_scoring()

    def calculate_my_team_score(self, players_total):
        self.data.calculate_my_team_score(players_total)

    def calculate_team_score(self, players_total, team):
        self.data.calculate_team_score(players_total, team)
