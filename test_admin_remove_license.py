###############################################################################################
#                                                                                             # 
# test_admin_remove_license.py                                                                #
#                                                                                             # 
# When all licences are removed, an administrator should not be logged out                    #
# This test logs in an administrator and checks that she is still logged in after six minutes #
#                                                                                             #
###############################################################################################
import time
import um_utils
import db_utils
from selenium import webdriver
import pyodbc

if __name__ == "__main__":
   
    # Name of editor to be used for this test
    username = 'avaa.johnsona'
    # Variable to hold the test result. Gets set to 1 if any part of the test fails
    testFailed = 0
    
    # Set up connection to database
    connection = db_utils.connectToDb()    
    cur = connection.cursor()
    
    # Delete all existing licenses
    db_utils.deleteAllLicenses(connection, cur)
    
    # Install license for five users
    db_utils.addFiveUserLicense(connection, cur)
    
    # Create a single user with admin rights
    user = um_utils.user(username, 'quantel@')
       
    result = um_utils.login(user)
    if (result == 0 or result == 1):
        user.loggedin = True 
    else:
        testFailed = 1
        print 'Test Failed: User could not log in.'

    if (user.loggedin == True):
        # Delete all existing licenses
        db_utils.deleteAllLicenses(connection, cur)
        
        for x in range(0, 6):
            # Check user every minute to see if still logged in
            print 'Sleeping for 60 secs.................'
            time.sleep( 60 )
        
            # Check that user is still logged in
            if (db_utils.isUserLoggedIn(connection, cur, user)):
                print 'User still logged in after %d minutes' % (x + 1)
            else:
                print 'Test Failed: User has been logged out'
                user.loggedin = False
                testFailed = 1
                break      

    # Log out any users that were logged in and close all the browsers
    if (user.loggedin == True):
        um_utils.logout(user)
        user.loggedin = False
    time.sleep( 1 )
    um_utils.closeBrowser(user)
    
    # Install license for five users
    db_utils.addFiveUserLicense(connection, cur)
    
    # Close connection to database
    db_utils.closeConnection(connection, cur) 
    
    # Print test result
    if (testFailed == 1):
        print '************ Test Failed ************'
    else:
        print '************ Test Passed ************'