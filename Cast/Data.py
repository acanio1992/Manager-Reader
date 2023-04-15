import csv

import ipdb


class Data:

    def __init__(self):
        self.csvfile = None
        self.my_players = None
        self.data_players = None
        self.scores = None
        self.writer = None

    def open_rival_scoring(self):
        self.csvfile = open("report.csv", "w", newline="", encoding="utf-8")
        self.writer = csv.writer(self.csvfile)
        self.writer.writerow(["Nombre", "Sub18", "Sub21", "Sub23", "Senior", "Challenge"])  # Escribir los encabezados

    def close_csv(self):
        self.csvfile.close()

    def set_data_players(self, data):
        self.data_players = data

    def set_my_players(self, data):
        self.my_players = data

    def _calculate_score(self, low_age, high_age):
        total = 0
        i = 0
        data = self.data_players if self.my_players is not None else self.my_players
        info_players_team_high = []
        info_players_team_low = []
        for p in data:
            info_player_high = []
            info_player_low = []
            if low_age < p.age <= high_age:
                i += 1
                total = total + p.grade
                if p.grade > 3:
                    info_player_high = [p.num, p.name, p.grade]
                    info_players_team_high.append(info_player_high)

                elif p.grade <= 2:
                    info_player_low = [p.num, p.name, p.grade]
                    info_players_team_low.append(info_player_low)

        if i != 0:
            prom = total / i
            print(f"\t\t\t\tScore age {high_age} {prom} miembros {i}")
            if len(info_players_team_high) > 0:
                print(f"\t\t\t\t\t\tLos mejores jugadores de este equipo son {len(info_players_team_high)}")
                for r in info_players_team_high:
                    print(f"\t\t\t\t\t\t {r}")
            if len(info_players_team_low) > 0:
                print(f"\t\t\t\t\t\tLos peores jugadores de este equipo son {len(info_players_team_low)}")
                for r in info_players_team_low:
                    print(f"\t\t\t\t\t\t {r}")
        else:
            prom = 0
            print(f"\t\t\t\tno menores a {high_age}")

        return prom

    def calculate_team_score(self, players_total, team):
        print(f"Team {team}, miembros {len(players_total)} totales")
        players_total = sorted(players_total, key=lambda pl: -pl.grade)
        self.set_data_players(players_total)
        u18 = self._calculate_score(0, 18)
        u21 = self._calculate_score(18, 21)
        u23 = self._calculate_score(18, 23)
        senior = self._calculate_score(18, 100)
        scores = [u18, u21, u23, senior]
        challenge = self.winning_chance(scores) if self.scores is not None else None
        self.writer.writerow([team, u18, u21, u23, senior, challenge])  # Escribir los encabezados

        return scores

    def calculate_my_team_score(self, players_total):
        self.set_my_players(players_total)
        team = "My Team"
        self.scores = self.calculate_team_score(players_total, team)
        return None

    def winning_chance(self, scores_rival):
        response = []
        response.append("u18") if (scores_rival[0] - 0.5 < self.scores[0]) else None
        response.append("u21") if (scores_rival[1] - 0.5 < self.scores[1]) else None
        response.append("u23") if (scores_rival[2] - 0.5 < self.scores[2]) else None
        response.append("senior") if (scores_rival[3] - 0.5 < self.scores[3]) else None
        return response
