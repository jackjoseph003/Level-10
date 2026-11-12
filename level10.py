
import pandas as pd

# This reads the CSV file
df = pd.read_csv("cfb.csv")

season = int(input("Enter a season to analyze: "))

season_data = df.query("Season == @season")

# This is a checker
if len(season_data) == 0:
    print("Season not found.")

else:
    categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    for index, row in season_data.iterrows():

        team = row["Team"]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins"].append(team)

        elif wins >= 8:
            categories["8-9 wins"].append(team)

        elif wins >= 6:
            categories["6-7 wins"].append(team)

        else:
            categories["Fewer than 6 wins"].append(team)

    print()
    print(f"College Football Results for {season}")

    for category, teams in categories.items():
        print()
        print(f"{category}:")

        for team in teams:
            print(team)
