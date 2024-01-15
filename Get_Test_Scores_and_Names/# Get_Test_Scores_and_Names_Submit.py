# Get_Test_Scores_and_Names


def get_test_score(answer_sheet, student_answers):
    correct = 0
    wrong = 0
    

    for i in range(0, len(answer_sheet)):
        name = student_answers[0]
        x = answer_sheet[i]
        y = student_answers[i+1]

        
        if x == y:
            correct += 1

            

        else:
            wrong += 1
            

    
    a = correct
    b = wrong






    z = a/(a + b)
    percentage = z * 100



    return name, percentage

# from main import *

run_cases = [
    (
        [
            "A",
            "A",
            "C",
            "D",
            "D",
            "B",
            "C",
            "A",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "D",
            "C",
            "B",
            "A",
            "D",
            "A",
        ],
        [
            "Allan",
            "A",
            "C",
            "C",
            "B",
            "D",
            "B",
            "C",
            "A",
            "C",
            "B",
            "A",
            "A",
            "C",
            "B",
            "D",
            "C",
            "B",
            "A",
            "D",
            "A",
        ],
        ("Allan", 85.0),
    ),
    (
        [
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "C",
            "D",
            "A",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
        ],
        [
            "John",
            "A",
            "B",
            "A",
            "A",
            "B",
            "B",
            "A",
            "B",
            "A",
            "C",
            "D",
            "A",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
        ],
        ("John", 100.0),
    ),
]

submit_cases = run_cases + [
    (
        [
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
        ],
        [
            "Tim",
            "D",
            "D",
            "C",
            "C",
            "B",
            "B",
            "A",
            "A",
            "D",
            "D",
            "C",
            "C",
            "B",
            "B",
            "A",
            "A",
            "D",
            "D",
            "C",
            "C",
        ],
        ("Tim", 0.0),
    ),
    (
        [
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
        ],
        [
            "Sally",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
            "C",
            "C",
            "D",
            "D",
            "A",
            "A",
            "B",
            "B",
        ],
        ("Sally", 100.0),
    ),
    (
        [
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
        ],
        [
            "Jeremy",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
            "D",
            "C",
            "B",
            "A",
        ],
        ("Jeremy", 0.0),
    ),
    (
        [
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
        ],
        [
            "Jeremy",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
            "A",
            "B",
            "C",
            "D",
        ],
        ("Jeremy", 100.0),
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nanswer_sheet: {input1}\nstudent_answers: {input2}")
    print(f"Expecting: {expected_output}")
    result = get_test_score(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()




