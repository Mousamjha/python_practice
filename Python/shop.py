import time

print("---------------------------------- 2nd Hand Shop ---------------------------------------")
print("****************************************************************************************")
print("                                      Shop Items                                        ")
print("----------------------------------------------------------------------------------------")
print("Sab par 50% DISCOUNT!")
print("1: Red & Black scissors                                                      Rs. 10")
print("2: Pack of Envelopes                                                         Rs. 5 Per Piece")
print("3: iPhone 14 cover 'black'                                                   Rs. 30")
print("4: iPhone 14 cover                                                           Rs. 30")
print("5: Hornbill Wallet                                                           Rs. 100")
print("6: Apple AirPods cover                                                       Rs. 20")
print("7: iPhone 15 cover Tom and Jerry                                             Rs. 50")
print("8: Bottle opener                                                             Rs. 10")     
print("9: Keyboard Mouse Combo (RGB)                                                Rs. 500")
print("10: Stapler Pins                                                             Rs. 30")
print("11: Stapler                                                                  Rs. Free With Pin")
print("12: Raymond Limited Edition Wallet                                           Rs. 500")

# Price dictionary
prices = {
    1: 10,
    2: 5,
    3: 30,
    4: 30,
    5: 100,
    6: 20,
    7: 50,
    8: 10,
    9: 500,
    10: 30,
    12: 500
}

# Menu dictionary
menu = {
    1: "Red & Black scissors",
    2: "Pack of Envelopes",
    3: "iPhone 14 cover 'black'",
    4: "iPhone 14 cover",
    5: "Hornbill Wallet",
    6: "Apple AirPods cover",
    7: "iPhone 15 cover Tom and Jerry",
    8: "Bottle opener",
    9: "Keyboard Mouse Combo (RGB)",
    10: "Stapler Pins",
    11: "Stapler",
    12: "Raymond Limited Edition Wallet"
}

total = 0
first_time = True  # Flag to know if it's the first question

while True:
    if first_time:
        choice_input = input("Aap kya lena pasand karenge?: ").strip().lower()
        first_time = False
    else:
        choice_input = input("Kya aap aur kuch lena pasand karenge?: ").strip().lower()
    
    if choice_input == "nahi":
        break
    
    if not choice_input.isdigit():
        print("❌ Kripya valid item number dijiye.")
        continue
    
    choice = int(choice_input)

    if choice not in menu:
        print("❌ Yeh item hamare paas nahi hai.")
        continue

    print(f"✅ Aapne choose kiya: {menu[choice]}")

    if choice == 11:
        print("🎁 Yeh item FREE hai Stapler Pins ke saath!")
        continue

    quantity = input("Kitne pieces chahiye?: ").strip()
    
    if not quantity.isdigit():
        print("❌ Kripya valid quantity dijiye.")
        continue
    
    quantity = int(quantity)
    price = prices[choice]
    total += price * quantity
    print(f"💰 Is item ka total: Rs. {price * quantity}")
    print(f"📦 Abhi tak ka bill: Rs. {total}")

print(f"\n🛒 Aapka final total hai: Rs. {total}")

bill_paid = input("Kya aapne bill pay kar diya? (haan/nahi): ").strip().lower()
if bill_paid == "haan":
    print("🙏 Dhanyavaad! Aapka din shubh ho!")
else:
    print("⚠️ Kripya bill pay kijiye.")
    confirm_payment = input("Kya aap abhi pay karna chahenge? (haan/nahi): ").strip().lower()
    if confirm_payment == "haan":
        print("🙏 Dhanyavaad! Aap jaa sakte hain wapis zarur aana.")
    else:
        print("\n📞 Police ko bula rahe hain...")
        time.sleep(2)
        print("🚨 Police raste me hai......")
        time.sleep(2)
        print("peo peo peo peo peo peo peo peo peo peo")

        # Police arrives and conversation starts
        print("\n🚔 Police: Yaha kya ho raha hai?")
        time.sleep(1)
        print("🛍️ Dukandaar: Saab, yeh aadmi apna bill pay nahi kar raha hai.")
        time.sleep(1)
        print("🚔 Police: Aap, kya aap is baat ko kabool karte hain?")

        while True:
            print("\n🧍 Customer, aap kya kahenge?")
            print("1: Haan, main abhi pay nahi kar paya.")
            print("2: Nahi, main ne sab pay kar diya tha.")
            print("3: Main kuch nahi kehna chahta.")
            response = input("Apna option chuniye (1/2/3): ").strip()

            if response == "1":
                print("\n🧍 Customer: Haan, main abhi pay nahi kar paya.")
                time.sleep(1)
                print("🚔 Police: Kya aap turant payment kar sakte hain?")
                time.sleep(1)
                while True:
                    print("\n1: Haan, main abhi pay karta hoon.")
                    print("2: Nahi, mere paas paise nahi hain.")
                    pay_now = input("Apna option chuniye (1/2): ").strip()

                    if pay_now == "1":
                        print("\n🧍 Customer: Haan, main abhi pay karta hoon.")
                        time.sleep(1)
                        print("🛍️ Dukandaar: Shukriya, aapka swagat hai phir se.")
                        time.sleep(1)
                        print("🚔 Police: Theek hai, aapko chhod dete hain. Agli baar dhyaan rakhein.")
                        time.sleep(1)
                        print("\n✅ Aapko jail nahi jana pada. Dhanyavaad!")
                        break

                    elif pay_now == "2":
                        print("\n🧍 Customer: Nahi, mere paas paise nahi hain.")
                        time.sleep(1)
                        print("🚔 Police: Yeh kanuni mamla hai. Aapko police station jaana hoga.")
                        time.sleep(1)
                        print("🛍️ Dukandaar: Dhanyavaad Saab.")
                        time.sleep(1)
                        print("🚔 Police: Chaliye, Police station chalte hain.")
                        time.sleep(1)
                        print("\n⛓️ Aapko jail bhej diya gaya.")
                        break
                    else:
                        print("❌ Kripya valid option chuniye: 1 ya 2.")
                break

            elif response == "2":
                print("\n🧍 Customer: Nahi, main ne sab pay kar diya tha.")
                time.sleep(1)
                print("🚔 Police: Kya aapke paas koi saboot hai?")
                time.sleep(1)
                while True:
                    print("\n1: Haan, mere paas receipt hai.")
                    print("2: Nahi, receipt nahi hai.")
                    proof = input("Apna option chuniye (1/2): ").strip()

                    if proof == "1":
                        print("\n🧍 Customer: Haan, mere paas receipt hai.")
                        time.sleep(1)
                        print("🚔 Police: Achha, dikhaiye toh.")
                        time.sleep(1)
                        print("🧍 Customer: (receipt dikhata hai)")
                        time.sleep(1)
                        print("🚔 Police: Yeh saboot theek lagta hai. Aapko chhod dete hain.")
                        time.sleep(1)
                        print("🛍️ Dukandaar: Maaf kijiye, galti ho gayi.")
                        time.sleep(1)
                        print("\n✅ Aapko jail nahi jana pada. Dhanyavaad!")
                        break

                    elif proof == "2":
                        print("\n🧍 Customer: Nahi, receipt nahi hai.")
                        time.sleep(1)
                        print("🚔 Police: Bina saboot ke aapko police station jaana hoga.")
                        time.sleep(1)
                        print("🛍️ Dukandaar: Dhanyavaad Saab.")
                        time.sleep(1)
                        print("🚔 Police: Chaliye, Police station chalte hain.")
                        time.sleep(1)
                        print("\n⛓️ Aapko jail bhej diya gaya.")
                        break
                    else:
                        print("❌ Kripya valid option chuniye: 1 ya 2.")
                break

            elif response == "3":
                print("\n🧍 Customer: Main kuch nahi kehna chahta.")
                time.sleep(1)
                print("🚔 Police: Aapka yeh atteet bahut ghamandi lag raha hai. Aapko police station le jaana hoga.")
                time.sleep(1)
                print("🛍️ Dukandaar: Dhanyavaad Saab.")
                time.sleep(1)
                print("🚔 Police: Chaliye, Police station chalte hain.")
                time.sleep(1)
                print("\n⛓️ Aapko jail bhej diya gaya.")
                break

            else:
                print("❌ Kripya valid option chuniye: 1, 2 ya 3.")