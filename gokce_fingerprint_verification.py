######################################################################
# Names of any others you worked with:
# AI transcript if used: Claude at moments I got really stuck.
# Any extensions done:
# Name: Gokce Can Ertem
######################################################################

# Function to read the file and turn it into a fingerprint
def read_and_list_fprint(filename):
    """Reads the given print and returns a dictionary with all info."""
    # Your turn!
    


    with open (filename) as fprint:
        #lines = fprint.read().strip().splitlines()
        lines = fprint.read().splitlines()
        fprint2dlist = [list(line) for line in lines]
        #print("2d List Creating")
        return(fprint2dlist)
        #print(fprint2dlist)


# Function to find the top of the fingerprint
def find_row_with_pattern(list_2d, value, count):
    """
    Find the first row in a 2D list that contains at least 'count' occurrences of 'value'.
    
    Args:
    list_2d (list): The 2D list to search.
    value: The value to search for.
    count (int): The minimum number of occurrences required.
    
    Returns:
    int: The index of the first row that matches the criteria, or -1 if not found.
    """
    for i in range(len(list_2d)):
        if list_2d[i].count(value) >= count:
            return i

# Function to check original and variant fingerprints
def simple_and_variant_check(filename1, filename2, pattern_value, pattern_count, rows_to_compare=None):
    """
    Compare two 2D lists and return the result.
    """


    #  Get 2d Lists from files
    list1 = read_and_list_fprint(filename1)
    list2 = read_and_list_fprint(filename2)



    # Get the top of the fingerprint
    start_row1 = find_row_with_pattern(list1, pattern_value, pattern_count)
    start_row2 = find_row_with_pattern(list2, pattern_value, pattern_count)
    

    # Find the end of the fingerprint
    end_row1 = start_row1 + rows_to_compare
    end_row2 = start_row2 + rows_to_compare



    total_elements = 0
    matching_elements = 0
    #compares the two lists against eachother
    for row1, row2 in zip(list1[start_row1:end_row1], list2[start_row2:end_row2]):
        # adds 1 to total elements at every step
        for item1, item2 in zip(row1, row2):
            total_elements += 1
            # adds 1 basen on matching element
            if item1 == item2:
                matching_elements += 1 
            else: 0

            
        

    # Calculates similarity percentage and prints it as string
    overall_similarity = (matching_elements / total_elements) * 100
    overall_similarity_str = f"{overall_similarity:.2f}%"

    # Returns different outcomes based on the percentage amount.
    if overall_similarity == 100.0:
        return "Identical Print. Match Percentage:", overall_similarity_str
    elif overall_similarity <= 75.0:
        return "Not Similar, cannot be the same person. Match Percentage:", overall_similarity_str
    elif 75.0 <= overall_similarity <= 88.0: 
        return "Similar but not enough to determine if same person or not. Match Percentage:", overall_similarity_str
    elif 88.0 <= overall_similarity <= 93.0: 
        return "Very similar, most likely the same person. Match Percentage:", overall_similarity_str
    else:
        return "Definitely the same person. Match Percentage:", overall_similarity_str



def shifted_check(filename1, filename2, pattern_value, pattern_count, rows_to_compare=None, max_shift=None):
    """ Compare a shifted fingerprint to another shifted or a non shifted one """


        #  Get 2d Lists from files
    list1 = read_and_list_fprint(filename1)
    list2 = read_and_list_fprint(filename2)



    # Get the top of the fingerprint
    start_row1 = find_row_with_pattern(list1, pattern_value, pattern_count)
    start_row2 = find_row_with_pattern(list2, pattern_value, pattern_count)
    

    # Find the end of the fingerprint
    end_row1 = start_row1 + rows_to_compare
    end_row2 = start_row2 + rows_to_compare



    total_elements = sum(len(row) for row in list1)
    matching_elements = 0
    #compares the two lists against eachother
    for row1, row2 in zip(list1[start_row1:end_row1], list2[start_row2:end_row2]):
        # adds 1 to total elements at every step
        for i in range(len(row1)):
            elem1 = row1[i]  # Gets the element at index i in row1
            for shift in range(-max_shift, max_shift + 1):
                
                j = i + shift  # Calculate the potential matching index in row2
                if 0 <= j < len(row2) and elem1 == row2[j]:
                    matching_elements += 1
                    break
            
        

    # Calculates similarity percentage and prints it as string
    overall_similarity = (matching_elements / total_elements) * 100
    overall_similarity_str = f"{overall_similarity:.2f}%"

    # Returns different outcomes based on the percentage amount.
    if overall_similarity == 100.0:
        return "Identical Print. Match Percentage:", overall_similarity_str
    elif overall_similarity <= 75.0:
        return "Not Similar, cannot be the same person. Match Percentage:", overall_similarity_str
    elif 75.0 <= overall_similarity <= 88.0: 
        return "Similar but not enough to determine if same person or not. Match Percentage:", overall_similarity_str
    elif 88.0 <= overall_similarity <= 93.0: 
        return "Very similar, most likely the same person. Match Percentage:", overall_similarity_str
    else:
        return "Definitely the same person. Match Percentage:", overall_similarity_str




#read_and_list_fprint(r"prints\User1_Original.txt")


#    Use for checking same or variant prints
def print_simple_or_variant_checks(file1, file2):
    print(simple_and_variant_check(file1, file2, "M", 3, 140))

print_simple_or_variant_checks((r"insert file name 1"), (r"insert file name 2"))

#    Use for checking shifted variants
def print_shifted_check(file1, file2):
    print(shifted_check(file1, file2, "M", 3, 140, 5))

print_shifted_check((r"insert file name 1"), (r"insert file name 2"))

# Sadly I dont think I have been able to make shifted variants work :(
# I will submit it like this because I am out of time but will continue working on it

#    Use for partial prints
## Wanted to do this but ran out of time so I excluded



"""""
if __name__ == '__main__':
    # Just to get you started
    data = read_print("./prints/User1_Original.txt")
    print(data)

    # Add anything else you need for testing down here as you go!
"""""