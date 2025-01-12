import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# inherit TestCase Class and create a new test class
username ='ADMIN'
access_key = ''
class DjangoTest(unittest.TestCase):
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()
      
  
    # cleanup method called after every test performed
    # TH1 nhap username đ, pw sai  ---> KQ kỳ vọng login f
    # TH2 Nhap username sai, pw đúng --> login f 
    # TH3 nhập đúng cả 2 --> loging thành công ---> vào trong trang hệ thông 
    # TH4 Nhap sai ca username, pw
    # khong nhap gi het --- login f 
    def tearDown(self):
        self.driver.close()
    # unittest
    # quy tac dat ten : test_unit_[ten functoin]
    def test_unit_login_3(self): 
        """
        Test the login functionality of the admin site.
        This test performs the following steps:
        1. Opens the admin login page.
        2. Enters the username "admin".
        3. Enters the password "123456".
        4. Submits the login form.
        5. Verifies that the page title is "Site administration | Django site admin".
        Assertions:
        - The page title should be "Site administration | Django site admin" after login.
        """
        # try:
        # get driver
        print('bat dau')
        driver = self.driver
        # get python.org using selenium
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        inputUserName  = driver.find_element(By.NAME,value="username")
       
        inputUserName.send_keys("admin")
        # time.sleep(5)

        password  = driver.find_element(By.NAME,value="password")
   
        password.send_keys("123456")
        # time.sleep(5)

        password.send_keys(Keys.RETURN)

        # time.sleep(10)
        actualTitle = driver.title 
        print(actualTitle)
        # assert actualTitle ,"Site administration | Django site admin"
        assert(actualTitle == "Site administration | Django site admin")

        # receive data
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

    def test_unit_login_2(self): 
        """
        Test the login functionality of the Django admin site.
        This test performs the following steps:
        1. Opens the Django admin login page.
        2. Enters the username "admin".
        3. Enters the password "qqqqqqqqqq".
        4. Submits the login form.
        5. Verifies that the page title after login is "Log in | Django site admin".
        Asserts:
            The page title after login is "Log in | Django site admin".
        """
        # try:
        # get driver
        print('bat dau')
        driver = self.driver
        # get python.org using selenium
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        inputUserName  = driver.find_element(By.NAME,value="username")
    
        inputUserName.send_keys("admin")
        # time.sleep(5)
        password  = driver.find_element(By.NAME,value="password")
        password.send_keys("qqqqqqqqqq")
        # time.sleep(5)

        password.send_keys(Keys.RETURN)

        # time.sleep(10)
        actualTitle = driver.title 
        print(actualTitle)
        # assert actualTitle ,"Site administration | Django site admin"
        assert(actualTitle == "Log in | Django site admin")

# execute the script
if __name__ == "__main__":
    unittest.main()