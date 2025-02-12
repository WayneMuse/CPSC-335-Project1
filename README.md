# CPSC-335-Project1
Spring 2025 CPSC 335 - Algorithm Engineering Due: 02/28

To run the CPSC-335 Project, just run main.py and bring up the menu and choose which algorithm you want to test.
When inputing an array of numbers do not write them with the brackets, write it as simply the numbers seperated by the commas 5, 25, 15, 10, 15


## Algorithm 2 Connecting Pairs of Persons 
### Pesudocode
Input: A list row of 2n individuals representing seat arrangements in integer format.
Output: Minimum number of swaps required to seat all couples together.

1. Create a dictionary position mapping each person to their index in row and initialize swaps to 0.
2. Define a function partner(person):
    i If person is even, return person + 1 (its partner).
    ii. If person is odd, return person - 1 (its partner).
3. Iterate through the list in steps of 2:
    i. Let first_person = row[i] and second_person = row[i + 1].
    ii. Compute correct_partner = partner(first_person).
    iii. If second_person != correct_partner, perform a swap:
        a. Locate correct_partner in row using position.
        b. Swap row[i + 1] and row[partner_index].
        c. Update position dictionary accordingly.
        d. Increment swaps.
4. Return swaps.

### Mathmatical Analysis and Big-O
Constructing position takes O(n) time.
The loop runs O(n) times, and each swap operation takes O(1) due to dictionary lookups.
Space complexity is O(n) due to the position dictionary.
Thus, the overall time complexity is O(n).