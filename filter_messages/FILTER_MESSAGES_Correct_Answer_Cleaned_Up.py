# FILTER_MESSAGES_Correct_Answer_Cleaned_Up

def filter_messages(messages):
    # my_list_append = []
    my_list_join = []
    my_list_together = []
   
    my_list_count = []
    # final_message = []


    for i in range(0, len(messages)):

        words = []
        my_list_append = []
        bad_count = 0

        words = messages[i].split()

        for x in words:

            if x == "dang":
                bad_count += 1
            else:
                my_list_append.append(x)

        my_list_count.append(bad_count)

        my_list_join = " ".join(my_list_append)
       
        my_list_together.append(my_list_join)
       
    real_message = my_list_together, my_list_count
    # final_message.append(my_list_together)
    # final_message.append(my_list_count)

    return real_message

# from main import *

run_cases = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
]

submit_cases = run_cases + [
    (
        [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 2, 1, 0, 0, 0, 1],
    ),
]


def test(input, expected_output1, expected_output2):
    print("---------------------------------")
    print(f"Input:")
    print(f" * messages: {input}")
    print("Expecting:")
    print(f" * filtered messages: {expected_output1}")
    print(f" * words removed: {expected_output2}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" * filtered messages: {result[0]}")
        print(f" * words removed: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    if result == (expected_output1, expected_output2):
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
