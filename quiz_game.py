import pyttsx3

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

wlcom = 'Welcome to my computer Quiz game'
print(wlcom)
talk(wlcom)

talk('Do you want to play? please type.')
playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Ok! Lets play")
talk("Ok! let's play")
score = 0

q1 = "What does CPU stands for?"
print(q1)
talk(q1)
ans = input("Type answer: ")
if ans.lower() == 'central processing unit':
    print("It's correct.")
    talk("It's Correct.")
    score += 1
else:
    print("It's not correct.")
    talk("It's not correct.")

q2 = "What does RAM stands for?"
print(q2)
talk(q2)
ans = input("Type answer: ")
if ans.lower() == 'random access memory':
    print("It's correct.")
    talk("It's Correct.")
    score += 1
else:
    print("It's not correct.")
    talk("It's not correct.")


q3 = "What does GPU stands for?"
print(q3)
talk(q3)
ans = input("Type answer: ")
if ans.lower() == 'graphic processing unit':
    print("It's correct.")
    talk("It's Correct.")
    score += 1
else:
    print("It's not correct.")
    talk("It's not correct.")


q4 = "What does PNG stands for?"
print(q4)
talk(q4)
ans = input("Type answer: ")
if ans.lower() == 'portable network graphics':
    print("It's correct.")
    talk("It's Correct.")
    score += 1
else:
    print("It's not correct.")
    talk("It's not correct.")


q5 = "What does NFT stands for?"
print(q5)
talk(q5)
ans = input("Type answer: ")
if ans.lower() == 'non fungible token':
    print("It's correct.")
    talk("It's Correct.")
    score += 1
else:
    print("It's not correct.")
    talk("It's not correct.")

cong = f'Congratulation, you got {score} scores.'
print(cong)
talk(cong)
percent = (score/5) * 100
result = f'Your percentage is {percent}%.'
print(result)
talk(result)