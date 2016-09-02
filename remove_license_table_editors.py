###############################################################################################
#                                                                                             # 
# remove_license_table_editors.py                                                            #
#                                                                                             # 
# Tests that no editors can log in when the license table has been deleted.                   #
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
    testFailed = 0
    
    # Set up connection to database
    connection = db_utils.connectToDb()    
    cur = connection.cursor()
    
    # Delete all existing licenses
    db_utils.deleteAllLicenses(connection, cur)
    maxUsers = 0
    
    # Delete the license table from the database
    db_utils.deleteLicencesTable(connection, cur)
    
    # Get the number of users already logged in
    count = db_utils.getNumberOfActiveUsers(connection, cur)
    
    print 'Max users allowed: %d' % maxUsers
    print 'Number of users already logged in: %d' % count
    print 'Opening browsers........'

    for editor in editors:
        # For each editor, create a user object and add object to users list
        users.append(um_utils.user(editor, 'quantel@'))
       
    # Keep trying to log in each of the editors. If any editor can log in, the test has failed.
    for user in users:
        result = um_utils.login(user)
        if (result == 0):
            # User has managed to log in successfully
            user.loggedin = True 
            testFailed = 1
            print 'Test Failed: User successfully logged in.'

    print 'Sleeping for 10 secs.................'
    time.sleep( 10 )
    
    # Log out any users that were logged in and close all the browsers
    for user in users:
        if (user.loggedin == True):
            um_utils.logout(user)
            user.loggedin = False
        time.sleep( 1 )
        um_utils.closeBrowser(user)
        
    # Re-create the license table and install a five user license
    db_utils.createLicencesTable(connection, cur)
    maxUsers = db_utils.addFiveUserLicense(connection, cur)
    print 'License installed for %d users' % maxUsers
    
    # Close connection to database
    db_utils.closeConnection(connection, cur) 
    
    # Print test result
    if (testFailed == 1):
        print '************ Test Failed ************'
    else:
        print '************ Test Passed ************'