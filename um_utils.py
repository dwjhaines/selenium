import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

os.environ["LICENSE_5_USERS"] = 'PVG-standalone-in-house-only-5-users----------------814755e6-01f2-c7e7-5971-cac39bde5fbb525b7c9c-0dab-45b3-ad29-8d282ef2cb81fae144dd-d44874a6b-a28a-7d330028771fae144e06-63ff-4d69-b087-337badbb7c52ca7ca81f-5069-4b61-8799-d58c5e9e9d459f42d31f-cccf-426b-b839-e3c3a9c32fba5cf15e77-b64f-4de9-b88e-114fba3fb67a755c4441-b3de-4a48-a20f-3bd142cd2d8f566fb6a8-3b20-451b-b74f-06da965efbe5e85a72a9-e941-465d-a73b-275205fb55ae3a265fb4-ea8e-45ba-8a9e-d12a3143497779389c8b-8cf9-49f7-84a5-a56b7529771fa003f339-614d-431b-a15c-6e76d6654efa80c80a5e-1772-411d-bbe5-ad8f0fa95439a4c86fdf-bb50-40c8-9f79-3c98c34461ea6b42520a-91a9-4fd3-9558-d6fc6d6bd42cd9ea5b42-de91-4cdd-81ec-820bd824c03f29b6c5ae-c6b8-462c-9e16-b53c1ecddf64543e2763-9548-4f7f-be53-2e104a0b337667b94404-55ad-4d0d-89c7-b2cbae172d3f62fc523d-656d-41e9-bdeb-eabaed3d3da3c53d8cb5-fb2f-408f-970c-a6267740b9ce02a4aec5-199a-48e5-b7a3-cb3969480e6a916f07c5-0733-4790-82ca-beeb67bbdb598f4e3261-3ffa-4237-b95d-d11e6a897fa58b0402e1-e94a-4013-904a-42983a3fd5dbcc769362-5c42-4fae-a7dd-55b5133e8002'

class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin = False
        self.loggedin = False
        # Create a new instance of the Chrome driver
        # Use incognito mode so that multiple users can be set up
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # Maximise browser window
        self.driver.maximize_window()
        # Go to the Go! login page
        self.driver.get("http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=/go/")
        
    def setAdmin(user, isAdmin):
        user.admin = isAdmin
        
def login (user):
    # Logs in the user
    print 'Login: %s' % user.username
    time.sleep( 2 )
    # Enter username into UserName dialog
    username = WebDriverWait(user.driver, 10).until(EC.presence_of_element_located((By.NAME, "UserName")))
    username.send_keys(user.username)

    # Enter password into Password dialog (assume password is quantel@)
    password = WebDriverWait(user.driver, 10).until(EC.presence_of_element_located((By.NAME, "Password")))
    password.send_keys(user.password)

    # Select and click on the login button
    user.driver.find_element_by_id('LoginButton').click()
    
    # Wait until we have moved on from the login page
    try:
        page_loaded = WebDriverWait( user.driver, 10 ).until_not(
        lambda driver: user.driver.current_url == "http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=/go/"
    )
    except TimeoutException:
        self.fail( "Loading timeout expired" )
        
    if ( user.driver.current_url == 'http://10.165.250.201/go/'):
        # If the Go! page has been loaded then login has been successful
        print '%s successfullly logged in' % user.username
        result = 0
    elif ( user.driver.current_url == 'http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=%2fgo%2f' ):
        divText = user.driver.find_element_by_id('LoginDiv').text
        if 'You are already logged in' in divText:
            print 'User already logged in'
            # Click on the OK button to get to the Go! page
            user.driver.find_element_by_id('ButtonOK').click()
            result = 1
        elif 'Please check your user name and password' in divText:
            print 'Username or password incorrect'
            result = 2        
        elif 'Maximum number of users are logged in.' in divText:
            print 'Maximum number of users exceded'
            result = 3
            
    return result

def logout (user):
    element = user.driver.find_element_by_class_name('icon-user')
    hov = ActionChains(user.driver).move_to_element(element)
    hov.perform()

    print 'Logging out: %s' % user.username
    form = user.driver.find_element_by_id('logout').click()
    
def closeBrowser(user):
    print 'Closing browser'
    user.driver.close()
    