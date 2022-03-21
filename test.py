import email
from os import access
import smtplib
import pandas
from random import randint

#generate random code between 10001 to 9999
def generateCode():
    num = randint(1001,9999)
    return num

#sends to unique security code on registerd email Id
def sendEmailWithOTP(emailId,code):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login('manishnangliya26@gmail.com', 'password')
    subject = "New Registration"
    body = 'Your Security code for luggage is: {}'.format(code)
    message = "Subject:{}\n\n{}".format(subject,body)
    server.sendmail('manishnangliya26@gmail.com', emailId, message)

    print('Security code has been sent to registered Email',end="\n\n")
    server.quit()


# function to register new luggage
def register():
    """
    Function to register Luggage
    """
    print("\nRegistering a new Luggage")
    print("-"*40, end="\n\n")
    emaiId = input("Enter your Email: ")
    code = str(generateCode())
    
    df = pandas.read_csv('users.csv')
    if emaiId in df['emaiId'].values:
        print("Luggage already exists!!", end="\n\n")
        return

    df.loc[len(df)] = [emaiId, code]
    sendEmailWithOTP(emaiId,code)
    df.to_csv('users.csv', index=False)

    print("Luggage registered successfully!!", end="\n\n")

# sends a alert Message on Email while someone want to access luggage
def sendmailForAccess(emailId):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login('manishnangliya26@gmail.com', 'password')
    subject = "!! Alert !!"
    body = 'Someone is Trying to open your luggage '
    message = "Subject:{}\n\n{}".format(subject,body)
    server.sendmail('manishnangliya26@gmail.com', emailId, message)

    print('Alert Mail Sent', end ="\n\n")
    server.quit()


def accessLuggage():
    """
    Function to Access Luggae
    """
    
    print("\nAccess Luggage")
    print("-"*40, end="\n\n")
    emaiId = input("Enter your Email: ")
    code = input("Enter your code: ")
    df = pandas.read_csv('users.csv', sep=',')

    for index, row in df.iterrows():
        if emaiId == str(row['emaiId']) and code == str(row['code']):
            sendmailForAccess(emaiId)
            return
    
    print("Luggage Doesn't belong to You", end="\n\n")

def main():
    while True:
        print("Welcome to the Secure luggage")
        print("1. Register")
        print("2. Access your Luggage")
        print("3. Exit", end="\n\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            accessLuggage()
        elif choice == "3":
            break
        else:
            print("Invalid choice",end="\n\n")


if __name__ == '__main__':
    main()