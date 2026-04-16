# Route Planning System with Pseudocode
import heapq
from collections import defaultdict
from pathlib import Path


# Function 1: Fully written in pseudocode
# ----------------------------------------
# Define function process_route_data(data)
#     Initialize empty dictionary route_map
#     For each entry in data:
#         Extract 'starting_point', 'destination', and 'distance'
#         Store 'starting_point' as key and a list of (destination, distance) tuples as value in route_map
#     Return route_map
def process_route_data(data):
    route_map = defaultdict(list)
    for entry in data:
        starting_point = entry["starting_point"]
        destination = entry["destination"]
        distance = float(entry["distance"])
        route_map[starting_point].append((destination, distance))
    return dict(route_map)


# Function 2: Function header with brief pseudocode
# --------------------------------------------------
def find_shortest_route(start, destination, route_map):
    """
    Find the shortest route between two locations.
    - Use a pathfinding algorithm to determine the optimal route.
    - Return the route and estimated distance.
    """
    # Initialize a priority queue with (0, start, [start])
    # Initialize a dictionary shortest_distance with infinity for each location
    # Set shortest_distance[start] = 0
    # while priority queue is not empty:
    #     Pop the location with the smallest known distance
    #     If current location is destination:
    #         Return (path_taken, total_distance)
    #     For each (neighbor, edge_distance) connected to current location:
    #         Compute new_distance = current_distance + edge_distance
    #         If new_distance is smaller than shortest_distance[neighbor]:
    #             Update shortest_distance[neighbor]
    #             Push (new_distance, neighbor, updated_path) into priority queue
    # If destination is never reached, return (None, "No route found")
    if start == destination:
        return [start], 0.0

    pq = [(0.0, start, [start])]
    shortest_distance = {location: float("inf") for location in route_map}
    shortest_distance[start] = 0.0

    while pq:
        current_distance, current_location, path_taken = heapq.heappop(pq)

        if current_distance > shortest_distance.get(current_location, float("inf")):
            continue

        if current_location == destination:
            return path_taken, current_distance

        for neighbor, edge_distance in route_map.get(current_location, []):
            new_distance = current_distance + edge_distance
            if new_distance < shortest_distance.get(neighbor, float("inf")):
                shortest_distance[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor, path_taken + [neighbor]))

    return None, "No route found"

# Pseudocode block 1: No function title, just high-level steps
# ------------------------------------------------------------
# Read user input for starting location and destination
# Validate that both locations exist in the route map
# If both are valid, call the shortest route function and return the result
# If not, return an error message
#
# def get_route_request_and_solve(route_map)
#     Build a set of all valid locations from route_map keys and destinations
#     Prompt user: "Enter starting location:"
#     Prompt user: "Enter destination:"
#     Normalize input (strip spaces and match title case if needed)
#     If start not in valid locations or destination not in valid locations:
#         Return "Error: One or both locations are not in the route network."
#     Call find_shortest_route(start, destination, route_map)
#     If no route found:
#         Return "No available route between selected locations."
#     Return route details (ordered stops + total distance)
def get_route_request_and_solve(route_map, start=None, destination=None):
    all_locations = build_location_set(route_map)

    if start is None:
        start = input("Enter starting location: ")
    if destination is None:
        destination = input("Enter destination: ")

    start = normalize_location_name(start)
    destination = normalize_location_name(destination)

    if start not in all_locations or destination not in all_locations:
        return "Error: One or both locations are not in the route network."

    route, distance = find_shortest_route(start, destination, route_map)
    if route is None:
        return "No available route between selected locations."
    return route, distance

# Pseudocode block 2: Another missing function title
# --------------------------------------------------
# Allow the system to handle multiple route calculations in a loop
# - Continue accepting input from the user
# - Provide the shortest route for each query
# - Allow the user to exit by typing 'quit'
#
# Define function interactive_route_planner(route_map)
#     Print welcome message with instructions and example cities from routes.txt
#     Loop forever:
#         Ask user for start city (or 'quit' to exit)
#         If start city is 'quit':
#             Break loop
#         Ask user for destination city (or 'quit' to exit)
#         If destination city is 'quit':
#             Break loop
#         Validate input cities against route_map network
#         If invalid:
#             Print validation error and continue loop
#         Compute shortest route with find_shortest_route(...)
#         Print route path and total distance in miles
#     Print goodbye message when loop exits
def interactive_route_planner(route_map):
    print("Route Planner")
    print("Type 'quit' at any prompt to exit.")
    print("Example cities:", ", ".join(sorted(build_location_set(route_map))[:8]))

    while True:
        start = input("Start city: ").strip()
        if start.lower() == "quit":
            break

        destination = input("Destination city: ").strip()
        if destination.lower() == "quit":
            break

        result = get_route_request_and_solve(route_map, start, destination)
        if isinstance(result, str):
            print(result)
            continue

        route, distance = result
        print(f"Shortest route: {' -> '.join(route)} ({distance:.1f} miles)")

    print("Goodbye.")

# BLANK SPACE: Students will continue writing the route planning implementation from here
# - Calculate the estimated travel time based on distance and average speed
# - Implement a function to suggest alternative routes if the shortest route is unavailable
# - Design a function that calculates the total fuel cost for a given route based on fuel efficiency
#
# Define function estimate_travel_time(total_distance, average_speed_mph)
#     If average_speed_mph <= 0:
#         Return error "Average speed must be greater than zero."
#     Compute hours = total_distance / average_speed_mph
#     Return hours
#
# Define function suggest_alternative_routes(start, destination, route_map, max_alternatives)
#     Use modified pathfinding (k-shortest paths approach)
#     Keep track of previously returned paths to avoid duplicates
#     Generate up to max_alternatives valid routes sorted by distance
#     Return list of (route_path, route_distance)
#
# Define function calculate_fuel_cost(total_distance, miles_per_gallon, fuel_price_per_gallon)
#     If miles_per_gallon <= 0 or fuel_price_per_gallon < 0:
#         Return error "Fuel inputs are invalid."
#     gallons_needed = total_distance / miles_per_gallon
#     total_cost = gallons_needed * fuel_price_per_gallon
#     Return total_cost
def estimate_travel_time(total_distance, average_speed_mph):
    if average_speed_mph <= 0:
        raise ValueError("Average speed must be greater than zero.")
    return total_distance / average_speed_mph


def suggest_alternative_routes(start, destination, route_map, max_alternatives=3):
    if max_alternatives <= 0:
        return []

    start = normalize_location_name(start)
    destination = normalize_location_name(destination)

    pq = [(0.0, [start])]
    results = []
    seen_paths = set()

    while pq and len(results) < max_alternatives:
        current_distance, path = heapq.heappop(pq)
        node = path[-1]

        if node == destination:
            path_key = tuple(path)
            if path_key not in seen_paths:
                seen_paths.add(path_key)
                results.append((path, current_distance))
            continue

        for neighbor, edge_distance in route_map.get(node, []):
            if neighbor in path:
                continue  # avoid cycles for simple path alternatives
            new_path = path + [neighbor]
            heapq.heappush(pq, (current_distance + edge_distance, new_path))

    return results


def calculate_fuel_cost(total_distance, miles_per_gallon, fuel_price_per_gallon):
    if miles_per_gallon <= 0 or fuel_price_per_gallon < 0:
        raise ValueError("Fuel inputs are invalid.")
    gallons_needed = total_distance / miles_per_gallon
    return gallons_needed * fuel_price_per_gallon
#
# Define function load_route_data(file_path)
#     Open file_path and read each non-empty line
#     For each line in format "CityA, CityB, Distance":
#         Split by comma and trim whitespace
#         Convert distance string to numeric value
#         Add bidirectional entries:
#             CityA -> (CityB, distance)
#             CityB -> (CityA, distance)
#     Return route_map produced from file data

def load_route_data(file_path):
    """
    Pseudocode outline:
    - Open the route file.
    - Parse each "source, destination, distance" record.
    - Build a bidirectional route map.
    - Return the completed map.
    """
    parsed_edges = []
    with open(file_path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line:
                continue

            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 3:
                raise ValueError(f"Invalid route entry: {line}")

            city_a, city_b, distance_str = parts
            distance = float(distance_str)
            parsed_edges.append(
                {
                    "starting_point": city_a,
                    "destination": city_b,
                    "distance": distance,
                }
            )
            parsed_edges.append(
                {
                    "starting_point": city_b,
                    "destination": city_a,
                    "distance": distance,
                }
            )

    return process_route_data(parsed_edges)


def normalize_location_name(name):
    return " ".join(word.capitalize() for word in name.strip().split())


def build_location_set(route_map):
    locations = set(route_map.keys())
    for neighbors in route_map.values():
        for destination, _distance in neighbors:
            locations.add(destination)
    return locations

if __name__ == "__main__":
    routes_file = Path(__file__).with_name("routes.txt")
    route_data = load_route_data(routes_file)
    demo_route, demo_distance = find_shortest_route("New York", "Washington", route_data)
    print(f"Demo shortest route: {' -> '.join(demo_route)} ({demo_distance:.1f} miles)")