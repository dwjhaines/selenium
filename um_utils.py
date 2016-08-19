import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

def login (username):
    # Create a new instance of the Chrome driver
    # Use incognito mode so that multiple users can be set up
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Maximise browser window
    driver.maximize_window()

    # Go to the Go! login page
    driver.get("http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=/go/")

    user = str(username)
    
    print 'User %s attempting to log in' % user
    time.sleep( 2 )
    # Enter username into UserName dialog
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "UserName")))
    username.send_keys(user)

    # Enter password into Password dialog (assume password is quantel@)
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Password")))
    password.send_keys('quantel@')

    # Select and click on the login button
    driver.find_element_by_id('LoginButton').click()
    
    # Wait until we have moved on from the login page
    try:
        page_loaded = WebDriverWait( driver, 10 ).until_not(
        lambda driver: driver.current_url == "http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=/go/"
    )
    except TimeoutException:
        self.fail( "Loading timeout expired" )
        
    if ( driver.current_url == 'http://10.165.250.201/go/'):
        # If the Go! page has been loaded then login has been successful
        print 'Successful Login'
        result = 0
    elif ( driver.current_url == 'http://10.165.250.201/quantel/um/login.aspx?ReturnUrl=%2fgo%2f' ):
        divText = driver.find_element_by_id('LoginDiv').text
        if 'You are already logged in' in divText:
            print 'User already logged in'
            # Click on the OK button to get to the Go! page
            driver.find_element_by_id('ButtonOK').click()
            result = 1
        elif 'Please check your user name and password' in divText:
            print 'Username or password incorrect'
            result = 2        
        elif 'Maximum number of users are logged in.' in divText:
            print 'Maximum number of users exceded'
            result = 3
            
    return (driver, result)

def logout (driver):
    print 'Select options'
    element = driver.find_element_by_class_name('icon-user')
    hov = ActionChains(driver).move_to_element(element)
    hov.perform()

    print 'Logging out'
    form = driver.find_element_by_id('logout').click()
    
def closeBrowser(driver):
    print 'Close browser'
    driver.close()
    #Login failed. Please check your user name and password, and try again.
    