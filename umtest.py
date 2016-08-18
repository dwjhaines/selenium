import time
import um_utils
from selenium import webdriver
    
if __name__ == "__main__":

    editors = ['fred'] #, 'dave', 'chloe.anderson', 'chloe.garcia', 'chloe.jackson', 'chloe.johnson', 'chloe.jones', 'chloe.lee']
    admins = []
    drivers = []
    
    for editor in editors:
        driver, result = um_utils.login(editor)
        drivers.append(driver)
        print 'Result = %d' % result

        

    # print 'Sleeping for 10 secs.................'
    # time.sleep( 10 )
    # um_utils.logout(driver1)
    # print 'Sleeping for 5 secs.................'
    # time.sleep( 5 )
    # um_utils.closeBrowser(driver1)
