import random
import time
import datetime

print("Welcome to Crawdale Hotel!")

# Validation of the receptionist!
print("Enter Login Details!")
repName = "Kim Kakiiza"
passwordCheck = "22112003Keem"

while True:
    receptionistName = input("Receptionist Name: ")
    password = input("Enter password: ")

    if receptionistName == repName and password == passwordCheck:
        print(f"Welcome, {receptionistName}!")
        print("What would you like to do today?")
        break
    else:
        print("Invalid Login details. Please try again.")

while True:
    print("=============================\n\nA - Add new member \nB - Book a night \nC - Redeem points \nD - Display Member details \nQ - Quit System \n")
    select = input("Choose an option: ")

    # Option for Add A New Member
    if select == 'A':
        hotelfile = "SampleData2017.txt"
        with open(hotelfile, "a") as file:
            membersname = input("What is your surname? ")
            current_year = datetime.datetime.now().year
            nights_booked = int(input("Enter Nights Booked: "))
            if nights_booked > 14:
                print("ERROR!!! You can only book a MAX of 14 nights in a single booking")
                continue
            membership_status = "Silver"
            points = nights_booked * 2500
            member_id = membersname[0:3] + str(random.randint(10, 99)) + str(current_year)[-3:]
            print("Your Member ID is ", member_id)
            file.write(member_id + "," + membersname + "," + str(current_year) + "," + membership_status + "," + str(nights_booked) + "," + str(points) + "\n")
            print(f"Congratulations, {membersname}! You have been registered as a {membership_status} member with member ID {member_id}.")
            time.sleep(2)

    # Option for Book A Night and Redeem Points
    elif select == 'B' or select == 'C':
        # Modify an existing member account
        print("How would you like to view the Member Data?\n")
        select2 = input("1 - Display With Only Member ID \n2 - Display All Info \nEnter Choice: ")

        if select2 == '1':
            print("Just a moment!")
            time.sleep(2)
            hotelfile = "SampleData2017.txt"
            with open(hotelfile) as f:
                for line in f:
                    member_id = line.split(',')[0]
                    print(member_id)
            member_id = input("Please enter Member ID: ")

        elif select2 == '2':
            print("Just A Moment! \nDisplaying all member accounts:\n")
            time.sleep(2)
            hotelfile = "SampleData2017.txt"
            with open(hotelfile, "r") as file:
                for line in file:
                    print(line)
            member_id = input("Please select the member ID to modify: ")

        else:
            print("Invalid choice. Please try again.")
            continue

        # Modify the member account with the given ID
        print(f"Modifying member account with ID: {member_id}")

        if select == 'B':
            nights_booked = int(input("Enter new Nights Booked: "))
            if nights_booked > 14:
                print("ERROR!!! You can only book a MAX of 14 nights in a single booking")
                continue
            # Update the member account with new nights booked and points
            hotelfile = "SampleData2017.txt"
            with open(hotelfile, "r") as file:
                lines = file.readlines()
            with open(hotelfile, "w") as file:
                for line in lines:
                    member_data = line.split(',')
                    if member_data[0] == member_id:
                        old_nights_booked = int(member_data[4])
                        member_data[4] = str(old_nights_booked + nights_booked)
                        member_data[5] = str((old_nights_booked + nights_booked) * 2500) + "\n"
                        line = ",".join(member_data)
                    file.write(line)

            print("Member account has been updated.")
            time.sleep(2)


        elif select == 'C':
            points_to_redeem = int(input("Enter points to redeem: "))
            hotelfile = "SampleData2017.txt"
            with open(hotelfile, "r") as file:
                lines = file.readlines()
            with open(hotelfile, "w") as file:
                for line in lines:
                    member_data = line.split(',')
                    if member_data[0] == member_id:
                        current_points = int(member_data[5])
                        if points_to_redeem > current_points:
                            print("ERROR!!! Not enough points to redeem.")
                            file.write(line)
                            continue
                        member_data[5] = str(current_points - points_to_redeem) + "\n"
                        line = ",".join(member_data)
                    file.write(line)

            print(f"{points_to_redeem} points have been redeemed for member ID: {member_id}.")
            time.sleep(2)

    # Option for Display
    elif select == 'D':
        hotelfile = "SampleData2017.txt"
        with open(hotelfile, "r") as file:
            for line in file:
                print(line)
        print("All Member Accounts displayed")

    elif select == 'Q':
        # Print Thank You message
        print("Thank You!\nHave a good day :)")
        break
