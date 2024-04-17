import random,time,sys
import mysql.connector

instruction='''INSTRUCTIONS: You can play as Son Goku in Dragon Ball Z- Son Goku. Even though, the main character is Goku, but you can play as other characters like Vegeta, Gohan or Piccolo in certain sagas.

1) Power levels - You are already given a power level of 1000 which can be increased through training. 
2) Tokens - You are already given 100 tokens which can either be lost or won by fighting opponents by losing or winning respectively , the magnitude of the tokens lost or won is directly proportional to the difficulty the opponents offer.
3) Health - You are already given a health of 100 points. During battles, you will only lose health and if your health reaches 0, you lose. But you can increase your health by eating Chi Chi's homemade warm food :)
4) Meal - Chi Chi has already packed you 100 meals. Just as tokens, you can use them to increase your health, but they can be lost or won if you lose or win in battles respectively. The magnitude of meals won or lost is directly proportional to the difficulty the opponents offer.
5)Dragon Balls - Mystical orbs from which we can wish for any thing. You have to collect all seven of them to summon a magical dragon - Shenron.
6)Zenkai Awakening - Saiyans have a tendency to get stronger with each near-death battle they fight. If your health is 10 points or less, then you will get a 90% boost in your power level.

It will be advisable to remember your directory number. Your game will not be saved if the directory number you entered will be same as any other in the database.

After deleting a saved file when the game asks you for your directory number, enter the directory number of the file you just deleted, otherwise it will lead to you losing progress in your other files.

MOST IMPORTANT INSTRUCTION! Have fun :)
'''

power_level=1000 

tokens=100 

health=100 

meal=100 

dragon_balls=0

password=input("Enter your MySQL password:")

def showall():
    db=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
    cur=db.cursor()
    cur.execute("SELECT * FROM DBZ_FILES")
    for i in cur:
        print(i)

def print_slow(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0125)
    print()
    
def villain_stats():
    lis=[["Saiyan","Raditz",1500],["Saiyan","Nappa",4000],["Saiyan","Vegeta",18000],["Frieza","Guldo",11500],["Frieza","Recoome",71000],["Frieza","Jeice",45000],["Frieza","Burter",70000],["Frieza","Captain Ginyu",120000],["Frieza","Lord Frieza",120000000],["Android","Android 19",157000000],["Android","Android 20",128000000],["Android","Android 18",280000000],["Android","Android 17",320000000],["Android","Android 16",440000000],["Cell","1st Form Cell",250000000],["Cell","2nd Form Cell",450000000],["Cell","Super Perfect Cell",5000000000],["Buu","Super Saiyan Majin Vegeta",3000000000],["Buu","Majin Buu",10000000000],["Buu","Evil Majin Buu",5200000000],["Buu","Super Buu",32000000000],["Buu","Super Buu (SS3 Gotenks & Piccolo Absorbed)",74150000000],["Buu","Super Buu (Gohan, Trunks, Goten & Piccolo Absorbed)",80250000000],["Buu","Kid Buu",22000000000]]
    print()
    print_slow("Press 1 to show the stats for the Saiyan Saga.")
    print_slow("Press 2 to show the stats for the Frieza Saga.")
    print_slow("Press 3 to show the stats for the Android Saga.")
    print_slow("Press 4 to show the stats for the Cell Saga.")
    print_slow("Press 5 to show the stats for the Buu Saga.")
    print()
    try:
        ques=int(input("Which saga do you want to choose:"))
    except ValueError:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        print()
        lis1=["Saga","Villain Name","Power Level"]
        print_slow(str(lis1))
        if ques==1:
            for i in range(len(lis)):
                if lis[i][0]=="Saiyan":
                    print(lis[i])
                else:
                    pass
        elif ques==2:
            for i in range(len(lis)):
                if lis[i][0]=="Frieza":
                    print(lis[i])
                else:
                    pass
        elif ques==3:
            for i in range(len(lis)):
                if lis[i][0]=="Android":
                    print(lis[i])
                else:
                    pass
        elif ques==4:
            for i in range(len(lis)):
                if lis[i][0]=="Cell":
                    print(lis[i])
                else:
                    pass
        elif ques==5:
            for i in range(len(lis)):
                if lis[i][0]=="Buu":
                    print(lis[i])
                else:
                    pass
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")

def Narrator(char,name):
    print_slow(f"At last {char} has decided to fight {name}. With his new power, he seems to be of almost equal standing as his adversary, but will he win and save the world once again? FIND OUT IN THE NEW EXCITING EPISODE OF DRAGON BALL Z TODAY! ")

def train():
    print()
    print_slow("Press 1 to use all of your tokens to train.")
    print_slow("Press 2 to use a specific amount of tokens to train.")
    print()
    ques=int(input("Do you want to use all of your tokens or specific tokens:"))
    global tokens
    if ques==1:
        for i in range(tokens):
            global power_level
            power_level+=10000
        print_slow(f"Goku after training day-in and day-out has achieved a new awesome power-level of {power_level}")
        tokens=0
        print("You have 0 tokens left")
    elif ques==2:
        try:
            n=int(input("Enter the number of tokens you want to use:"))
        except ValueError:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
        else:
            if n>0 and n<=tokens:
                for i in range(n):
                    power_level+=10000
                    tokens-=1
                print_slow(f"Goku after training day-in and day-out has achieved a new awesome power-level of {power_level}")
                print(f"You have {tokens} left.")
            else:
                print_slow("Number of tokens cannot be 0 or negative.")
    else:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")

def heal():
    global health
    print()
    if health==100:
        print_slow(f"Goku is already at his maximum, now go fight someone.")
    else:
        print_slow("Press 1 to heal Goku with all of your meals.")
        print_slow("Press 2 to heal Goku using a specific amount of meals")
        print()
        ques=int(input("Do you want to use all of your meal or specific number of meals:"))
        global meal
        if ques==1:
            for i in range(meal):
                health+=10
            meal=0
            print("You have 0 meals left")
        elif ques==2:
            try:
                n=int(input("Enter the number of meals you want to use:"))
            except ValueError:
                print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
            else:
                if n>0 and n<=meal:
                    for i in range(n):
                        meal-=1
                        health+=10
                    print(f"You have {meal} left.")
                else:
                    print_slow("Number of meals cannot be 0 or negative.")
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    if health>100:
        health=100
        print_slow(f"Goku after eating Chi Chi's home-made food, feels a lot stronger and now his health is {health}")
    elif health>0 and health <=100:
        print_slow(f"Goku after eating Chi Chi's home-made food, feels a lot stronger and now his health is {health}")
    else:
        pass    

def result(rel):
    print("Power-level, token, health and meal are in the order of:",rel)
    
def dragonballs():
    global dragon_balls
    print()
    if 0<=dragon_balls<7:
        ques=input("Would you like to collect them (yes/no):")
        if ques.lower()=="yes":
            people=["Goku","Bulma","Gohan","Vegeta","Master Roshi","Tien","Yamcha"]
            places=["Goku's house","Kami lookout","Kame House","Korin Tower","Central City","East City","Gingertown"]
            for i in range(1,8):
                person=random.choice(people)
                place=random.choice(places)
                print_slow(f"{person} found {i} star(s) dragon ball in {place}")
                time.sleep(5)
                dragon_balls+=1
        elif ques.lower()=="no":
            print_slow("'See you and take care'- Goku")
            exit()
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        print_slow("You already have the dragon balls.")
    
def shenron():
    global dragon_balls
    print()
    if dragon_balls==7:
        print_slow("Press 1 to wish for 100 tokens")
        print_slow("Press 2 to wish for 100 meals")
        print()
        ques=int(input("State your wish:"))
        if ques==1:
            global tokens
            tokens+=100
            dragon_balls=0
            print_slow("Your wish has been granted.")
        elif ques==2:
            global meal
            meal+=100
            dragon_balls=0
            print_slow("Your wish has been granted.")
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        print_slow("You have to collect dragon balls.")

def health_text(char,name):
    print_slow(f"While fighting {name}, {char} by performing his final attack to defeat his enemy, lost his life. His friends arrange a funeral for him.")

def database_and_table():
    print_slow("Please install MySQL for saving and loading the game.")
    db=mysql.connector.connect(host="localhost",user="root",passwd=password)
    cur=db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS DBZ")
    db.commit()
    db1=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
    cur1=db1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS DBZ_Files (power_levels bigint, tokens bigint, health bigint, meals bigint,dragon_balls int(1), direc_num int(1) PRIMARY KEY)")
    db.commit()
    
def insert():
    db=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
    cur=db.cursor()
    ques=input("Is this your first saved file (yes/no):")
    if ques.lower()=="yes":
        num=int(input("Enter directory number (eg. 1,2,3) for uniquely saving the file:"))
        query = "INSERT INTO DBZ_Files VALUES (%s, %s, %s, %s, %s, %s)"
        values = (power_level, tokens, health, meal, dragon_balls,num)
        cur.execute(query, values)
        db.commit()
        print_slow("Saved successfully!")
        exit()
    elif ques.lower()=="no":
        db1=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
        cur1=db1.cursor()
        num1=int(input("Enter directory number (eg. 1,2,3) for uniquely saving the file:"))
        cur1.execute("Select * from dbz_files")
        lis=[]
        lis_num=[]
        for i in cur1:
            lis.append(i)
        for i in range(len(lis)):
            lis_num.append(lis[i][-1])
        if num1 in lis_num:
            print_slow("Directory number cannot be same.")
            exit()
        else:
            query = "INSERT INTO DBZ_Files VALUES (%s, %s, %s, %s, %s, %s)"
            values = ( power_level, tokens, health, meal, dragon_balls,num1)
            cur.execute(query, values)
            db.commit()
            print_slow("Saved successfully!")
            exit()
    else:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
        
def load():
    db=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
    cur=db.cursor()
    cur.execute("select * from DBZ_Files")
    for i in cur:
        print(i)
        ques=input("Is this your saved file (yes/no):")
        if ques.lower()=="yes":
            global power_level
            power_level=i[0]
            global tokens
            tokens=i[1]
            global health
            health=i[2]
            global meal
            meal=i[3]
            global dragon_balls
            dragon_balls=i[4]
            main()
            db1=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
            cur1=db1.cursor()
            query="UPDATE DBZ_Files set power_levels=%s, tokens=%s, health=%s,meals=%s, dragon_balls=%s where direc_num=%s"
            num=int(input("Enter your directory number:"))
            values=(power_level,tokens,health,meal,dragon_balls,num)
            cur1.execute(query,values)
            db1.commit()
        elif ques.lower()=="no":
            continue
        else:
            pass
   
def delete(num):
    db=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
    cur=db.cursor()
    query="DELETE FROM DBZ_FILES WHERE direc_num=%s"
    value=(num,)
    cur.execute(query,value)
    db.commit()
    print_slow("Saved deleted successfully.")
    
def main():
    print()
    print_slow("Press 1 to train Goku.")
    print_slow("Press 2 to fight as Goku.")
    print_slow("Press 3 to heal Goku.")
    print_slow("Press 4 to collect dragon balls.")
    print_slow("Press 5 to summon Shenron.")
    print_slow("Press 6 to show stats.")
    print_slow("Press 7 to see all the saved games.")
    print_slow("Press 8 to delete a saved file.")
    print_slow("Press 9 to exit.")
    print()
    ques=int(input("What do you want to do first:"))
    if ques==1:
            train()
    elif ques==2:
            fight()
    elif ques==3:
            heal()
    elif ques==4:
            dragonballs()
    elif ques==5:
            shenron()
    elif ques==6:
            print()
            print_slow("Press 1 to show your stats.")
            print_slow("Press 2 to show villain stats.")
            print()
            try:
                ques1=int(input("Which stats do you want to see:"))
            except ValueError:
                print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
            else:
                if ques1==1:
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                elif ques1==2:
                    villain_stats()
                else:
                    print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    elif ques==7:
        showall()
    elif ques==8:
            n=int(input("Enter the directory number you want to delete:"))
            db1=mysql.connector.connect(host="localhost",user="root",passwd=password,database="DBZ")
            cur1=db1.cursor()
            cur1.execute("Select * from dbz_files")
            lis=[]
            lis_num=[]
            for i in cur1:
                lis.append(i)
            for i in range(len(lis)):
                lis_num.append(lis[i][-1])
            if n in lis_num:
                ques1=input("Are you sure you want to delete the file (yes/no):")
                if ques1.lower()=="yes":
                    print_slow("Very well.")
                    delete(n)
                elif ques1.lower()=="no":
                    print_slow("Alright.")
                    pass
                else:
                    print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
            else:
                print_slow("No such directory found.")
    elif ques==9:
            print_slow("'See you and take care'- Goku")
            exit()
    else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")

def saiyan():
    print_slow("The remaining saiyans have arrived to Earth in search for the mystical Dragon Balls. Now it is upto Goku to defeat them, is he strong enough? FIND OUT TODAY")
    print()
    print_slow("Press 1 for Raditz - Kakarot's elder brother.")
    print_slow("Press 2 for Nappa - A saiyan tank.")
    print_slow("Press 3 for Vegeta - The Prince of all Saiyans.")
    print()
    try:
        opp=int(input("Which opponent do you want to choose:"))
        print()
    except ValueError:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        if opp==1:
            Narrator("Goku","Raditz")
            power_rad=1500
            global power_level
            if power_level>power_rad:
                print_slow("Kakarot was able to defeat his elder brother in an epic showdown.")
                global tokens
                tokens+=1
                global health
                health-=10
                global meal
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Raditz")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
            elif power_rad>power_level:
                print_slow("Raditz was able to teach his younger brother a lesson. He defeated Kakarot badly.")
                tokens-=1
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                health_text("Goku","Raditz")
                print("You lost.")
            else:
                print_slow("The brothers ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                health-=10
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Raditz")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
        elif opp==2:
            Narrator("Goku","Nappa")
            power_nappa=4000
            if power_level>power_nappa:
                print_slow("Kakarot was able to defeat Vegeta's henchman - Nappa in an epic showdown.")
                tokens+=1
                health-=10
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Nappa")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
            elif power_nappa>power_level:
                print_slow("Nappa was able to teach the inferior warrior - Goku a lesson. He defeated Kakarot badly.")
                tokens-=1
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Nappa")
                print("You lost.")
            else:
                print_slow("The saiyans ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                health-=10
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Nappa")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
        elif opp==3:
            Narrator("Goku","Vegeta")
            power_vegeta=18000
            if power_level>power_vegeta:
                print_slow("Kakarot was able to defeat the Prince of all Saiyans - Vegeta in an epic showdown.")
                tokens+=1
                health-=10
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Vegeta")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
            elif power_vegeta>power_level:
                print_slow("Vegeta was able to teach the inferior warrior - Goku a lesson. He defeated Kakarot badly.")
                tokens-=1
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Vegeta")
                print("You lost.")
            else:
                print_slow("The saiyans ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                health-=10
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Vegeta")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")

def frieza():
    print_slow("Which opponent will Son Goku fight?")
    print()
    print_slow("Press 1 for The Ginyu Force - Freiza's henchmen.")
    print_slow("Press 2 for Lord Frieza - Lord of the Universe")
    print()
    try:
        opp=int(input("Which opponent do you want to choose:"))
        print()
    except ValueError:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        if opp==1:
            Narrator("Goku","The Ginyu Force")
            print_slow("First to battle from the Ginyu force is the time-stopping menace - Guldo")
            power_gul=11500
            global power_level
            if power_level>power_gul:
                print_slow("Goku was able to defeat Guldo in an epic showdown.")
                global tokens
                tokens+=10
                global health
                health-=10
                global meal
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Guldo")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            elif power_gul>power_level:
                print_slow("The mighty Ginyu Force member was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                tokens-=5
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Guldo")
                print("You lost.")
            else:
                print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health-=10
                if health<=0:
                    health_text("Goku","Guldo")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            print_slow("Next to battle from the Ginyu force is the flamboyant fighter - Recoome")
            power_rec=71000
            if power_level>power_rec:
                print_slow("Goku was able to defeat Recoome in an epic showdown.")
                tokens+=10
                health-=10
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Recoome")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            elif power_rec>power_level:
                print_slow("The mighty Ginyu Force member was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                tokens-=5
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Recoome")
                print("You lost.")
            else:
                print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health-=10
                if health<=0:
                    health_text("Goku","Recoome")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            print_slow("Next to battle from the Ginyu force is the australian adversary - Jeice")
            power_jec=45000
            if power_level>power_jec:
                print_slow("Goku was able to defeat Jeice in an epic showdown.")
                tokens+=10
                health-=10
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Jeice")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            elif power_jec>power_level:
                print_slow("The mighty Ginyu Force member was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                tokens-=5
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Jeice")
                print("You lost.")
            elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
            else:
                print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                health-=10
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Jeice")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            print_slow("Next to battle from the Ginyu force is the blueish brawler - Burter")
            power_but=70000
            if power_level>power_but:
                print_slow("Goku was able to defeat Burter in an epic showdown.")
                tokens+=10
                health-=10
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Burter")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            elif power_but>power_level:
                print_slow("The mighty Ginyu Force member was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                tokens-=5
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Burter")
                print("You lost.")
            else:
                print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                health-=10
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Burter")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            print_slow("Last to battle from the Ginyu force is the captain himself - Captain Ginyu")
            power_cap=120000
            if power_level>power_cap:
                print_slow("Goku was able to defeat Captain Ginyu in an epic showdown.")
                tokens+=10
                health-=10
                meal+=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Captain Ginyu")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            elif power_cap>power_level:
                print_slow("The leader of the Ginyu Force member was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                tokens-=5
                health=0
                meal-=5
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Captain Ginyu")
                print("You lost.")
            else:
                print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                rel=[power_level,tokens,health,meal]
                result(rel)
                print()
                health-=10
                if health<=0:
                    health_text("Goku","Captain Ginyu")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
        elif opp==2:
            Narrator("Goku","Frieza")
            power_fri=120000000
            rage=random.randrange(1,101)
            if rage>75:
                power_level3=power_level*50
                print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_level3} and the power level of Frieza is {power_fri}.")
                print()
                print_slow(f"Kakarot has beaten Frieza to a plum and while trying to cut Goku in half, he is sliced.")
                tokens+=100
                health-=10
                meal+=5
                print()
                rel=[power_level3,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Frieza")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            else:
                if power_level>power_fri:
                    print_slow("Goku was able to defeat Frieza in an epic showdown.")
                    tokens+=100
                    health-=10
                    meal+=5
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Frieza")
                        print("You lost.")
                    elif health>0 and health<=10:
                        boost=(90/100)*power_level
                        power_level+=boost
                        print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_fri>power_level:
                    print_slow("The Lord of the Universe was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                    tokens-=50
                    health=0
                    meal-=5
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Frieza")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    result()
                    print()
                    health-=10
                    if health<=0:
                        health_text("Goku","Frieza")
                        print("You lost.")
                    elif health>0 and health<=10:
                        boost=(90/100)*power_level
                        power_level+=boost
                        print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")

def android():
    print_slow("Which opponent will Son Goku fight?")
    print()
    print_slow("Press 1 for Android 19 - A clown bot")
    print_slow("Press 2 for Android 20 - Dr.Gero")
    print_slow("Press 3 for Android 18 - A MILFy murder machine")
    print_slow("Press 4 for Android 17 - Boyish brawler")
    print_slow("Press 5 for Android 16 - Goku's threat.")
    print()
    try:
        opp=int(input("Which opponent do you want to choose:"))
        print()
    except ValueError:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        if opp==1:
            print_slow("The Android Saga has begun with a clown bot - Android 19.")
            power_19=157000000
            rage=random.randrange(1,101)
            ques=input("You can now play as Vegeta - The Prince of all Saiyans, would you like to continue (Yes/No):")
            if ques.lower()=="no":
                Narrator("Goku","Android 19")
                if rage>75:
                    global power_level
                    power_level4=power_level*50
                    if power_level4>power_19:
                        print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_level4} and the power level of Android 19 is {power_19}.")
                        print()
                        print_slow(f"Kakarot has beaten Android 19 to a plum.")
                        global tokens
                        tokens+=200
                        global health
                        health-=20
                        global meal
                        meal+=10
                        print()
                        rel=[power_level4,tokens,health,meal]
                        result(rel)
                        print()
                        if health<=0:
                            health_text("Goku","Android 19")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
                    elif power_19>power_level4:
                        power_19=160000000
                        print_slow(f"This is indeed a sight to witness, after obtaining the Super Saiyan form, Android 19 was able to get hold of the legendary warrior and absorb most of his energy, and now his power level has risen to 160 million!") 
                        print()
                        print_slow("Android 19 was able to beat Kakarot to a pulp.")
                        tokens-=100
                        health=0
                        meal-=5
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Android 19")
                        print("You lost.")
                        
                    else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health-=20
                        if health<=0:
                            health_text("Goku","Android 19")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")   
                        else:
                            pass
                else:
                    if power_level>power_19:
                        print_slow("Goku was able to defeat Android 19 in an epic showdown.")
                        tokens+=200
                        health-=20
                        meal+=10
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        if health<=0:
                            health_text("Goku","Android 19")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
                    elif power_19>power_level:
                        print_slow("Android 19 was able to fullfil his mission to defeat Goku. He defeated Kakarot badly.")
                        tokens-=100
                        health=0
                        meal-=10
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Android 19")
                        print("You lost.")
                        
                    else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health-=20
                        if health<=0:
                            health_text("Goku","Android 19")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
            elif ques.lower()=="yes":
                Narrator("Vegeta","Android 19")
                print_slow("'Now tell me, does a machine like you feel fear?' - Vegeta")
                power_veg=4000000
                power_veg*=50
                print_slow(f"This is indeed a sight to witness, Vegeta has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_veg} and the power level of Android 19 is {power_19}.")
                print()
                print_slow(f"The Prince has beaten Android 19 to a plum.")
                tokens+=200
                health-=20
                meal+=10
                print()
                rel=[power_veg,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Vegeta","Android 19")
                    print("You lost.")
                elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            else:
                print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
        elif opp==2:
            power_20=128000000
            rage=random.randrange(1,101)
            ques=input("You can now play as Piccolo , would you like to continue (Yes/No):")
            if ques.lower()=="yes":
                Narrator("Piccolo","Android 20")
                print_slow("'...And if I'm a fly, then just try and swat me!' -Piccolo")
                power_pic=165000000
                print_slow(f"This is indeed a sight to witness, Piccolo has demonstrated his awesome which is  {power_pic} and the power level of Android 20 is {power_20}.")
                print()
                print_slow(f"The Namekian has beaten Android 20 to a plum.")
                tokens+=200
                health-=20
                meal+=10
                print()
                rel=[power_pic,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Piccolo","Android 20")
                    print("You lost.")
                else:
                    pass
            elif ques.lower()=="no":
                Narrator("Goku","Android 20")
                if rage>75:
                    power_level5=power_level*50
                    if power_level5>power_20:
                        print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_level5} and the power level of Android 20 is {power_20}.")
                        print()
                        print_slow(f"Kakarot has beaten Android 20 to a plum.")
                        tokens+=200
                        health-=20
                        meal+=10
                        print()
                        rel=[power_level5,tokens,health,meal]
                        result(rel)
                        print()
                        if health<=0:
                            health_text("Goku","Android 20")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
                    elif power_20>power_level5:
                        power_20=154800000
                        print_slow(f"This is indeed a sight to witness, after obtaining the Super Saiyan form, Android 20 was able to get hold of the legendary warrior and absorb most of his energy, and now his power level has risen to 154.8 million!") 
                        print()
                        print_slow("Android 20 was able to beat Kakarot to a pulp.")
                        tokens-=100
                        health=0
                        meal-=5
                        rel=[power_level5,tokens,health,meal]
                        print()
                        result(rel)
                        print()
                        health_text("Goku","Android 20")
                        print("You lost.")
                        
                    else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level5,tokens,health,meal]
                        result(rel)
                        print()
                        health-=20
                        if health<=0:
                            health_text("Goku","Android 20")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
                else:
                    if power_level>power_20:
                        print_slow("Goku was able to defeat Android 20 in an epic showdown.")
                        tokens+=200
                        health-=20
                        meal+=10
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        if health<=0:
                            health_text("Goku","Android 20")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
                    elif power_20>power_level:
                        print_slow("Android 20 was able to fullfil his mission to defeat Goku. He defeated Kakarot badly.")
                        tokens-=100
                        health=0
                        meal-=10
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Android 20")
                        print("You lost.")
                        
                    else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health-=20
                        if health<=0:
                            health_text("Goku","Android 20")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
        elif opp==3:
            Narrator("Goku","Android 18")
            power_18=280000000
            rage=random.randrange(1,101)
            if rage>75:
                power_level6=power_level*50
                if power_level6>power_18:
                    print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_level6} and the power level of Android 18 is {power_18}.")
                    print()
                    print_slow(f"Kakarot has beaten Android 18 to a plum.")
                    tokens+=200
                    health-=20
                    meal+=10
                    print()
                    rel=[power_level6,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Android 18")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_18>power_level6:
                    power_18=154800000
                    print_slow(f"This is indeed a sight to witness, after obtaining the Super Saiyan form, Android 18 was able to get hold of the legendary warrior and absorb most of his energy, and now his power level has risen to 154.8 million!") 
                    print()
                    print_slow("Android 18 was able to beat Kakarot to a pulp.")
                    tokens-=100
                    health=0
                    meal-=5
                    print()
                    rel=[power_level6,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Android 18")
                    print("You lost.")
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level6,tokens,health,meal]
                    result(rel)
                    print()
                    health-=20
                    if health<=0:
                        health_text("Goku","Android 18")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
            else:
                if power_level>power_18:
                    print_slow("Goku was able to defeat Android 18 in an epic showdown.")
                    tokens+=200
                    health-=20
                    meal+=10
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Android 18")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_18>power_level:
                    print_slow("Android 18 was able to fullfil her mission to defeat Goku. He defeated Kakarot badly.")
                    tokens-=100
                    health=0
                    meal-=10
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Android 18")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health-=20
                    if health<=0:
                        health_text("Goku","Android 18")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
        elif opp==4:
            Narrator("Goku","Android 17")
            power_17=320000000
            rage=random.randrange(1,101)
            if rage>75:
                power_level7=power_level*50
                if power_level7>power_17:
                    print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_level7} and the power level of Android 17 is {power_17}.")
                    print()
                    print_slow(f"Kakarot has beaten Android 17 to a plum.")
                    tokens+=200
                    health-=20
                    meal+=10
                    print()
                    rel=[power_level7,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Android 17")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_17>power_level7:
                    print_slow(f"This is indeed a sight to witness, after obtaining the Super Saiyan form, Android 17 was able to get hold of the legendary warrior and defeat the mighty warrior!") 
                    print()
                    print_slow("Android 17 was able to beat Kakarot to a pulp.")
                    tokens-=100
                    health=0
                    meal-=5
                    print()
                    rel=[power_level7,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Android 17")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level7,tokens,health,meal]
                    result(rel)
                    print()
                    health-=20
                    if health<=0:
                        health_text("Goku","Android 17")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
            else:
                if power_level>power_17:
                    print_slow("Goku was able to defeat Android 17 in an epic showdown.")
                    tokens+=200
                    health-=20
                    meal+=10
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Android 17")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_17>power_level:
                    print_slow("Android 17 was able to fullfil his mission to defeat Goku. He defeated Kakarot badly.")
                    tokens-=100
                    health=0
                    meal-=10
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Android 17")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health-=20
                    if health<=0:
                        health_text("Goku","Android 17")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
        elif opp==5:
            Narrator("Goku","Android 16")
            power_16=440000000
            rage=random.randrange(1,101)
            if rage>75:
                power_level8=power_level*50
                if power_level8>power_16:
                    print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_level8} and the power level of Android 16 is {power_16}.")
                    print()
                    print_slow(f"Kakarot has beaten Android 16 to a plum.")
                    tokens+=200
                    health-=20
                    meal+=10
                    print()
                    rel=[power_level8,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Android 16")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_16>power_level8:
                    print_slow(f"This is indeed a sight to witness, after obtaining the Super Saiyan form, Android 16 was able to get hold of the legendary warrior and defeat the mighty warrior!") 
                    print()
                    print_slow("Android 16 was able to beat Kakarot to a pulp.")
                    tokens-=100
                    health=0
                    meal-=5
                    print()
                    rel=[power_level8,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Android 16")
                    print("You lost.")
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level8,tokens,health,meal]
                    result(rel)
                    print()
                    health-=20
                    if health<=0:
                        health_text("Goku","Android 16")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
            else:
                if power_level>power_16:
                    print_slow("Goku was able to defeat Android 16 in an epic showdown.")
                    tokens+=200
                    health-=20
                    meal+=10
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Android 16")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_16>power_level:
                    print_slow("Android 16 was able to fullfil his mission to defeat Goku. He defeated Kakarot badly.")
                    tokens-=100
                    health=0
                    meal-=10
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Android 16")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health-=20
                    if health<=0:
                        health_text("Goku","Android 16")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")

def cell():
    print_slow("Which opponent will Son Goku fight?")
    print()
    print_slow("Press 1 for Cell - A Bio Machine")
    print()
    try:
        opp=int(input("Which opponent do you want to choose:"))
        print()
    except ValueError:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        if opp==1:
            Narrator("Goku","Cell")
            power_1cell=250000000
            global power_level
            rage=random.randrange(1,101)
            if rage>75:
                global power_level9
                power_level9=power_level*50
                if power_level9>power_1cell:
                    print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_level9} and the power level of First-Form Cell is {power_1cell}.")
                    print()
                    print_slow(f"Kakarot has beaten Cell to a plum.")
                    global tokens
                    tokens+=300
                    global health
                    health-=20
                    global meal
                    meal+=15
                    print()
                    rel=[power_level9,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","First-Form Cell")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_1cell>power_level9:
                    print_slow(f"This is indeed a sight to witness, after obtaining the Super Saiyan form, Android 19 was able to get hold of the legendary warrior and absorb most of his energy, and now his power level has risen to 160 million!") 
                    print()
                    print_slow("Android 19 was able to beat Kakarot to a pulp.")
                    tokens-=100
                    health=0
                    meal-=5
                    rel=[power_level9,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Android 19")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level9,tokens,health,meal]
                    result(rel)
                    print()
                    health-=20
                    if health<=0:
                        health_text("Goku","Android 19")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
            else:
                if power_level>power_1cell:
                    print_slow("Goku was able to defeat First-Form Cell in an epic showdown.")
                    tokens+=300
                    health-=20
                    meal+=15
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","First-Form Cell")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_1cell>power_level:
                    print_slow("First-form Cell was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                    tokens-=150
                    health=0
                    meal-=30
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","First-Form Cell")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health-=30
                    if health<=0:
                        health_text("Goku","First-Form Cell")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
            print_slow("After absorbing Android 17, Cell evolved to - Second-Form Cell")
            power_2cell=450000000
            if power_level9>power_2cell:
                print_slow("Goku was able to defeat Second-Form Cell in an epic showdown.")
                tokens+=300
                health-=20
                meal+=5
                print()
                rel=[power_level9,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Second-Form Cell")
                    print("You lost.")
                elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            elif power_2cell>power_level9:
                print_slow("Cell's second form was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                tokens-=150
                health=0
                meal-=15
                print()
                rel=[power_level9,tokens,health,meal]
                result(rel)
                print()
                health_text("Goku","Second-Form Cell")
                print("You lost.")
            else:
                print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                print()
                rel=[power_level9,tokens,health,meal]
                result(rel)
                print()
                health-=20
                if health<=0:
                    health_text("Goku","Second-Form Cell")
                    print("You lost.")
                elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
            print_slow("After absorbing Android 18, Cell achieved its perfect form - Super Perfect Cell")
            power_3cell=5000000000
            ques=input("You can now play as Gohan - Son of Goku, would you like to continue (Yes/No):")
            if ques.lower()=="no":
                if power_level9>power_3cell:
                    print_slow("Goku was able to defeat Super Perfect Cell in an epic showdown.")
                    tokens+=350
                    health-=25
                    meal+=20
                    print()
                    rel=[power_level9,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Super Perfect Cell")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_3cell>power_level9:
                    print_slow("The mighty Perfect Cell was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                    tokens-=155
                    health=0
                    meal-=20
                    print()
                    rel=[power_level9,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Super Perfect Cell")
                    print("You lost.")
                    
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    health-=25
                    rel=[power_level9,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Super Perfect ")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
            elif ques.lower()=="yes":
                power_gohan=50000000
                power_gohan*=100
                Narrator("Gohan","Super Perfect Cell")
                print_slow(f"This is indeed a sight to witness, Gohan has obtained the legendary Super Saiyan 2 form increasing his power level 100 times which is now {power_gohan} and the power level of Super Perfect Cell is {power_3cell}.")
                print()
                print_slow(f"The beast has beaten Super Perfect Cell to a plum.")
                tokens+=350
                health-=25
                meal+=15
                print()
                rel=[power_gohan,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Gohan","Super Perfect Cell")
                    print("You lost.")
                elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                else:
                    pass
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
     
def buu():
    print_slow("Which opponent will Son Goku fight?")
    print()
    print_slow("Press 1 for Super Saiyan Majin Vegeta - A demented prince of the Saiyans.")
    print_slow("Press 2 for Majin Buu - A demon buffon.")
    print_slow("Press 3 for Evil Majin Buu.")
    print_slow("Press 4 for Super Buu.")
    print_slow("Press 5 for Super Buu (Trunks, Gotens and Piccolo absorbed.)")
    print_slow("Press 6 for Super Buu (Gohan, Trunks, Goten & Piccolo Absorbed)")
    print_slow("Press 7 for Kid Buu.")
    print()
    try:
        opp=int(input("Which opponent do you want to choose:"))
        print()
    except ValueError:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
    else:
        if opp==1:
            Narrator("Goku","Super Saiyan Majin Vegeta")
            power_ssj2vegeta=3000000000
            global power_level
            rage=random.randrange(1,101)
            if rage>85:
                power_level10=power_level*100
                Narrator("Goku","Super Saiyan Majin Vegeta")
                print_slow(f"This is indeed a sight to witness, Goku has obtained the legendary Super Saiyan 2 form increasing his power level 100 times which is now {power_level10} and the power level of Super Saiyan Majin Vegeta is {power_ssj2vegeta}.")
                print()
                print_slow(f"Kakarot has beaten Super Saiyan Majin Vegeta to a plum.")
                global tokens
                tokens+=400
                global health
                health-=30
                global meal
                meal+=20
                print()
                rel=[power_level10,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Super Saiyan Majin Vegeta")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
            else:
                if power_level>power_ssj2vegeta:
                    print_slow("Goku was able to defeat Super Saiyan Majin Vegeta in an epic showdown.")
                    tokens+=400
                    health-=30
                    meal+=20
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Super Saiyan Majin Vegeta")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
                elif power_ssj2vegeta>power_level:
                    print_slow("The demented prince was able to teach the inferior saiyan - Goku a lesson. He defeated Kakarot badly.")
                    tokens-=200
                    health=0
                    meal-=35
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Super Saiyan Majin Vegeta")
                    print("You lost.")
                else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health-=35
                    if health<=0:
                        health_text("Goku","Super Saiyan Majin Vegeta")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
        elif opp==2:
            print_slow("You can fight Majin Buu with a couple characters.")
            print_slow("Press 1 to play as Goku.")
            print_slow("Press 2 to play as Super Saiyan 2 Majin Vegeta.")
            print_slow("Press 3 to play as Super Saiyan 2 Gohan")
            print()
            power_buu=10000000000
            ques1=int(input("With which character do you want to fight Majin Buu against:"))
            if ques1==1:
                Narrator("Goku","Majin Buu")
                rage1=random.randrange(1,101)
                if rage1>90:
                    power_level2=power_level*150
                    if power_level2>power_buu:
                        print_slow(f"This is indeed a sight to witness, Kakarot has obtained the legendary Super Saiyan 3 form increasing his power level 100 times which is now {power_level2} and the power level of Majin Buu is {power_buu}.")
                        print()
                        print_slow(f"Kakarot has beaten Majin Buu to a plum.")
                        tokens+=450
                        health-=30
                        meal+=35
                        print()
                        rel=[power_level2,tokens,health,meal]
                        result(rel)
                        print()
                        if health<=0:
                            health_text("Goku","Majin Buu")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
                    elif power_buu>power_level2:
                        print_slow("Majin Buu was able to beat Kakarot to a pulp.")
                        tokens-=250
                        health=0
                        meal-=45
                        rel=[power_level2,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Majin Buu")
                        print("You lost.")
                    else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level2,tokens,health,meal]
                        result(rel)
                        print()
                        health-=30
                        if health<=0:
                            health_text("Goku","Majin Buu")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")   
                        else:
                            pass
                else:
                    if power_level>power_buu:
                        print_slow("Goku was able to defeat Majin Buu in an epic showdown.")
                        tokens+=450
                        health-=45
                        meal+=20
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        if health<=0:
                            health_text("Goku","Majin Buu")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
                    elif power_buu>power_level:
                        print_slow("Majin Buu was able to fullfil his mission to defeat Goku. He defeated Kakarot badly.")
                        tokens-=150
                        health=0
                        meal-=20
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Majin Buu")
                        print("You lost.")
                    else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level,tokens,health,meal]
                        result(rel)
                        print()
                        health-=45
                        if health<=0:
                            health_text("Goku","Majin Buu")
                            print("You lost.")
                        elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
            elif ques1==2:
                power_ssj2vegeta=3000000000
                Narrator("Super Saiyan Vegeta","Majin Buu")
                print_slow(f"This is indeed a sight to witness, Vegeta has obtained the legendary Super Saiyan 2 form increasing his power level 100 times which is now {power_ssj2vegeta} and the power level of Majin Buu is {power_buu}.")
                print()
                print_slow(f"The Prince has beaten Majin Buu to a plum.")
                tokens+=450
                health-=30
                meal+=50
                print()
                rel=[power_ssj2vegeta,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Super Saiyan 2 Vegeta","Majin Buu")
                    print("You lost.")
                elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
            elif ques1==3:
                Narrator("Super Saiyan Gohan","Majin Buu")
                power_ssj2gohan=2500000000
                print_slow(f"This is indeed a sight to witness, Gohan has obtained the legendary Super Saiyan 2 form increasing his power level 100 times which is now {power_ssj2gohan} and the power level of Majin Buu is {power_buu}.")
                print()
                print_slow(f"Gohan has beaten Majin Buu to a plum.")
                tokens+=450
                health-=30
                meal+=50
                print()
                rel=[power_ssj2gohan,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Super Saiyan 2 Gohan","Majin Buu")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
            else:
                print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")                 
        elif opp==3:
            Narrator("Goku","Evil Majin Buu")
            power_level1=power_level*400
            power_emajinbuu=5200000000
            if power_level>power_emajinbuu:
                print_slow(f"This is indeed a sight to witness, Goku has obtained the legendary Super Saiyan 3 form increasing his power level 400 times which is now {power_level1} and the power level of Evil Majin Buu is {power_emajinbuu}.")
                print()
                print_slow(f"Kakarot has beaten Evil Majin Buu to a plum.")
                tokens+=400
                health-=30
                meal+=20
                print()
                rel=[power_level1,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Evil Majin Buu")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
            elif power_emajinbuu>power_level:
                    print_slow("Evil Majin Buu was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                    tokens-=200
                    health=0
                    meal-=35
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health_text("Goku","Evil Majin Buu")
                    print("You lost.")
            else:
                    print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                    print()
                    rel=[power_level,tokens,health,meal]
                    result(rel)
                    print()
                    health-=35
                    if health<=0:
                        health_text("Goku","Evil Majin Buu")
                        print("You lost.")
                    elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                    else:
                        pass
        elif opp==4:
            que=input("You can now play as SSJ3 Gotenks, would you like to continue (yes/no):")
            if que.lower()=="yes":
                power_gotenks=56800000000
                power_ebuu=32000000000
                print_slow("Trunks and Gotens, sons of Vegeta and Kakarot respectively have been training to fuse with each other in order to defeat the Super Buu. They are together known as Gotenks!")
                Narrator("Gotenks","Super Buu")
                power_gotenks*=400
                print_slow(f"This is indeed a sight to witness, Gotenks has obtained the legendary Super Saiyan 3 form increasing his power level 400 times which is now {power_gotenks} and the power level of Super  Buu is {power_ebuu}.")
                print()
                print_slow(f"The fusion has beaten Super Buu to a plum.")
                tokens+=400
                health-=30
                meal+=20
                print()
                rel=[power_gotenks,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Gotenks","Super Buu")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyans after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                print_slow("Even though the battle was a success, Buu was able to get hold of the saiyan duo and the Namek - Piccolo and absorb them.")
            elif que.lower()=="no":
                Narrator("Goku","Super Buu")
                power_level11=power_level*400
                power_ebuu=32000000000
                if power_level11>power_ebuu:
                    print_slow(f"This is indeed a sight to witness, Goku has obtained the legendary Super Saiyan 3 form increasing his power level 400 times which is now {power_level11} and the power level of Super Buu is {power_ebuu}.")
                    print()
                    print_slow(f"Kakarot has beaten Super Buu to a plum.")
                    tokens+=400
                    health-=30
                    meal+=20
                    print()
                    rel=[power_level11,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Super Buu")
                        print("You lost.")
                    elif health>0 and health<=10:
                        boost=(90/100)*power_level
                        power_level+=boost
                        print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                elif power_ebuu>power_level11:
                        print_slow("Super Buu was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                        tokens-=200
                        health=0
                        meal-=35
                        print()
                        rel=[power_level11,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Super Buu")
                        print("You lost.")
                else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level11,tokens,health,meal]
                        result(rel)
                        print()
                        health-=35
                        if health<=0:
                            health_text("Goku","Super Buu")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass        
            else:
               print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")           
        elif opp==5:
            que3=input("You can now play as Gohan - Power Unleashed, would you like to continue (yes/no):")
            if que3.lower()=="yes":
                power_gohanpu=42000000000
                power_buu2=38250000000
                Narrator("Gohan","Super Buu (Trunks, Gotens and Piccolo absorbed)")
                print_slow(f"This is indeed a sight to witness, Gohan had his power unleashed by the Supreme Kai  which is now {power_gohanpu} and the power level of Super Buu (Trunks, Gotens and Piccolo absorbed) is {power_buu2}.")
                print()
                print_slow(f"The Saiyan has beaten Super Buu (Trunks, Gotens and Piccolo absorbed) to a plum.")
                tokens+=450
                health-=30
                meal+=50
                print()
                rel=[power_gohanpu,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Gohan","Super Buu (Trunks, Gotens and Piccolo absorbed)")
                    print("You lost.")
                elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!") 
            elif que3.lower()=="no":
                Narrator("Goku","Super Buu (Trunks, Gotens and Piccolo absorbed)")
                power_level12=power_level*400
                power_buu2=38250000000
                if power_level12>power_buu2:
                    print_slow(f"This is indeed a sight to witness, Goku has obtained the legendary Super Saiyan 3 form increasing his power level 400 times which is now {power_level12} and the power level of Super Buu (Trunks, Gotens and Piccolo absorbed) is {power_buu2}.")
                    print()
                    print_slow(f"Kakarot has beaten Super Buu (Trunks, Gotens and Piccolo absorbed) to a plum.")
                    tokens+=400
                    health-=30
                    meal+=20
                    print()
                    rel=[power_level12,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Super Buu (Trunks, Gotens and Piccolo absorbed)")
                        print("You lost.")
                    elif health>0 and health<=10:
                        boost=(90/100)*power_level
                        power_level+=boost
                        print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                    else:
                        pass
                elif power_buu2>power_level12:
                        print_slow("Super Buu (Trunks, Gotens and Piccolo absorbed) was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                        tokens-=200
                        health=0
                        meal-=35
                        print()
                        rel=[power_level12,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Super Buu (Trunks, Gotens and Piccolo absorbed)")
                        print("You lost.")
                else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level12,tokens,health,meal]
                        result(rel)
                        print()
                        health-=35
                        if health<=0:
                            health_text("Goku","Super Buu (Trunks, Gotens and Piccolo absorbed)")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
            else:
                print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
        elif opp==6:
            que2=input("You can now play as Vegito - A fusion of Vegeta and Kakarot, would you like to continue (yes/no):")
            if que2.lower()=="no":
                Narrator("Goku","Super Buu (Gohan, Gotenks and Piccolo absorbed)")
                power_level13=power_level*400
                power_buu3=80250000000
                if power_level13>power_buu3:
                    print_slow(f"This is indeed a sight to witness, Goku has obtained the legendary Super Saiyan 3 form increasing his power level 400 times which is now {power_level13} and the power level of Super Buu (Gohan, Gotenks and Piccolo absorbed) is {power_buu3}.")
                    print()
                    print_slow(f"Kakarot has beaten Super Buu (Gohan, Gotenks and Piccolo absorbed) to a plum.")
                    tokens+=400
                    health-=30
                    meal+=20
                    print()
                    rel=[power_level13,tokens,health,meal]
                    result(rel)
                    print()
                    if health<=0:
                        health_text("Goku","Super Buu (Gohan, Gotenks and Piccolo absorbed)")
                    elif health>0 and health<=10:
                        boost=(90/100)*power_level
                        power_level+=boost
                        print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                    else:
                        pass
                elif power_buu3>power_level13:
                        print_slow("Super Buu (Gohan, Gotenks and Piccolo absorbed) was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                        tokens-=200
                        health=0
                        meal-=35
                        print()
                        rel=[power_level13,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Super Buu (Gohan, Gotenks and Piccolo absorbed)")
                        print("You lost.")
                else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level13,tokens,health,meal]
                        result(rel)
                        print()
                        health-=35
                        if health<=0:
                            health_text("Goku","Super Buu (Gohan, Gotenks and Piccolo absorbed)")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
            elif que2.lower()=="yes":
                power_vegito=9000000000000 
                power_buu3=80250000000 
                Narrator("Vegito","Super Buu (Trunks, Gotens and Piccolo absorbed)")
                print_slow(f"This is indeed a sight to witness, Vegito has obtained the legendary Super Saiyan form increasing his power level 50 times which is now {power_vegito} and the power level of Super Buu (Gohan, Trunks, Goten & Piccolo Absorbed) is {power_buu3}.")
                print()
                print_slow(f"The Saiyan duo has beaten Super Buu (Gohan, Trunks, Goten & Piccolo Absorbed) to a plum.")
                tokens+=450
                health-=30
                meal+=50
                print()
                rel=[power_vegito,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Vegito","Super Buu (Gohan, Trunks, Goten & Piccolo Absorbed)")
                    print("You lost.")
                elif health>0 and health<=10:
                            boost=(90/100)*power_level
                            power_level+=boost
                            print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!") 
                else:
                    pass
        elif opp==7:
            Narrator("Goku and Vegeta","Kid Buu")
            power_kid_buu=22000000000
            power_level14=power_level*400
            if power_level14>power_kid_buu:
                print_slow(f"This is indeed a sight to witness, Goku has obtained the legendary Super Saiyan 3 form increasing his power level 400 times which is now {power_level14} and the power level of Kid Buu is {power_kid_buu}.")
                print()
                print_slow(f"Kakarot has beaten Super Buu to a plum.")
                tokens+=400
                health-=30
                meal+=20
                print()
                rel=[power_level14,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Goku","Kid Buu")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")
                else:
                    pass
                Narrator("Vegeta","Kid Buu")
                print_slow("With Kakarot trying to form a spirit bomb in order to defeat Kid Buu, Vegeta is buying time for him.")
                power_vegeta_new=6000000000
                print_slow(f"This is indeed a sight to witness, Vegeta has obtained the legendary Super Saiyan 2 form increasing his power level 100 times which is now {power_vegeta_new} and the power level of Kid Buu is {power_kid_buu}.")
                print()
                print_slow(f"The prince has beaten Kid Buu to a plum.")
                tokens+=400
                health-=30
                meal+=20
                print()
                rel=[power_vegeta_new,tokens,health,meal]
                result(rel)
                print()
                if health<=0:
                    health_text("Vegeta","Kid Buu")
                    print("You lost.")
                elif health>0 and health<=10:
                    boost=(90/100)*power_level
                    power_level+=boost
                    print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
            elif power_kid_buu>power_level14:
                        print_slow("Kid  Buu was able to teach the inferior monkey - Goku a lesson. He defeated Kakarot badly.")
                        tokens-=200
                        health=0
                        meal-=35
                        print()
                        rel=[power_level14,tokens,health,meal]
                        result(rel)
                        print()
                        health_text("Goku","Super Buu")
                        print_slow("With Kakarot defeated, he was not able to form the deadly spirit bomb. Vegeta was killed afterwards by Kid Buu")
                        print("You lost.")
            else:
                        print_slow("The fighters ended up in a stalemate in which both of them were injured pretty badly.")
                        print()
                        rel=[power_level14,tokens,health,meal]
                        result(rel)
                        print()
                        health-=35
                        if health<=0:
                            health_text("Goku","Kid Buu")
                            print("You lost.")
                        elif health>0 and health<=10:
                                boost=(90/100)*power_level
                                power_level+=boost
                                print_slow("The saiyan after a hard battle has now Zenkai Awakened! This has boosted his power level by 90%!")    
                        else:
                            pass
        else:
            print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")
                
def fight():
    print_slow("Press 1 to play in the Saiyan Saga.")
    print_slow("Press 2 to play in the Frieza Saga.")
    print_slow("Press 3 to play in the Android Saga.")
    print_slow("Press 4 to play in the Cell Saga.")
    print_slow("Press 5 to play in the Buu Saga")
    print()
    ques=int(input("Which Saga do you want to play in:"))
    if ques==1:
        saiyan()
    elif ques==2:
        frieza()
    elif ques==3:
        android()
    elif ques==4:
        cell()
    elif ques==5:
        buu()
    else:
        print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.") 
    
def DBZ_SonGoku():
    print()
    print_slow("Welcome to Dragon Ball Z - Son Goku.")
    print_slow("Here you can play as the legendary Super Saiyan - Son Goku, and fight his adversaries.")
    while True:
        ques=input("Would you like to start a new game or load a saved game (new/load/exit):")
        if ques.lower()=="new":
            database_and_table()
            while True:
                ques1=input("Would you like to continue (yes/no):")
                if ques1.lower()=="no":
                    print_slow("Saving the game.")
                    insert()
                    break
                else:
                    main()
                    pass
        elif ques.lower()=="load":
            load()
        elif ques.lower()=="exit":
            exit()
        else:
            pass
 
ques=input("Would you like to read the instructions (yes/no):")
if ques.lower()=="yes":
    print_slow(instruction)
    DBZ_SonGoku()
    print()  
elif ques.lower()=="no":
    DBZ_SonGoku()
    print()
else:
    print_slow("Vegeta - “Come on Kakarot find a way, I entrusted everything to you, my pride, my promise, everything. I WONT TOLERATE FAILURE.")