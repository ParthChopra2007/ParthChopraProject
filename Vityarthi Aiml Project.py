import time                             #importing time module

reminders = []

print("Welcome to the Reminder App!")
print("Type your reminder, then enter minutes from now. Type 'exit' to stop.\n")

while True:                     #asking user for inputs
    reminder = input("What do you want to be reminded about? (Type 'exit' to quit): ")
    if reminder.lower() == 'exit':
        print("Exiting Reminder Bot. Goodbye!")
        break
    minutes = input("How many minutes from now should I remind you? ")
    if not minutes.isdigit():                   #error
        print("Please enter a valid number.")
        continue
    remind_time = time.time() + int(minutes) * 60           #calculating for the reminder
    reminders.append((reminder, remind_time))
    print(f"Reminder set for \"{reminder}\" in {minutes} minutes.\n")

    while reminders:                            #checking for the reminders every 10 sec
        current_time = time.time()
        for r in reminders:
            if current_time >= r[1]:
                print(f"\n**Reminder: {r[0]}**\n")
                reminders.remove(r)
        if not reminders:
            break
        time.sleep(10)

