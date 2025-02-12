# CPSC-335-Project1 
Spring 2025 CPSC 335 - Algorithm Engineering Due: 02/28
Wayne Muse - 88601211
waynemuse@csu.fullerton.edu
https://github.com/WayneMuse/CPSC-335-Project1

## Running Project1
1. Run the Program
    1. Execute main.py to start the program.
    2. A menu will appear, allowing you to select which algorithm you want to test.
2. Choosing an Algorithm
    1. Enter 1 to test Algorithm 1: Greedy Approach to Hamiltonian Problem.
    2. Enter 2 to test Algorithm 2: Connecting Pairs of Persons.
    3. Enter 3 to exit the program.
2. Input Format
    1. When entering an array of numbers, do not use brackets [ ].
    2. Instead, enter the numbers separated by spaces.
    3. Example: don't: [5,25,15,10,15]  do: 5 25 15 10 15

## Algorithm 1: Greedy Approach to Hamiltonian Problem
### Pseudocode
Input:
- city_distances: List of distances between neighboring cities.
- fuel: List of fuel available at each city.
- mpg: integer miles per gallon the car can travel.

Output:
- Index of the preferred starting city.

1. Initialize Variables:
    - total_fuel = 0
    - total_distance = 0
    - current_tank = 0
    - start_city = 0

2. Iterate over all cities (i = 0 to n - 1):
    1. Compute fuel_gained = fuel[i] * mpg
    2. Compute distance_needed = city_distances[i]
3. Update variables
    1. Update total_fuel += fuel_gained
    2. Update total_distance += distance_needed
    3. Update current_tank += fuel_gained - distance_needed
4. If current_tank < 0:
    1. Set start_city = i + 1
    2. Reset current_tank = 0
5. Check Validity:
    1. If total_fuel >= total_distance, return start_city
    2. Otherwise, return -1

### Mathematical Analysis and Big-O Complexity
Iterating through the cities takes O(n) time.
Each lookup and arithmetic operation is O(1).
Space complexity: O(1) (constant space usage).
Overall time complexity: O(n).

## Algorithm 2 Connecting Pairs of Persons 
### Pesudocode
Input: A list row of 2n individuals representing seat arrangements in integer format.
Output: Minimum number of swaps required to seat all couples together.

1. Create a dictionary position mapping each person to their index in row and initialize swaps to 0.
2. Define a function partner(person):
    1. If person is even, return person + 1 (its partner).
    2. If person is odd, return person - 1 (its partner).
3. Iterate through the list in steps of 2:
    1. Let first_person = row[i] and second_person = row[i + 1].
    2. Compute correct_partner = partner(first_person).
    3. If second_person != correct_partner, perform a swap:
        1. Locate correct_partner in row using position.
        2. Swap row[i + 1] and row[partner_index].
        3. Update position dictionary accordingly.
        4. Increment swaps.
4. Return swaps.

### Mathematical Analysis and Big-O Complexity
Constructing position takes O(n) time.
The loop runs O(n) times, and each swap operation takes O(1) due to dictionary lookups.
Space complexity is O(n) due to the position dictionary.
Thus, the overall time complexity is O(n).