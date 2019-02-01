# coding: utf-8
class Team:
    num = 0
    win = 0
    lose = 0
    draw = 0
    def score(this):
        return (this.win * 2) + this.draw

times = int(input())

teams = []

for i in range(times):
    line = input()
    team = Team()
    team.num = i + 1
    for ch in line:
        if ch == 'W':
            team.win += 1
        elif ch == 'D':
            team.draw += 1
        elif ch == 'L':
            team.lose += 1
    teams.append(team)

won = Team()
for team in teams:
    if won.score() < team.score():
        won = team

print(f"{won.num} {won.score()} {won.win} {won.draw} {won.lose}")
