import sqlite3
conn = sqlite3.connect('accountLog.db')  # This creates or opens the file 'example.db' as a database
c = conn.cursor()

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


def managing_options():
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


print("Welcome to the C2C Banking Management System")


while True:
  
  print("--------------------------------------------")
  c.execute('SELECT * FROM accounts')
  print(c.fetchall())
  print("--------------------------------------------")
  managing_options()
  m_choice = int(input("Choose an option from the menu above: "))
  if m_choice == 1:
    ac_num = int(input("Enter your account number: "))
    bal = c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
    theVal = c.fetchone()[0]
    print("Your current account balance is: "+ str(theVal))
      
  if m_choice == 2:
    ac_num = int(input("Enter your account number: "))
    dep = int(input("Enter the amount you want to deposit: "))
    bal = c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
    theVal = c.fetchone()[0]
    new_bal = int(theVal) + dep
    c.execute("UPDATE accounts SET account_bal = "+str(new_bal)+" WHERE account_num = "+str(ac_num))
    print("Your new balance is: "+ str(new_bal))

  if m_choice == 3:
    ac_num = int(input("Enter your account number: "))
    withd = int(input("Enter the amount you want to withdraw: "))
    bal = c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
    theVal = c.fetchone()[0]
    new_bal = int(theVal) - withd
    c.execute("UPDATE accounts SET account_bal = "+str(new_bal)+" WHERE account_num = "+str(ac_num))
    print("Your new balance is: "+ str(new_bal))

  if m_choice == 4:
    ac_num = int(input("Enter your account number: "))
    print("What would you like to change? ")
    print("(1) Account Number")
    print("(2) Account Pin")
    print(" ")
    change_choice = int(input("Enter your choice: "))
    if change_choice == 1:
      new_ac_num = int(input("Enter your new account number: "))
      c.execute("UPDATE accounts SET account_num = "+new_ac_num+" WHERE account_num = "+ac_num)
      print("Your account number has been updated to: "+str(new_ac_num)+".")
    if change_choice == 2:
      new_pin = int(input("Enter your new account pin: "))
      c.execute("UPDATE accounts SET account_pin = "+new_pin+" WHERE account_pin = "+ac_pin)
      print("Your new pin is: "+ str(new_pin))

  if m_choice == 5:
    new_ac_num = int(input("Enter your new account number: "))
    new_pin = int(input("Enter your new account pin: "))
    c.execute("INSERT INTO accounts (account_num, account_pin, account_bal) VALUES ("+str(new_ac_num)+", "+str(new_pin)+", 0)")
    print("Your new account has been created.")

  if m_choice == 6:
    ac_num = int(input("Enter your account number: "))
    c.execute("DELETE FROM accounts WHERE account_num = "+str(ac_num))
    print("Your account has been deleted.")
  if m_choice == 7:
    print(" ")
    print("--------------------------------------------")
    print("Thank you for using the C2C Banking Management System!")
    break
      
    


conn.commit()
conn.close()