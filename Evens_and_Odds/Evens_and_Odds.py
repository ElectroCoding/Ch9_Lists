# Evens_and_Odds

def get_odds_and_evens(numbers):

    num_evens = 0
    num_odds = 0

    a = 2
    b = 0
   
    for i in numbers:
        b = i % 2
       
        if b == 0:
            num_evens += 1
        else:
            num_odds += 1
           

    # num_odds and num_evens return the individual VALUES
    # "x" returns a TUPLE
            
    x = (num_odds, num_evens)       
    
    return x, num_odds, num_evens
    
   
numbers = []

x, num_odds, num_evens = get_odds_and_evens(numbers)
print("=================================================================")
print(x)
print(f" x is a {type(x)}")
print("=================================================================")
print(f" num_odds = {num_odds} and num_evens = {num_evens}")
print(f" num_odds is a {type(num_odds)} and num_evens is a {type(num_evens)}")

print("=================================================================")
