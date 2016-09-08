# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#  print("Invalid score")
# elif score > 90:
#  result = "Excellent"
# elif score > 50:
#  result = "Passable"
# elif score < 50:
#  result = "Bad"
# print(result)

# other way to do this is
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    score = "Bad"
elif score < 90:
    score = "Passable"
else:
    score = "Excellent"
print(score)
