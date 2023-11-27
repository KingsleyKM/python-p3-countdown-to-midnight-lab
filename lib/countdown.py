# your code goes here!
def countdown(x):
    while x >= 1 :
        print(f"{x} SECOND(S)!")
        x -= 1
    else :
        print("HAPPY NEW YEAR!")
countdown(10)

def countdown_with_sleep(k):
     while k >= 1 :
        print(f"{k} SECOND(S)!")
        k -= 1
     else :
        print("HAPPY NEW YEAR!")
countdown_with_sleep(10)