import random
import csv

for x in range(1):
    n = random.randint(1,43)
    u = random.randint(1,500)

with open("./genres.csv", 'r') as genres:
    reader = csv.reader(genres)
    genres = list(reader)

with open ("./gameslist.csv", 'r') as games:
    gamereader = csv.reader(games)
    games = list(gamereader)

print games[u], "but as a", genres[n],"."

