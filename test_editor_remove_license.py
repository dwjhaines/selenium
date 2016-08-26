###############################################################################################
#                                                                                             # 
# test_editor_remove_license.py                                                               #
#                                                                                             # 
# When all licences are removed, a standard user should be given five minutes before being    #
# logged out. This test logs in a standard user and checks that the user is still logged in   #
# for five minutes. After five minutes, the user should be logged out.                        #
#                                                                                             #
###############################################################################################
import time
import um_utils
import db_utils
from selenium import webdriver
import pyodbc

if __name__ == "__main__":
   
    # Name of editor to be used for this test
    username = 'chloe.anderson'
    # Variable to hold the test result. Gets set to 1 if any part of the test fails
    testFailed = 0
    
    # Set up connection to database
    connection = db_utils.connectToDb()    
    cur = connection.cursor()
    
    # Delete all existing licenses
    db_utils.deleteAllLicenses(connection, cur)
    
    # Install license for five users
    db_utils.addFiveUserLicense(connection, cur)
    
    # Create a single standard user
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
        
        for x in range(0, 4):
            # Check user every minute to see if still logged in
            print 'Sleeping for 60 secs.................'
            time.sleep( 60 )
        
            # Check that user is still logged in
            if (db_utils.isUserLoggedIn(connection, cur, user)):
                print 'User still logged in after %d minutes' % (x + 1)
            else:
                print 'Test Failed: User logged out before 5 minutes'
                user.loggedin = False
                testFailed = 1
                break
        
        if (testFailed == 0):
            # If still logged in after four minutes, wait another 90 seconds and check that user has been logged out
            print 'Sleeping for 90 secs.................'
            time.sleep( 90 )
            # Check that user has been logged out
            if (db_utils.isUserLoggedIn(connection, cur, user)):
                print 'Test Failed: User has not been logged out after five minutes'
                print 'User still logged in after %d minutes' % x + 1
                testFailed = 1
            else:
                print 'User logged out after five minutes'
                user.loggedin = False

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