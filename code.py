# 20-Questions
#first question
q1= raw_input("Is it on the floor")
#continuation for first quesion "yes" answers
if 'yes' in q1:
  print("It is on floor")
if 'yes' in q1:
  q2a =raw_input("Is it smooth")
#continuation for first quesion "no" answers
if 'no' in q1:
  print("It is not on the floor")
if 'no' in q1:
  q2b=raw_input("Is it on the wall?")
#continuation for second quesion "yes yes" answers
if 'yes' in q2a:
  print("It is smooth")
if 'yes' in q2a:
    q3a=raw_input("Is it floor?")
#continuation for second quesion "yes no" answers
if 'no' in q2a:
  print("It is not smooth")
if 'no' in q2a:
  	q3b=raw_input("Is it electronic?")
#continuation for second quesion "no yes" answers
if 'yes' in q2b:
  print("It is on wall")
if 'yes' in q2b:
  	q3c=raw_input("Is it a poster?")
#continuation for second quesion "no no" answers
if 'no' in q2b:
  print("It is not on wall")
if 'no' in q2b:
  	q3d=raw_input("Is it on the ceiling?")
#continuation for third question "yes yes yes"
if 'yes' in q3a:
  print("It is floor, floor is good")
#continuation for third question "yes yes no"
if 'no' in q3a:
  print("It must be desk,then...")
#continuation for third question "yes no yes"
if 'yes' in q3b:
  print("It is computer, yes?, everthing electronic is computer")
#continuation for third question "yes no no"
if 'no' in q3b:
  print("I dont know, lot of non-smooth and non-electronic things, not have enough time to code in")
#continuation for third question "no yes yes"
if 'yes' in q3c:
  	q3c=raw_input("Poster show great many things, so guess is good right?")
#continuation for third question "no yes no"
if 'no' in q3c:
  	q3c=raw_input("If poster not on wall, what is? Nail, cabniet, hole?; they not matter, poster matters")
#continuation for third question "no no yes"
if 'yes' in q3d:
  	q3d=raw_input("If on ceiling, then it must be light!")
#continuation for third question "no no no"
if 'no' in q3d:
  	q3d=raw_input("So it is not on celing, wall, or celing, where is it?; Your item must be invisible...")
else:
  raw_input("you silly goose!, it is yes or no question!")
