import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to check for the function 'score_input'
def test_score_input_function():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    function_def = any(isinstance(node, ast.FunctionDef) and node.name == 'score_input' for node in ast.walk(tree))
    assert function_def, "DMACC Student, there does not appear to be a function named 'score_input' in your code. Please create a function named 'score_input'."

# Test to check if 'score_input' function has a reST style docstring
def test_score_input_function_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'score_input':
            docstring = ast.get_docstring(node)
            assert docstring is not None, "DMACC Student, the function 'score_input' does not have a docstring. Please add a reST style docstring to the function."
            assert ":param" in docstring and ":returns:" in docstring, "DMACC Student, the function 'score_input' docstring does not follow the reST style guide. Please ensure it includes ':param' and ':returns:'."

# Individual test cases for 'score_input' function
def test_score_input_case_1():
    from assignment import score_input
    result = score_input('Test 1', 70)
    expected = 'Test 1: 70'
    assert result == expected, f"DMACC Student, the function 'score_input' did not return the expected value for inputs ('Test 1', 70). Expected '{expected}', but got '{result}'."

def test_score_input_case_2():
    from assignment import score_input
    result = score_input('Test 1')
    expected = 'Invalid test score!'
    assert result == expected, f"DMACC Student, the function 'score_input' did not return the expected value for inputs ('Test 1'). Expected '{expected}', but got '{result}'."

def test_score_input_case_3():
    from assignment import score_input
    result = score_input('Test 1', -70)
    expected = 'Invalid test score!'
    assert result == expected, f"DMACC Student, the function 'score_input' did not return the expected value for inputs ('Test 1', -70). Expected '{expected}', but got '{result}'."

def test_score_input_case_4():
    from assignment import score_input
    result = score_input('Test 1', 101)
    expected = 'Invalid test score!'
    assert result == expected, f"DMACC Student, the function 'score_input' did not return the expected value for inputs ('Test 1', 101). Expected '{expected}', but got '{result}'."

def test_score_input_case_5():
    from assignment import score_input
    result = score_input('Test 1', 101, "There is no extra credit!")
    expected = 'There is no extra credit!'
    assert result == expected, f"DMACC Student, the function 'score_input' did not return the expected value for inputs ('Test 1', 101, 'There is no extra credit!'). Expected '{expected}', but got '{result}'."

def test_score_input_case_6():
    from assignment import score_input
    result = score_input('Test 1', "Seventy")
    expected = 'Invalid test score!'
    assert result == expected, f"DMACC Student, the function 'score_input' did not return the expected value for inputs ('Test 1', 100). Expected '{expected}', but got '{result}'."

if __name__ == "__main__":
    pytest.main()