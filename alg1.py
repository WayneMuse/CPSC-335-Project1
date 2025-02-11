def find_starting(city_distances=[], fuel=[], mpg=int) -> int:
    n = len(city_distances)

        
    # Initialize variables
    total_fuel = 0
    total_distance = 0
    current_tank = 0
    start_city = 0

    # Iterate over each city
    for i in range(n):
        fuel_gained = fuel[i] * mpg
        distance_needed = city_distances[i]
        
        # Update totals
        total_fuel += fuel_gained
        total_distance += distance_needed
        
        # Update current tank balance
        current_tank += fuel_gained - distance_needed
        
        # If tank balance becomes negative, reset start city
        if current_tank < 0:
            start_city = i + 1
            current_tank = 0

    # Check if there's a valid solution
    if total_fuel >= total_distance:
        return start_city
    else:
        return -1
    
# Sample Input
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Output the preferred starting city
preferred_city = find_starting(city_distances, fuel, mpg)
print("The preferred starting city is:", preferred_city)
