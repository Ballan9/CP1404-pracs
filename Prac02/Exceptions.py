finished = False
result = 0
while not finished:
    try:
        result = int(input("please enter a number"))
        finished = True
    except:
        print("Please enter a valid integer.")
print("Valid result is:", result)
