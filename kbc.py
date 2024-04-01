def amount(a):
    a=a+1000
    return a
q=["What is the capital bird of India ?",
   "What are the no. of players in a cricket team ?",
   "Who is known as the GOAT in football ?",
   "The Battle of Plassey was fought in ",
   "A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?",
   "Look at this series: 2, 1, (1/2), (1/4), ... What number should come next?",
   "The keyword used to transfer control from a function back to the calling function is",
   "Which of the following type of class allows only one object of it to be created?",
   "Which of the following statements is correct?",
   "Synonym of the word BRIEF is"]
p=0
print(q.pop(0))
a1=["a. Peacock","b. Humming bird","c. Pigeon"]
print(a1)
u1=input("Enter your answer :")
if u1== "a":
    print("Correct answer")
    p=amount(p)
    
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()

print(q.pop(0))
a2=["a. 11","b. 7","c. 13"]
print(a2)
u1=input("Enter your answer :")
if u1== "a":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()

print(q.pop(0))
a3=["a. L.Messi","b. C.Ronaldo","c. L.Suarez"]
u3=input("Enter your answer :")
if u3== "a":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()
    
print(q.pop(0))
a4=["a. 1757","b. 1748","c.1748"]
u4=input("Enter your answer :")
if u4== "a":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()
    
print(q.pop(0))
a5=["a. 120 metres","b. 150 metres","c. 324 metre"]
u5=input("Enter your answer :")
if u5== "b":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()

print(q.pop(0))
a6=["a. (1/3)","b. (2/8)","c. (1/8)"]
u6=input("Enter your answer :")
if u6== "c":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()

print(q.pop(0))
a7=["a. goto","b. return","c. switch"]
u7=input("Enter your answer :")
if u7== "b":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()
    
print(q.pop(0))
a8=["a. Singleton class","b. Virtual class","c. Friend class"]
u8=input("Enter your answer :")
if u8== "a":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()
    
print(q.pop(0))
a9=["a. Pointer to derived class cannot be created.","b. Base class pointer cannot point to derived class.","c. Derived class pointer cannot point to base class."]
u9=input("Enter your answer :")
if u9== "c":
    print("Correct answer")
    p=amount(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()

print(q.pop(0))
a10=["a. Little","b. Short","c. Limited"]
u10=input("Enter your answer :")
if u10== "b":
    print("Correct answer")
    print("You won the game!!")
    p=amount(p)
    print(p)
else:
    print("Sorry! You lost the game.")
    print("You have own Rs.")
    print(p)
    quit()