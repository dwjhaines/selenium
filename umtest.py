import time
import um_utils
import db_utils
from selenium import webdriver
import pyodbc

if __name__ == "__main__":
    
    # Set up connection to database
    connection = db_utils.connectToDb()    
    cur = connection.cursor()
    
    '''# Delete all existing licenses
    db_utils.deleteAllLicenses(connection, cur)
    
    # Install license for five users
    db_utils.addFiveUserLicense(connection, cur)
    '''
    count = db_utils.getNumberOfActiveUsers(connection, cur)
    print 'Number of active users: %d' % count
    
    # Close connection to database
    db_utils.closeConnection(connection, cur) 
    
    # List of editors i.e. users that do not have admin rights
    editors = ['chloe.anderson', 'chloe.garcia', 'chloe.jackson', 'chloe.johnson', 'chloe.jones', 'chloe.lee', 'chloe.lewis', 'chloe.martin', 'chloe.martinez', 'chloe.miller', 'chloe.moore', 'chloe.robinson'] 
    # List of administrators i.e. users with administrator rights
    admins = ['avaa.johnsona', 'avaa.whitea', 'avac.whitec', 'avad.johnsond', 'avaf.whitef', 'avag.johnsong', 'avag.wilsong', 'avai.robinsoni', 'aval.wilsonl', 'avag.whiteg', 'avah.wilsonh', 'avam.robinsonm']
    # List of managers i.e. users with manager rights
    managers = ['maria.a', 'maria.b', 'maria.c', 'maria.d', 'maria.e', 'maria.f', 'maria.g', 'maria.h', 'maria.i', 'maria.j', 'maria.k', 'maria.l']
    # Empty list to be filled with user objects
    users = [] 
    '''
    for editor in admins:
        # For each editor, create a user object and add object to users list
        users.append(um_utils.user(editor, 'quantel@'))
       
    for user in users:
        result = um_utils.login(user)
        print 'Result = %d' % result
        if (result == 0 or result == 1):
            user.loggedin = True 

    print 'Sleeping for 10 secs.................'
    time.sleep( 10 )
    
    for user in users:
        if (user.loggedin == True):
            um_utils.logout(user)
            user.loggedin = False
        time.sleep( 1 )
        um_utils.closeBrowser(user)
        
    test_valid_license_editors.py      
    test_valid_license_admins.py
    test_valid_license_managers.py
    test_no_license_editors.py
    test_no_license_admins.py
    test_no_license_managers.py
    test_incorrect_ip_address_editors.py
    test_incorrect_ip_address_admins.py
    test_incorrect_ip_address_managers.py
    test_editor_remove_license.py
    test_admin_remove_license.py
    test_manager_remove_license.py
    test_license_not_yet_valid_editors.py
    test_license_not_yet_valid_admins.py
    test_license_not_yet_valid_managers.py
    test_license_expired_admins.py
    test_license_expired_editors.py
    test_license_expired_managers.py
    test_license_invalid_version_editors.py
    test_license_invalid_version_admins.py
    test_corrupted_license_editors.py
    test_corrupt_license_admins.py
        
        
    '''