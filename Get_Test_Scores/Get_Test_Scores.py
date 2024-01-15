 # Get_Test_Scores

def get_test_score(answer_sheet, student_answers):
    correct = 0
    wrong = 0

    for i in range(0, len(answer_sheet)):
        x = answer_sheet[i]
        y = student_answers[i]

        print("===============================")
        print("===============================")

        print(f"the answer_sheet[i] is {answer_sheet[i]}")
        print(f"the student_answer[i] is {student_answers[i]}")
        print("===============================")
        print("")

        if x == y:
            correct += 1

            print("===============================")
            print("===============================")

            print(f" correct is {correct}")
            print(f" wrong is {wrong}")

            print("===============================")
            print("")


        else:
            wrong += 1
            print("===============================")
            print("===============================")

            print(f" correct is {correct}")
            print(f" wrong is {wrong}")

            print("===============================")
            print("")


    
    a = correct
    b = wrong






    z = a/(a + b)
    percentage = z * 100

    print("===============================")
    print("===============================")

    print(f" a is {a}")
    print(f" b is {b}")
    print(f" z is {z}")

    print("===============================")
    print("")

    return percentage


answer_sheet = ["A", "A", "C", "D"]
student_answers = ["A", "B", "C", "D"]

percentage = get_test_score(answer_sheet, student_answers)

print(f" The percentage right is {percentage}")



