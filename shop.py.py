shop = {
  "apple": [50,7],
  "bnanna":[60,5],
  "watermelon":[30,40],
  }

user_car = {
  "apple":0,
  "bnanna":0,
  "watermelon":0, 
}

pill=[]

print("#Welcome to ITI shop")
stat1 = True
stat2 = True
stat3 = True
#prg loop
while stat1:
 mode = int(input("#select mode\nfor customer-->1:          for owner-->2:         to exist-->0:  ")) 
 if mode==1:
  #user mood while loop
  while stat2:
   user_mode = int(input("to show our products-->1       to buy from our products-->2      to print the bill-->3  to exit-->0  "))
   if user_mode==1:
    print(shop)
   elif user_mode==2:
    add = (input("enter the element you to add"))
    user_car[add]=user_car[add]+1
    shop[add][0]=shop[add][0]-1
    pill.insert(0,shop[add][1])
   elif user_mode==3:
    print(user_car)
    total=0
    for item in pill:
     total=total+item
    print("total=",total)
   elif user_mode==0:
    stat2=False
   else:
    print("rong input") 
 
 
 #oner mode
 elif mode==2:
 #oner mood loop
  while stat3:
   owner_mode = int(input("to add new product-->1   show product press-->2   change cost-->3  exit-->0   ")) 
   if owner_mode==1:
    new_element =(input("enter element you want to add"))
    quantaty = int(input("enter quantaty of the new element you want to add"))
    cost = int(input("enter cost of the new element you want to add"))
    shop[new_element]=[quantaty,cost]
   elif owner_mode==2:
    print(shop)
   elif owner_mode==3:
    element =(input("enter element you want to shange"))
    prize = int(input("enter new prize"))
    shop[element]=prize
   elif owner_mode==0:
    stat3=False
   else:
    print("rong input")  
 elif mode==0:
  stat1=False
 else:
  print("rong input")
	
	
	
