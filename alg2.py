def min_swaps(row):
    # Map each person to their position in the row
    position = {person: i for i, person in enumerate(row)}
    swaps = 0
    
    def partner(person):
        return person - 1 if person % 2 else person + 1
    
    for i in range(0, len(row), 2):
        first_person = row[i]
        second_person = row[i + 1]
        correct_partner = partner(first_person)
        
        if second_person != correct_partner:
            swaps += 1
            partner_index = position[correct_partner]
            
            # Swap second_person with the correct partner
            row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
            
            # Update positions in the map
            position[second_person] = partner_index
            position[correct_partner] = i + 1
    
    return swaps

#assert min_swaps([0, 2, 1, 3]) == 1
#assert min_swaps([3, 2, 0, 1]) == 0
