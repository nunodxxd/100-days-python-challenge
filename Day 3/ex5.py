# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score1 = 0
score2 = 0

for x in name1.lower():
    if x in "true":
        score1 +=1
    if x in "love":
        score2 +=1

for y in name2.lower():
    if y in "true":
        score1 +=1
    if y in "love":
        score2 +=1

final_score = int(str(score1) + str(score2))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")


