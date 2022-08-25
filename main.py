from art import logo,vs
from replit import clear
import random
from game_data import data
print(logo)
should_continue=True
current_score=0

#choosing values randomly from the data
def choose_one(data):
  compare=random.choice(data)
  return compare
first_one=choose_one(data)
second_one=choose_one(data)
def greater_one(data1,data2):
  print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}.")
  print(vs)
  print(f"Compare B: {data2['name']}, a {data2['description']}, from {data2['country']}.")
  question=input("Who has more followers? Type 'A' or 'B':")
  if question=="A":
    if data1["follower_count"]>data2["follower_count"]:
      return 1
    else:
      return 0
  elif question=="B":
    if data2["follower_count"]>data1["follower_count"]:
      return 1
    else:
      return 0
new_first_one=""
new_second_one=""
new_first_one=first_one
new_second_one=second_one
final_one=greater_one(new_first_one,new_second_one)

  
def repeat(final_one,new_first_one,new_second_one,should_continue,current_score):
  while should_continue:
    
    if new_first_one["name"]!=new_second_one["name"]:
      if final_one==1:
        clear()
        print(logo)
        current_score+=1
        print(f"You're right! Current score: {current_score}")
        new_first_one=new_second_one
        new_second_one=choose_one(data)
        final_one=greater_one(new_first_one,new_second_one)
        print(final_one)
      elif final_one==0:
        clear()
        should_continue=False
        print(f"Sorry, that's wrong. Final score: {current_score}")
    
      elif first_one["follower_count"]==second_one["follower_count"]:
        
          new_second_one=choose_one(data)
          final_one=greater_one(new_first_one,new_second_one)
          print(final_one)
        
        
    else:
      new_second_one=choose_one(data)
      final_one=greater_one(new_first_one,new_second_one)
      print(final_one)
        
        
check=repeat(final_one=final_one,new_first_one=new_first_one,new_second_one=new_second_one,should_continue=should_continue,current_score=current_score)


  

  

  


    