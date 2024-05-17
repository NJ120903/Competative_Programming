import re

def parse_game_result(game_result):
    match = re.match(r'(\w+)#(\d+)@(\d+)#(\w+)', game_result)
    if match:
        team1, score1, score2, team2 = match.groups()
        return team1, int(score1), int(score2), team2
    else:
        return None

def calculate_standings(tournament_name, team_names, game_results):
    standings = {team: [0, 0, 0, 0, 0, 0] for team in team_names}
    for result in game_results:
        team1, score1, score2, team2 = parse_game_result(result)
        if team1 and team2:
            standings[team1][0] += 1  # games played
            standings[team2][0] += 1  # games played
            standings[team1][4] += score1  # goals for
            standings[team2][4] += score2  # goals for
            standings[team1][5] += score2  # goals against
            standings[team2][5] += score1  # goals against
            if score1 > score2:
                standings[team1][1] += 1  # wins
                standings[team2][3] += 1  # losses
            elif score1 < score2:
                standings[team2][1] += 1  # wins
                standings[team1][3] += 1  # losses
            else:
                standings[team1][2] += 1  # ties
                standings[team2][2] += 1  # ties
    standings = [(team, 3 * wins + ties, wins, ties, losses, goals_for - goals_against, goals_for, goals_against) 
                  for team, (games, wins, ties, losses, goals_for, goals_against) in standings.items()]
    standings.sort(key=lambda x: (-x[1], -x[2], x[5], x[6], x[3], x[0].lower()))
    return standings

def print_standings(tournament_name, standings):
    print(tournament_name)
    for i, (team, points, wins, ties, losses, goal_difference, goals_for, goals_against) in enumerate(standings, start=1):
        print(f"{i}) {team} {points}p, {len(standings)}g ({wins}-{ties}-{losses}), {goal_difference}gd ({goals_for}-{goals_against})")

def main():
    num_tournaments = int(input("Enter the number of tournaments: "))
    for _ in range(num_tournaments):
        tournament_name = input("Enter the tournament name: ")
        num_teams = int(input("Enter the number of teams: "))
        team_names = [input(f"Enter team {_+1} name: ") for _ in range(num_teams)]
        num_games = int(input("Enter the number of games: "))
        game_results = [input(f"Enter game {_+1} result: ") for _ in range(num_games)]
        standings = calculate_standings(tournament_name, team_names, game_results)
        print_standings(tournament_name, standings)
        print()

if __name__ == "__main__":
    main()