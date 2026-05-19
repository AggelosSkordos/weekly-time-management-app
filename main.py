import matplotlib.pyplot as plt
class User:
    def __init__(self, name,total_hours):
        self.name= name
        self.total_hours=total_hours
        self.activities = []
    def add_activity(self,activity):
        self.activities.append(activity)
class Activity:
    def __init__(self,name,type,time,importance):
        self.name= name
        self.type= type
        self.time = time
        self.importance= importance

def menu():
    print("\n"+ "="*45)
    print("WEEKLY TIME MANAGEMENT APP")
    print("="*45)
    print("1.Add activity")
    print("2.Edit activity")
    print("3.Delete activity")
    print("4.Show all activities")
    print("5.Show all activities by category")
    print("6.Show statistics")
    print("7.Show feasible activities")
    print("8.Sort activities")
    print("9.Save data")
    print("10.Load data")
    print("0.Exit")
    print("\n" + "=" * 45)

def get_time():
    while True:
        try:
            time = float(input("Time:"))
        except ValueError:
            print("Please enter a correct form of time")
            continue
        if time >= 0 and time <=user.total_hours:
            return time
        else:
            print("The value inserted is out of bounds. Please insert only values between 0 and ",user.total_hours,"(The max possible time.)")

def get_importance():
    while True:
        try:
            importance = int(input("Importance(1-10)"))
        except ValueError:
            print("Please enter an integer value ")
            continue
        if importance >= 1 and importance <= 10:
            return importance
        else:
            print("The value inserted is out of bounds(Accepted values 1-10).")

def get_type():
    while True:  # εδω ελέγχουμε άμα οι τιμές που θα εισάγουμε στον πίνακα της κλάσης είναι αποδεκτές και προστατεύουμε το σύστημα απο το να κρασάρει σε περίπτωση λάθος τιμής
        try:
            acttype = int(input("Type(0=Free time activities 1=Chores):"))
        except ValueError:
            print("Please enter an integer value(0 or 1)")
            continue
        if acttype == 1 or acttype == 0:
            return acttype
        else:
            print("Please type only values between 0-1.")



def add(user):
    print("Please input your activity details")
    name = input("Name:")
    acttype=get_type()
    time=get_time()
    importance=get_importance()
    activity = Activity(name, acttype, time, importance)
    user.add_activity(activity)
    

def edit(user):
    key = 0
    while True:
        master = False
        while True:
            name = input("Give the name of the activity you want to change")
            key = 0
            for activity in user.activities:
                if name.lower() == activity.name.lower():
                    found = activity
                    key = 1
                    break
            if key == 0:
                while True:
                    answer = input(
                        "Sorry didnt find the activity you were looking for.Would you like to try again(yes/no):")
                    if answer.lower() == "yes" or answer.lower() == "no":
                        break
                    else:
                        print("Please type either yes or no.")
                if answer.lower() == "no":
                    master = True
            if key == 1:
                break
        if master == True:
            break
        key = 0
        while key == 0:
            try:
                position = int(input("Please input which field you would like to be modified(1-4)"))
            except ValueError:
                print("Thats not an accepted value.")
                continue
            if position == 1:
                found.name = input("Please enter the activities new name")
                key = 1
                break
            elif position == 2:
               found.type=get_type()
               key=1
               break
            elif position == 3:
                found.time=get_time()
                key=1
                break
            elif position == 4:
                found.importance=get_importance()
                key=1
                break
        while True:
            answer = input("Would you like to continue editing the activity(yes/no):")
            if answer.lower() == "yes" or answer.lower() == "no":
                break
            else:
                print("Please enter only yes or no")
        if answer.lower() == "no":
            break

def delete(user):
    while True:
        answer=input("Please input the name of the activity you would like to delete")
        key=0
        for activity in user.activities:
            if activity.name == answer:
                key=key+1
        if key==0 :
            while True:
                print("No activity with the name:",answer,"was found.Would you like to search the activity with its details(Yes/No)?")
                cont=input()
                if cont.lower() != "yes" and cont.lower() != "no":
                    print("Please type only Yes or No.")
                else:
                    break
            if cont.lower()=="yes":
                print("Please input the information of the missing activity")
                acttype=get_type()
                importance=get_importance()
                time=get_time()
                num=1
                print("The activities found with the specific details are the following")
                for activity in user.activities:
                    if activity.type == acttype and activity.importance == importance and activity.time==time:
                        print(num,".",activity.name)
                        num=num+1
                if num==1:
                    print("No activities found.")
                    break
                else:
                    num2 = False
                    while True:
                        name=input("Which is the activities name?")
                        for activity in user.activities:
                            if activity.name== name:
                                user.activities.remove(activity)
                                num2=True
                                break
                        if num2 == True:
                            break
                        else:
                            print("The name you gave did not exist.Try again.")
            else:
                break
        elif key ==1:
            for activity in user.activities:
                if activity.name == answer:
                    user.activities.remove(activity)
                    print("The activity was removed successfully")
        else:
            while True:
                cont=input("There are multiple activities with the same name.Would you like to remove them all?")
                if cont.lower()=="yes" or cont.lower()=="no":
                    break
                else:
                    print("Please type only yes/no.")
            if cont.lower()=="yes":
                user.activities = [a for a in user.activities if a.name != answer]    #δεν μπορούμε να σβύσουμε πολλά  activities  όταν κάνουμε προσπέλαση με τον γνωστό τρόπο
            else:
                print("Please input the time,importance of the activity")   # Δεν χρειαζόμαστε τον τύπο της δραστηριότητας διότι θεωριτικά είναι όλες ίδιες.
                importance=get_importance()
                time=get_time()
                master=0   #θέλω να βάλω έναν τρόπο να μπορώ να φύγω από τις επαναλήψεις
                while True:
                    cont=0
                    for activity in user.activities:
                        if activity.importance==importance and activity.time==time :
                            cont=cont+1
                    if cont == 0:
                        while True:
                            temp = input("There are no activities with the specific time and importance that you entered.Would you like to retry(Yes?No)?")
                            if temp.lower() != "yes" and temp.lower() != "no":
                                print("Please enter only yes/no")
                            else:
                                break
                        if temp.lower() == "yes":
                            print("Please input the time,importance of the activity")
                            importance = get_importance()
                            time = get_time()
                            continue
                        else:
                            master = 1
                            break
                    elif cont==1:
                        for activity in user.activities:
                            if activity.importance==importance and activity.time==time:
                                user.activities.remove(activity)
                                break
                    else:
                        while True:
                            cont = input(
                                "There are multiple activities with the same name.Would you like to remove them all?")
                            if cont.lower() == "yes" or cont.lower() == "no":
                                break
                            else:
                                print("Please type only yes/no.")
                        if cont.lower() == "yes":
                            user.activities = [a for a in user.activities if a.name != answer]
                if master==1:
                    break

def showall(user):
    if len(user.activities) == 0:
        print("No activities found.")
        return
    print("Here are all the activities currently in the system.")
    print("-" * 20)
    for activity in user.activities :
        print("Name:", activity.name)
        print("Type:", activity.type)
        print("Time:", activity.time)
        print("Importance:", activity.importance)
        print("-" * 20)

def showallbycat(user):
    if len(user.activities) == 0:
        print("No activities found.")
        return
    print("Here are all the activities currently in the system sorted by category.")
    print("-" * 20)
    print("FREE TIME ACTIVITIES:")
    free=False
    chore=False
    for activity in user.activities:
        if activity.type == 0 :
            print("Name:", activity.name)
            print("Time:", activity.time)
            print("Importance:", activity.importance)
            print("-" * 20)
            free=True
    print("CHORES:")
    for activity in user.activities:
        if activity.type == 1 :
            print("Name:", activity.name)
            print("Time:", activity.time)
            print("Importance:", activity.importance)
            print("-" * 20)
            chore=True
    if chore == False:
        print("There are no chores in the system. ")
    if free == False:
        print("There are no free time  activities in the system.")

def stats(user):
    if len(user.activities) == 0:
        print("No activities found.")
        return
    totalact=len(user.activities)
    totaltime=0
    remaintime=0
    freetime=0
    choretime=0
    avgimport=0
    countavg=0
    mostimportact=0
    longestact=0
    for activity in user.activities:
        totaltime+=activity.time
        avgimport+=activity.importance
        countavg+=1
        if activity.type == 0 :
            freetime+=activity.time
        else:
            choretime+=activity.time
        if activity.importance>mostimportact:
            mostimportact=activity.importance
            mostimportactname=activity.name
        if activity.time>longestact:
            longestact=activity.time
            longestactname=activity.name
    avgimport=avgimport/countavg
    remaintime=user.total_hours-(choretime+freetime)
    if remaintime<0 :
        print("WARNING:Weekly schedule overload detected.")
        while True:
            try:choice=int(input("How would you like to continue?(1=continue,2=edit activities)"))
            except ValueError:
                print("Wrong type of value inserted.Try again.")
                continue
            if choice==1:
                break
            elif choice==2:
                while True:
                    edit(user)
                    if len(user.activities) == 0:
                        print("No activities found.")
                        return
                    totalact = len(user.activities)
                    totaltime = 0
                    remaintime = 0
                    freetime = 0
                    choretime = 0
                    avgimport = 0
                    countavg = 0
                    mostimportact = 0
                    longestact = 0
                    for activity in user.activities:
                        totaltime += activity.time
                        avgimport += activity.importance
                        countavg += 1
                        if activity.type == 0:
                            freetime += activity.time
                        else:
                            choretime += activity.time
                        if activity.importance > mostimportact:
                            mostimportact = activity.importance
                            mostimportactname = activity.name
                        if activity.time > longestact:
                            longestact = activity.time
                            longestactname = activity.name
                    avgimport = avgimport / countavg
                    remaintime = user.total_hours - (choretime + freetime)
                    if remaintime >= 0:
                        break
                    else:
                        print("WARNING:Weekly schedule overload detected again.")
            else:
                print("Please input only 1/2 values.")
    print("Total activities:",totalact)
    print("Total used time:",totaltime)
    print("Remaining free time:",remaintime)
    print("Free time activities hours:",freetime)
    print("Chores hours",choretime)
    print("Average importance:",avgimport)
    print("Most important activity:",mostimportactname)
    print("Longest activity:",longestactname)
    while True:
        choice = input("Would you like to display graphical statistics? (yes/no):")
        if choice.lower()=="yes" or choice.lower()=="no":
            break
        else:
            print("Please type only yes/no")
    if choice.lower() =="no":
        return
    else:
        labels = ["Free Time", "Chores"]
        sizes = [freetime, choretime]
        plt.pie(sizes, labels=labels, autopct="%1.1f%%")
        plt.title("Weekly Time Distribution")
        plt.show()

def showfeasible(user):
    if len(user.activities) == 0:
        print("No activities found.")
        return
    if len(user.activities) == 1:
        print(user.activities[0].name)
        return
    count=0
    for i in range(len(user.activities) - 1):
        if user.activities[i].importance < user.activities[i + 1].importance:
            count=1
    if count== 1:
        while True:
            answer=input("The activity list is not sorted.Would you like it to get sorted?(Yes/No):")
            if answer.lower()=="yes":
                #sort(user)
                print("The list has been sorted.")
                break
            elif answer.lower()=="no":
                return
            else:
                print("Please input only yes/no.")
    print("="*13,"FEASIBLE ACTIVITIES","="*13)
    totaltime=user.total_hours
    for activity in user.activities:
        if totaltime-activity.time >=0:
            print("Name:", activity.name)
            print("Importance:", activity.importance)
            print("Time:", activity.time)
            totaltime=totaltime-activity.time
    print("Remaining time:", totaltime)

def save(user):
    filename = user.name + ".txt"
    file = open(filename, "w")
    file.write(user.name + "\n")
    file.write(str(user.total_hours) + "\n")
    for activity in user.activities:
        line = (
            activity.name + ","
            + str(activity.type) + ","
            + str(activity.time) + ","
            + str(activity.importance)
            + "\n")
        file.write(line)
    file.close()
    print("Data saved successfully.")

def load():
    filename = input("Enter filename: ")
    file = open(filename, "r")
    username = file.readline().strip()
    total_hours = float(file.readline().strip())
    user = User(username, total_hours)
    for line in file:
        data = line.strip().split(",")
        name = data[0]
        type = int(data[1])
        time = float(data[2])
        importance = int(data[3])
        activity = Activity(name, type, time, importance)
        user.add_activity(activity)
    file.close()
    print("Data loaded successfully.")
    return user




#Εδώ ξεκινάει η main
print("="*5,"WELCOME TO THE TIME MANAGEMENT APP FOR EVERY DAY USE","="*5)
while True:
    try:
        choice=int(input("Please type 1 for new user and 0 for existing user."))
    except ValueError:
        print("You inserted a wrong value.Try again.")
        continue
    if choice ==1 or choice ==0 :
        break
    else:
        print("Please enter values equal to 0 or 1")
if choice == 1:
    username= input("Please enter your username")
    total=int(input("Please input your total available time this week in the form of hours "))
    while total < 0 or total > 119:  # ο μέγιστος συνολικός χρόνος που μπορεί κάποιος να έχει μέσα σε μια βδομάδα πλην τον χρόνο για ύπνο
        print("Wrong value inserted")
        total = int(input("Please input your total available time this week in the form of hours "))
    user = User(username, total)
else:
    user=load()

while True:
    menu()
    while True: #εδώ ελέγχω άμα ο χρήστης δώσει λάθος τύπο μεταβλητής ώστε να εμποδίσω το σύστημα από το να κρασάρει και να περάσω μόνο αποδεκτές επιλογές
         try:
             choice=int(input("Enter your choice"))
         except ValueError:
             print("Please enter an integer number")
             continue
         if choice>=0 and choice<=11:
             break
         else:
             print("The value is out of bounds")
    if choice == 1:
        add(user)
    elif choice == 2:
        edit(user)
    elif choice == 3:
        delete(user)
    elif choice == 4:
        showall(user)
    elif choice == 5:
        showallbycat(user)
    elif choice == 6:
        stats(user)
    elif choice ==7:
        showfeasible(user)
    #elif choice ==8:

    elif choice ==9:
        save(user)
    elif choice ==10:
        load()

    #elif choice ==0:



















