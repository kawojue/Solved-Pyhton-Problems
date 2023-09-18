winning_teams = []

try:
    with open('WorldSeriesWinners.txt', 'r') as file:
        for line in file:
            winning_teams.append(line.strip())
except FileNotFoundError:
    print("File not found. Please make sure 'WorldSeriesWinners.txt' exists in the current directory.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    exit()

user_team = input("Enter the name of a team: ")

team_wins = 0

for team in winning_teams:
    if user_team == team:
        team_wins += 1

if team_wins == 0:
    print(f"The team '{user_team}' did not win any World Series from 1903 to 2019.")
else:
    print(f"The team '{user_team}' won the World Series {team_wins} times from 1903 to 2019.")
