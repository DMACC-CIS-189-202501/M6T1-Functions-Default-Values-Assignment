# TODO 1: Add your DocString Here


# TODO 2: Modify score_input to have 3 parameters; test_name, test_score, and invalid_message
# Note: see README.md for requirements; test_score and invalid_message should ahve default values
def score_input():
    """
    Process the test score for a given test.

    :param test_name: Required parameter. No validation needed.
    :type test_name: str
    :param test_score: Optional parameter. Default value is -1. This should have validation that the value is between 0 and 100 inclusive, else it will return invalid_message.
    :type test_score: int, optional
    :param invalid_message: Optional parameter with default value of 'Invalid test score!'. The return should be a string.
    :type invalid_message: str, optional
    :return: A string indicating the validity of the test score.
    :rtype: str
    """

    # TODO 3: Try to cast test_score to an int. Then validate if that int is in the range 0 to 100

    # TODO 4: if it can be cast to an int, and is in the proper range, return a string in
    # the format "{test_name}: {test_score}"

    # TODO 5: else if it failed to cast to an int, or is not in the range, return a string in
    # the format "{invalid_message}"

    # TODO 6: Delete this comment and the below pass
    pass

if __name__ == "__main__":

    #Note: You can comment out and uncomment these as needed.
    #Note 2: Hold/hover your mouse over score_input to view the reST style documentation.

    #Test Case 1
    display_string = score_input('Test 1', 70) # function call, returned value stored as a variable; params are Input below
    print(display_string) #printing the returned string; printed output should match expected output

    #Test Case 2
    #display_string = score_input('Test 1')
    #print(display_string)
    
    #Test Case 3
    #display_string = score_input('Test 1', -70)
    #print(display_string)

    #Test Case 4
    #display_string = score_input('Test 1', 101)
    #print(display_string)

    #Test Case 5
    #display_string = score_input('Test 1', 101, "There is no extra credit!")
    #print(display_string)

    #Test Case 6
    #display_string = score_input('Test 1', "Seventy")
    #print(display_string)