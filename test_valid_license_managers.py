###############################################################################################
#                                                                                             # 
# test_valid_license_managers.py                                                              #
#                                                                                             # 
# Adds a license for five users and tests that ten managers can log in.                       #
#                                                                                             #
###############################################################################################
import time
import um_utils
import db_utils
from selenium import webdriver
import pyodbc

if __name__ == "__main__":
    
    # List of managers i.e. users with manager rights
    managers = ['maria.a', 'maria.b', 'maria.c', 'maria.d', 'maria.e', 'maria.f', 'maria.g', 'maria.h', 'maria.i', 'maria.j', 'maria.k', 'maria.l']
    # Empty list to be filled with user objects
    users = [] 
    testFailed = 0
    
    # Set up connection to database
    connection = db_utils.connectToDb()    
    cur = connection.cursor()
    
    # Delete all existing licenses
    db_utils.deleteAllLicenses(connection, cur)
    
    # Install license for five users and set the value of maxManagers
    maxUsers = db_utils.addFiveUserLicense(connection, cur)
    print 'License installed for %d users' % maxUsers       
    maxManagers = maxUsers + 5
    print 'Maximum number of managers = %d' % maxManagers
    count = db_utils.getNumberOfActiveUsers(connection, cur)
    
    print 'Max users allowed: %d' % maxUsers
    print 'Max managers allowed: %d' % maxManagers
    print 'Number of users already logged in: %d' % count
    print 'Opening browsers........'

    for manager in managers:
        # For each administrator, create a user object and add object to users list
        users.append(um_utils.user(manager, 'quantel@'))
       
    # Keep trying to log in each of the editors. Once the max number of users have been logged in, no further logins should be allowed.
    for user in users:
        result = um_utils.login(user)
        if (result == 0 or result == 1):
            user.loggedin = True 
        count = db_utils.getNumberOfActiveUsers(connection, cur)
        print '\tNumber of active users (max: %d): %d' % (maxManagers, count)
        if (count > maxManagers):
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