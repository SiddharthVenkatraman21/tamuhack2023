# don't touch this pls

# teams will be a list of tuples
# team = (<team number>:[<prefered teams>], [<tolerated teams>], [<no way teams>], <team size>)

# floors will be a dictionary
# floor = {<floor number>: <floor capacity>}

def sort_teams(teams, floors):
    # Sort teams based on the number of team members
    teams = sorted(teams.items(), key=lambda x: x[1][0], reverse=True)
    # Sort floors based on their capacity
    floors = sorted(floors.items(), key=lambda x: x[1], reverse=True)
    
    # Place teams in the best available floor based on their preferences
    for team in teams:
        placed = False
        for floor in floors:
            if placed:
                break
            if team[0] in floor[1][1]: # Check if team is in preferred teams list
                floor[1][0].append(team[0])
                placed = True
            elif not any(t in floor[1][2] for t in team[1][2]) and not any(t in floor[1][3] for t in team[1][3]):
                floor[1][0].append(team[0])
                placed = True
    # Check the capacity of each floor and make sure it is at least 25% full
    for floor in floors:
        if len(floor[1][0])/floor[1] < 0.25:
            for team in teams:
                if len(floor[1][0])/floor[1] >= 0.25:
                    break
                if team[0] in floor[1][1]:
                    floor[1][0].append(team[0])
    # Return the final placement of teams in each floor
    return {floor[0]: floor[1][0] for floor in floors}
