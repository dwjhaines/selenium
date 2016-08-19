import time
import um_utils
from selenium import webdriver
    
if __name__ == "__main__":

    editors = ['fred', 'dave', 'chloe.anderson', 'chloe.garcia', 'chloe.jackson', 'chloe.johnson', 'chloe.jones', 'chloe.lee', 'chloe.lewis', 'chloe.martin'] 
    admins = []
    drivers = []

    for editor in editors:
        driver, result = um_utils.login(editor)
        drivers.append(driver)
        print 'Result = %d' % result

    print 'Sleeping for 10 secs.................'
    time.sleep( 10 )
    for driver in drivers:
        um_utils.logout(driver)
        time.sleep( 1 )
        um_utils.closeBrowser(driver)
