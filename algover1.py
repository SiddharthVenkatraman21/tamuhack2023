# don't touch this pls
import heapq

# teams will be a list of tuples
# team = (<team number>:[<prefered teams>], [<tolerated teams>], [<no way teams>], <team size>)

# floors will be a dictionary
# floor = {<floor number>: <floor capacity>}

def sort_teams_into_floors(teams, floors):
    # sort teams by number of members in descending order
    teams = sorted(teams, key=lambda x: x[2], reverse=True)

    # create priority queue for floors
    # key is the available capacity, value is the floor number
    floor_queue = [(floor[1], floor[0]) for floor in floors]
    heapq.heapify(floor_queue)

    # list to hold assigned teams
    assigned_teams = []

    for team in teams:
        # get the floor with highest available capacity from priority queue
        available_floor = heapq.heappop(floor_queue)
        floor_num, available_capacity = available_floor

        # check if the capacity of the floor is more than 25%
        if available_capacity >= 0.25 * floors[floor_num][1]:
            # add team to the floor and update floor's available capacity
            assigned_teams.append((team[0], floor_num))
            available_capacity -= team[2]
            heapq.heappush(floor_queue, (available_capacity, floor_num))
        else:
            # if no floor with more than 25% capacity is available, remove team from the list of teams
            pass

    # ensure that none of the floors are empty
    for floor in floors:
        floor_num = floor[0]
        assigned_teams_on_floor = [t for t in assigned_teams if t[1] == floor_num]
        if len(assigned_teams_on_floor) == 0:
            team_to_move = sorted(assigned_teams, key=lambda x: x[1])[0]
            assigned_teams.remove(team_to_move)
            assigned_teams.append((team_to_move[0], floor_num))

    return assigned_teams