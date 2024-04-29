import sqlite3
import os
import time
conn = sqlite3.connect('accountLog.db')  # This creates or opens the file 'example.db' as a database
c = conn.cursor()

#starting table i made **JUST A REFERENCE FOR ME**
'''
# Create table
c.execute("""CREATE TABLE accounts
            (account_num, account_pin, account_bal)""")

c.execute("""INSERT INTO accounts (account_num, account_pin, account_bal) VALUES
        (1, 1234, 2500),
        (2, 6789, 4500)""")

c.execute('SELECT * FROM accounts')
print(c.fetchall())
'''


def managing_options(): #list of choices printed in layout
  print("(1) Check Balance")
  print("(2) Deposit")
  print("(3) Withdraw")
  print("(4) Change Account Details")
  print("(5) Create Account")
  print("(6) Delete Account")
  print(" ")
  print("(7) Exit")
  print(" ")
  print(" ")

def reset(): #cleans up program when a choice is completed
    time.sleep(0.5)
    os.system('clear')
    print("RESULT----")
    print(" ")

def checkBal(ac_num): #check account balance (choice 1)
  bal = c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
  theVal = c.fetchone()[0]
  
  reset()
  print("Your current account balance is: "+ str(theVal))
  time.sleep(3)

def deposit(dep, ac_num): #deposit function (choice 2)
    bal = c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
    theVal = c.fetchone()[0]
    new_bal = int(theVal) + dep
    c.execute("UPDATE accounts SET account_bal = "+str(new_bal)+" WHERE account_num = "+str(ac_num))

    reset()
    print("Your new balance is: "+ str(new_bal))
    time.sleep(3)

def withdraw(withd, ac_num); #withdraw function (choice 3)
  bal = c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
  theVal = c.fetchone()[0]
  new_bal = int(theVal) - withd
  c.execute("UPDATE accounts SET account_bal = "+str(new_bal)+" WHERE account_num = "+str(ac_num))
  
      reset()
      print("Your new balance is: "+ str(new_bal))
      time.sleep(3)

def changeDetails(ac_num, ac_pin): #change acc pin or num (choice 4)
  print("What would you like to change? ")
  print("(1) Account Number")
  print("(2) Account Pin")
  print(" ")
  change_choice = int(input("Enter your choice: "))
  if change_choice == 1: #changing acc number(4.1)
    new_ac_num = int(input("Enter your new account number: "))
    c.execute("UPDATE accounts SET account_num = "+str(new_ac_num)+" WHERE account_num = "+str(ac_num))
  
    reset()
    print("Your account number has been updated to: "+str(new_ac_num)+".")
    time.sleep(3)
      
  if change_choice == 2: #changing acc pin(4.2)
    new_pin = int(input("Enter your new account pin: "))
    c.execute("UPDATE accounts SET account_pin = "+str(new_pin)+" WHERE account_pin = "+str(ac_pin))
  
    reset()
    print("Your new pin is: "+ str(new_pin))
    time.sleep(3)


def createAcc(ac_num, ac_pin): #create a new account (choice 5)
  c.execute("INSERT INTO accounts (account_num, account_pin, account_bal) VALUES ("+str(new_ac_num)+", "+str(new_pin)+", 0)")
  reset()
  print("Your new account has been created.")
  time.sleep(2)

def deleteAcc(ac_num): #delete an old account (choice 6)
  c.execute("DELETE FROM accounts WHERE account_num = "+str(ac_num))
  reset()
  print("Your account has been deleted.")
  time.sleep(2)
  

print("Welcome to the C2C Banking Management System")

def main(): #main program
  while True:  #this loops the program so you can make more choices
    #beginning layout
    print("--------------------------------------------")
    print("ACCOUNTS----")
    print(" ")
    c.execute('SELECT * FROM accounts')
    print(c.fetchall())
    print(" ")
    print("--------------------------------------------")
    managing_options() #prints choices 1-7
    
    m_choice = int(input("Choose an option from the menu above: ")) #user input choice option

    if m_choice == 1: #checking balance choice
      ac_num = int(input("Enter your account number: "))
      checkBal(ac_num)

    
    if m_choice == 2: #depositing choice
      ac_num = int(input("Enter your account number: "))
      dep = int(input("Enter the amount you want to deposit: "))
      deposit(dep, ac_num)

    
    if m_choice == 3: #withdrawing choice
      ac_num = int(input("Enter your account number: "))
      withd = int(input("Enter the amount you want to withdraw: "))
      withdraw(withd, ac_num)

    
    if m_choice == 4: #changing acc details choice
      ac_num = int(input("Enter your account number: "))
      ac_pin = int(input("Enter your account pin: "))
      changeDetails(ac_num, ac_pin)
  
    
    if m_choice == 5: #creating a new account choice
      new_ac_num = int(input("Enter your new account number: "))
      new_pin = int(input("Enter your new account pin: "))
      createAcc(new_ac_num, new_pin)
      
  
    if m_choice == 6: #deleting a new account choice
      ac_num = int(input("Enter your account number: "))
      deleteAcc(ac_num)
      
    if m_choice == 7: #exiting the program
      print(" ")
      print("--------------------------------------------")
      print("Thank you for using the C2C Banking Management System!")
      break
      
    


  conn.commit()
  conn.close()

if __name__ == '__main__': #unit testing call
  main()