# Get_Test_Scores_and_Names


def get_test_score(answer_sheet, student_answers):
    correct = 0
    wrong = 0
    

    for i in range(0, len(answer_sheet)):
        name = student_answers[0]
        x = answer_sheet[i]
        y = student_answers[i+1]

        print("===============================")
        print("===============================")
        print(f"the students name is {name}")
        print(f"the answer_sheet[i] is {answer_sheet[i]}")
        print(f"the student_answer[i] is {student_answers[i+1]}")
        print("")
        print(f"the x is {x}")
        print(f"the y is {y}")
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

    return name, percentage


answer_sheet = ["A", "A", "C", "D"]
student_answers = ["John","A", "B", "C", "D"]

name, percentage = get_test_score(answer_sheet, student_answers)

print(f" Student name {name} The percentage right is {percentage}")




