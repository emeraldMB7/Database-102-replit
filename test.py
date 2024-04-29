import unittest
from main import deposit
import sqlite3

class TestAccounts(unittest.TestCase):
  def setUp(self):
    self.test_conn = sqlite3.connect('accountLog.db')
    self.c = self.test_conn.cursor()


  
  def test_canary(self):
    self.assertTrue(True)


  
  def test_deposit(self):
    ac_num = 1
    testDep = 500
    
    bal = self.c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
    beforeVal = self.c.fetchone()[0]
    
    deposit(testDep, ac_num)
    
    bal = self.c.execute("SELECT account_bal FROM accounts WHERE account_num = "+str(ac_num))
    afterVal = self.c.fetchone()[0]
    self.assertEqual(int(beforeVal)+testDep, int(afterVal))


  
  def tearDown(self):
    self.c.close()
    self.test_conn.close()

if __name__ == '__main__':
  unittest.main()