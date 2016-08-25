import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains


class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.admin = False
        self.manager = False
        self.loggedin = False

        # Create a new instance of the Chrome driver
        # Use incognito mode so that multiple users can be set up
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # Maximise browser window
        # self.driver.maximize_window()
        # Go to the Go! login page
        self.driver.get("http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=/go/")
        
    def setAdmin(user, isAdmin):
        user.admin = isAdmin
        
def login (user):
    # Logs in the user
    print 'Attempting Login: %s' % user.username
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
        print '\t%s successfullly logged in' % user.username
        result = 0
    elif ( user.driver.current_url == 'http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=%2fgo%2f' ):
        divText = user.driver.find_element_by_id('LoginDiv').text
        if 'You are already logged in' in divText:
            print '\tLogin failed: User already logged in'
            # Click on the OK button to get to the Go! page
            user.driver.find_element_by_id('ButtonOK').click()
            result = 1
        elif 'Please check your user name and password' in divText:
            print '\tLogin failed: Username or password incorrect'
            result = 2        
        elif 'Maximum number of users are logged in.' in divText:
            print '\tLogin failed: Maximum number of users already logged in'
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
    