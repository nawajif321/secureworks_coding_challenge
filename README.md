## Secureworks Coding Challenge

Author: Nawjif Hasan

--- 

## The Challenge

Your code will be evaluated on the amount of test coverage and overall general quality too include readability, following best practices for the language, etc. Your code will be evaluated by more than one person, typically the hiring manager and potential future-coworkers that all completed a coding challenge before joining the team.  Please note they will execute their review based on the instructions you provide.

We advise using these best practices for your response:

Provide working test cases
Provide full documentation of everything in your response, to include assumptions
Provide a set of instructions for the reviewers to execute their review
Confirm the program runs out of the box before sending

### The Coding Challenge:

For this challenge, you can use node js, java, python, go, or whatever language you are most comfortable with, to develop code that meets the challenge requirements listed below:

1. Read input from a file of words;
2. Find the largest word in the file
3. Transpose the letters in the largest word
4. Show the largest word and the largest word transposed 
5. Demonstrate positive and negative test cases
6. Ensure you document code and instructions for building and running based on the response best practices above

### Example file (Input Data)

```
a
ab
abc
abcd
abcde
```
### Output
```
abcde
edcba
```
---
## The Solution

This project solves the coding challenge provided by Secureworks. It has been developed using Python programming language along with some open source libraries. This consists of the below folders and files:
1. `main.py` - The script that performs the functionality
2. `files/` - The folder that contains the list of files for the input to the script and tests
3. `tests/test_main.py` - The test file that contains the tests
4. `Pipfile` - This file contains the dependancies used in the project

### Prerequisites
1. Python 3.7
2. Pip
3. Pipenv

### Next Steps...
1. Clone the repository
2. Navigate to `secureworks_coding_challenge` folder
3. Install the dependencies
    - `$ pipenv install`
4. Launch the virtualenv pipenv (optional)
    - `$ pipenv shell`

*Note*: If this step is not perfomed then all the commands below need to be appended with `$ pipenv run`
    - For example: `$ pipenv run <command>`

### Steps to run the script
- `$ python main.py <filepath>`
- For example: `$ python main.py files/wordlist.txt`
    

### Steps to run the tests
- `$ coverage run -m pytest`
- For test coverage report
    - `$ coverage report -m main.py`

### Coverage report
```
Name      Stmts   Miss  Cover   Missing
---------------------------------------
main.py      29      1    97%   38
```
