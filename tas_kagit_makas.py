import random

print("*****taş-kağıt-makas oyunu*****\n\n")

user_score, computer_score = 0, 0

while True:
    print("\n1-) Taş\n2-) Kağıt\n3-) Makas\n")
    user_choice=input("->Bir seçim yapın (oyunu bitirmek için 0'a basın):")
    computer_choice=random.choice(["1", "2", "3"])

    if user_choice == "1":
        if computer_choice == "1":
            print("\nBilgisayarın seçimi: Taş\nBerabere!")
        
        elif computer_choice == "2":
            print("\nBilgisayarın seçimi: Kağıt\nKağıt taşı yener. Bigisayar kazandı!")
            computer_score+=100
        
        elif computer_choice == "3":
            print("\nBilgisayarın seçimi: Makas\nTaş makası yener. Sen kazandın!")
            user_score+=100
    elif user_choice == "2":
        if computer_choice == "1":
            print("\nBilgisayarın seçimi: Taş\nKağıt taşı yener. Sen kazandın!")
            user_score+=100
        
        elif computer_choice == "2":
            print("\nBilgisayarın seçimi: Kağıt\nBerabere!")
        
        elif computer_choice == "3":
            print("\nBilgisayarın seçimi: Makas\nMakas kağıtı yener. Bilgisayar kazandı!")
            computer_score+=100
    
    elif user_choice == "3":
        if computer_choice == "1":
            print("\nBilgisayarın seçimi: Taş\nTaş makası yener. Bigisayar kazandı!")
            computer_score+=100
        
        elif computer_choice == "2":
            print("\nBilgisayarın seçimi: Kağıt\nMakas kağıdı yener. Sen kazandın!")
            user_score+=100
        
        elif computer_choice == "3":
            print("\nBilgisayarın seçimi: Makas\nBerabere!")
    elif user_choice > "3" or user_choice < "0":
        print("yanlış seçim, tekrar deneyin!\n")
    elif user_choice=="0":
        print("oyun bitti!\n") 
        break

print('senin skorun: ' + str(user_score) + '\nBilgisayarın skoru: ' + str(computer_score))
int(user_score)
int(computer_score)

if user_score > computer_score:
    print("\nSEN KAZANDIN")

elif computer_score > user_score:
    print("\nBİLGİSAYAR KAZANDI")

else:
    print("\nBERABERE")

    





    

