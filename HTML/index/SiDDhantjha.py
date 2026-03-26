total=0
print("------------------------------------Welcome to Ambience-----------------------------------")
print("******************************************************************************************")
print("                               Our Dishes/FOOD ITEMS/CHICKEN                              ")
print("------------------------------------------------------------------------------------------")
print("1:Idli Sambar                                                    Rs. 60/Plate")
print("2:Kadhai Paneer                                                   Rs. 150/PLate")
print("3:Butter Chicken                                                    Rs. 250/6 Pieces")
print("4:Kadhai Chicken                                                   Rs. 150/3 Pieces")
print("5:Dosa                                                              Rs. 20/Plate")
menuChoice  = {1:"Idli Sambar",2: "Kadhai Paneer", 3:"Butter Chicken", 4:"Kadhai Chicken", 5:"Dosa"}
while True:
    choice=eval(input("Aap kya khana pasand karenge?:"))
    if(choice == 1):
        print(f"Aapne chuna hai: {menuChoice.get(choice, "Kuch Nahi")}")
        quantity = int(input("Kitna khana cahenge:  "))
        total = quantity * 60
    elif(choice == 2):
        print(f"Aapne chuna hai: {menuChoice.get(choice, "Kuch Nahi")}")
        quantity = int(input("Kitna khana cahenge: "))
        total=quantity * 150
    elif(choice == 3):
        print(f"Aapne chuna hai: {menuChoice.get(choice, "Kuch Nahi")}")
        quantity=int(input("Kitna khana cahenge: "))
        total=quantity * 250
    elif(choice==4):
        print(f"Aapne chuna hai: {menuChoice.get(choice, "Kuch Nahi")}")
        quantity=int(input("Kitna khana cahenge: "))
        total=quantity*150
    elif(choice==5):
        print(f"Aapne chuna hai: {menuChoice.get(choice, "Kuch Nahi")}")
        quantity=int(input("Kitna khana cahenge: "))
        total=quantity*20
    elif(choice=="nahi"):
        break
    
    
    print("Kya aap kuch aur lena chahenge? ")
    total += total
    print("Aap ko dena padega:",total)