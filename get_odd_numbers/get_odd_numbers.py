# get_odd_numbers



def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        
        if (i % 2) != 0:
            odd_numbers.append(i)


    # don't touch below this line

    return odd_numbers


alist = 10

# alist = [(10, [1, 3, 5, 7, 9]), (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])]
          
odd_numbers = get_odd_numbers(alist)

print(f"The odd numbers are {odd_numbers}")
          