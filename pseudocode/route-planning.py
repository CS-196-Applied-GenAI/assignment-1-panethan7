# Route Planning System with Pseudocode

# Function 1: Fully written in pseudocode
# ----------------------------------------
# Define function process_route_data(data)
#     Initialize empty dictionary route_map
#     For each entry in data:
#         Extract 'starting_point', 'destination', and 'distance'
#         Store 'starting_point' as key and a list of (destination, distance) tuples as value in route_map
#     Return route_map


# Function 2: Function header with brief pseudocode
# --------------------------------------------------
def find_shortest_route(start, destination, route_map):
    """
    Find the shortest route between two locations.
    - Use a pathfinding algorithm to determine the optimal route.
    - Return the route and estimated distance.
    """
    pass  # To be implemented

# Pseudocode block 1: No function title, just high-level steps
# ------------------------------------------------------------
# Read user input for starting location and destination
# Validate that both locations exist in the route map
# If both are valid, call the shortest route function and return the result
# If not, return an error message

# Pseudocode block 2: Another missing function title
# --------------------------------------------------
# Allow the system to handle multiple route calculations in a loop
# - Continue accepting input from the user
# - Provide the shortest route for each query
# - Allow the user to exit by typing 'quit'

# BLANK SPACE: Students will continue writing the route planning implementation from here
# - Calculate the estimated travel time based on distance and average speed
# - Implement a function to suggest alternative routes if the shortest route is unavailable
# - Design a function that calculates the total fuel cost for a given route based on fuel efficiency

if __name__ == "__main__":
    route_data = load_route_data("routes.txt")