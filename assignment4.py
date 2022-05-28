# Sample data for Relationship Status below:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

'''
Sample data for Tic Tac Toe below:
'''

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

'''
Sample data for ETA below:
(from_stop, to_stop)
'''

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

#'''Assignment 4
# This assignment covers your proficiency with Python's data structures.
# It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
# '''
#   
#     Item 1.
#     Relationship Status. 20 points.
#     Let us pretend that you are building a new app.
#     Your app supports social media functionality, which means that users can have
#     relationships with other users.
#     There are two guidelines for describing relationships on this social media app:
#     1. Any user can follow any other user.
#     2. If two users follow each other, they are considered friends.
#     This function describes the relationship that two users have with each other.
#     Please see "assignment-4-sample-data.py" for sample data. The social graph
#     will adhere to the same pattern.
#     Parameters
#     ----------
#     from_member: str
#         the subject member
#     to_member: str
#         the object member
#     social_graph: dict
#         the relationship data    
#     Returns
#     -------
#     str
#         "follower" if fromMember follows toMember,
#         "followed by" if fromMember is followed by toMember,
#         "friends" if fromMember and toMember follow each other,
#         "no relationship" if neither fromMember nor toMember follow each other.
#     '''
#     # Write your code below this line

def relationship_status(from_member, to_member, social_graph):
    follower = social_graph[from_member]["following"]
    following = social_graph[to_member]["following"]
    
    if from_member in following and to_member in follower:
        return "friends"
    elif to_member in follower:
        return "follower"
    elif from_member in following:
        return "followed by"
    else:
        return "no relationship"
print(relationship_status("@joaquin","@chums",social_graph))
print(relationship_status("@jobenilagan", "@bongolpoc", social_graph))

    
#     '''
#     Item 2.
#     Tic Tac Toe. 20 points.
#     Tic Tac Toe is a common paper-and-pencil game. 
#     Players must attempt to successfully draw a straight line of their symbol across a grid.
#     The player that does this first is considered the winner.
#     This function evaluates a tic tac toe board and returns the winner.
#     Please see "assignment-4-sample-data.py" for sample data. The board will adhere
#     to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
#     have more than one winner. The board will only ever have 2 unique symbols at the same time.
#     Parameters
#     ----------
#     board: list
#         the representation of the tic-tac-toe board as a square list of lists
#     Returns
#     -------
#     str
#         the symbol of the winner or "NO WINNER" if there is no winner
#     '''
#     # Write your code below this line

def tic_tac_toe(board):
    #FOR THE HORIZONTALS
    for row in board: 
        if row[0] == row[1] == row[2] and row[0] !=" ":
            return row[0]
            
    #FOR THE VERTICALS:
    for col in range(3):  
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] !=" ":
            return board[0][col]
    #FOR THE DIAGONALS    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] !=" ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] !=" ":
        return board[0][2]


print(tic_tac_toe(board1))
print(tic_tac_toe(board2))
print(tic_tac_toe(board3))
print(tic_tac_toe(board4))
print(tic_tac_toe(board5))
print(tic_tac_toe(board6))

#     '''
#     Item 3.
#     ETA. 25 points.
#     A shuttle van service is tasked to travel along a predefined circlar route.
#     This route is divided into several legs between stops.
#     The route is one-way only, and it is fully connected to itself.
#     This function returns how long it will take the shuttle to arrive at a stop
#     after leaving another stop.
#     Please see "assignment-4-sample-data.py" for sample data. The route map will
#     adhere to the same pattern. The route map may contain more legs and more stops,
#     but it will always be one-way and fully enclosed.
#     Parameters
#     ----------
#     first_stop: str
#         the stop that the shuttle will leave
#     second_stop: str
#         the stop that the shuttle will arrive at
#     route_map: dict
#         the data describing the routes
#     Returns
#     -------
#     int
#         the time it will take the shuttle to travel from first_stop to second_stop
#     '''
#     # Write your code below this line
def eta(first_stop, second_stop, route_map):
    final = 0
    loop = 0
    for i in legs.keys():
        if i[0] == first_stop:
            loop = i
    while loop[1] != second_stop:
        final+= legs[loop]['travel_time_mins']
        for i in legs.keys():
            if i[1] == second_stop:
                loop = i
    final += legs[loop]['travel_time_mins']
    return final

print(eta("upd", "admu", legs))
print(eta("admu", "upd", legs))
print(eta("admu", "dlsu", legs))
print(eta("dlsu", "upd", legs))
    
    
    
    
    
    
    
    
    