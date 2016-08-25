###############################################################################################
#                                                                                             # 
# valid_license_editors.py                                                                    #
#                                                                                             # 
# Adds a license for five users and tests that no more than five users can log in.            #
#                                                                                             #
###############################################################################################
import time
import um_utils
import db_utils
from selenium import webdriver
import pyodbc

if __name__ == "__main__":
   
    # List of editors i.e. users that do not have admin rights
    editors = ['chloe.anderson', 'chloe.garcia', 'chloe.jackson', 'chloe.johnson', 'chloe.jones', 'chloe.lee']
    # Empty list to be filled with user objects
    users = [] 
    # Variable to hold the test result. Gets set to 1 if any part of the test fails
    testFailed = 0
    
    # Set up connection to database
    connection = db_utils.connectToDb()    
    cur = connection.cursor()
    
    # Delete all existing licenses
    db_utils.deleteAllLicenses(connection, cur)
    
    # Install license for five users and set the value of maxUsers
    maxUsers = db_utils.addFiveUserLicense(connection, cur)
    print 'License installed for %d users' % maxUsers
    # Check that the database indicates the correct max number of users
    MaxConcurrentUsers = db_utils.getMaxConcurrentUsers(connection, cur)
    if (MaxConcurrentUsers != maxUsers):
        testFailed = 1
        print 'Test Failed: MaxConcurrentUsers not set correctly in database.'
    else:
        print 'MaxConcurrent users set correctly in datavbase'
    # Get the number of users already logged in
    count = db_utils.getNumberOfActiveUsers(connection, cur)
    
    
    print 'Max users allowed: %d' % maxUsers
    print 'Number of users already logged in: %d' % count
    print 'Opening browsers........'

    for editor in editors:
        # For each editor, create a user object and add object to users list
        users.append(um_utils.user(editor, 'quantel@'))
       
    # Keep trying to log in each of the editors. Once the max number of users have been logged in, no further logins should be allowed.
    for user in users:
        result = um_utils.login(user)
        if (result == 0 or result == 1):
            user.loggedin = True 
        count = db_utils.getNumberOfActiveUsers(connection, cur)
        print '\tNumber of active users (max: %d): %d' % (maxUsers, count)
        if (count > maxUsers):
            testFailed = 1
            print 'Test Failed: Max number of users exceded.'
            
    print 'Sleeping for 10 secs.................'
    time.sleep( 10 )
    
    # Log out any users that were logged in and close all the browsers
    for user in users:
        if (user.loggedin == True):
            um_utils.logout(user)
            user.loggedin = False
        time.sleep( 1 )
        um_utils.closeBrowser(user)
    
    # Close connection to database
    db_utils.closeConnection(connection, cur) 
    
    # Print test result
    if (testFailed == 1):
        print '************ Test Failed ************'
    else:
        print '************ Test Passed ************'