import pandas as pd 

files = ["castle-solutions.csv", "castle-solutions-2.csv", "castle-solutions-3.csv", "castle-solutions-4.csv"]
dataframes = []

for file in files:
    df = pd.read_csv("./prev_battles/" + file)
    dataframes.append(df)

all_battles = pd.concat(dataframes, ignore_index=True)
all_battles = all_battles.iloc[:, :10]

team_list = all_battles.values.tolist()


def battle(team1, team2) -> int:
    team1_pts = 0
    team2_pts = 0
    
    for n in range(10):
        if team1[n] > team2[n]:
            team1_pts += n + 1
        elif team2[n] > team1[n]:
            team2_pts += n + 1
    
    if team1_pts > team2_pts:
        return 1
    elif team2_pts > team1_pts:
        return -1
    return 0



def battle_all(team_list) -> int:
    N = len(team_list)
    print(f"There are {N} teams")
    pnt_cnts = [0.0] * N

    for i in range(N):
        for j in range(i + 1, N):
            res = battle(team_list[i], team_list[j])
            if res == 1:
                pnt_cnts[i] += 1
            elif res == -1:
                pnt_cnts[j] += 1
            else:
                pnt_cnts[i] += .5
                pnt_cnts[j] += .5
    
    return pnt_cnts

def new_battle_all(team_list):
    while len(team_list) > 1:
        N = len(team_list)
        print(f"There are {N} teams")
        pnt_cnts = [0.0] * N
        for i in range(N):
            for j in range(i + 1, N):
                res = battle(team_list[i], team_list[j])
                if res == 1:
                    pnt_cnts[i] += 1
                elif res == -1:
                    pnt_cnts[j] += 1
                else:
                    pnt_cnts[i] += .5
                    pnt_cnts[j] += .5
        min_idx = pnt_cnts.index(min(pnt_cnts))
        team_list.pop(min_idx)
    return team_list




# ______ THis is the process I used to select the team at the bottom ________

# pnt_cnts = battle_all(team_list)
# sorted_teams_1 = [team for _, team in sorted(zip(pnt_cnts, team_list), reverse=True)]

# pnt_cnts = battle_all(sorted_teams_1[:2000])
# sorted_teams_2 = [team for _, team in sorted(zip(pnt_cnts, sorted_teams_1[:2000]), reverse=True)]

# pnt_cnts = battle_all(sorted_teams_2[:750])
# best_idx = pnt_cnts.index(max(pnt_cnts))

# best_team = sorted_teams_2[best_idx]

# print(best_team)

#____________________________________________________________________________
# team_list.append([0, 2, 11, 3, 4, 23, 5, 6, 37, 9]) team I submitted


# _____Running first 1000 then running new kind of battle__________________
# pnt_cnts = battle_all(team_list)
# sorted_teams_1 = [team for _, team in sorted(zip(pnt_cnts, team_list), reverse=True)]
# sorted_teams_1 = sorted_teams_1[:1000]

# print(new_battle_all(sorted_teams_1))

# [[4, 3, 8, 12, 13, 25, 6, 5, 13, 11]] This team wins the new battle if you take the top 1000 from the first run
#__________________________________________________________________________