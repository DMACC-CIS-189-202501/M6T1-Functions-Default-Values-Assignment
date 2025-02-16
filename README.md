# M6 T1: Functions Default Values Assignment

## Instructions for students

- Implement your solutions in `assignment.py`
- The tests in `test_assignment.py` can be inspected but do not modify them

### Directions - Copy/Pasted from Canvas

* Write a function named ```score_input``` that takes the parameteres: ```test_name```, ```test_score```, and ```invalid_message```
* The function will validate the test score, then return a string

| Parameter | Requirement |
| ---- | ---- |
| ```test_name``` | Required parameter. No validation needed. |
| ```test_score``` | Optional parameter. Default value that is negative, eg -1. This should have validation that the valuie is between 0 and 100 inclusive, else it will return invalid_message|
| ```invalid_message``` | Optional, with default value of 'Invalid test score!'. |

### Example Input and Output

Calling the function may look like:
~~~python
if __name__ == "__main__":
    display_string = score_input('Test 1', 70) # function call, returned value stored as a variable; params are Input below
    print(display_string) #printing the returned string; printed output should match expected output
~~~

| Input | Expected Output | Note |
| ---- | ---- | ---- |
| 'Test 1', 70 | ```Test 1: 70``` | Test name, and a score between 0 and 100 |
| 'Test 1' | ```Invalid test score!``` | Only a test name, so invalid_message and test_score are their defaults, since test_score defaults to -1 it prionts the default invalid_message. |
| 'Test 1', -70| ```Invalid test score!``` | Score is not in 0 to 100 range (below), so it prints the default invalid_message. |
| 'Test 1', 101| ```Invalid test score!``` | Score is not in 0 to 100 range (above), so it prints the default invalid_message. |
| 'Test 1', 101, "There is no extra credit!"| ```There is no extra credit!``` | Score is not in 0 to 100 range (above), so it prints the invalid_message; which was passed in as a string. |
| 'Test 1', "Seventy" | ```Invalid test score!``` | Make sure you account for non-numeric input. You could use a Try Catch. |