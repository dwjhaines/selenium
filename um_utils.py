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
        
    def setAdmin(user, isAdmin):
        user.admin = isAdmin
        
def login (user):
    # Logs in the user
    print 'Attempting Login: %s' % user.username
    return 0 # result

def logout (user):
    print 'Logging out: %s' % user.username
    
def closeBrowser(user):
    print 'Closing browser'

    