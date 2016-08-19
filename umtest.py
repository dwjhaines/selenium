import time
import um_utils
from selenium import webdriver

if __name__ == "__main__":
    # List of editors i.e. users that do not have admin rights
    editors = ['chloe.anderson', 'chloe.garcia', 'chloe.jackson']#, 'chloe.johnson', 'chloe.jones', 'chloe.lee', 'chloe.lewis', 'chloe.martin', 'chloe.martinez', 'chloe.miller', 'chloe.moore', 'chloe.robinson'] 
    # List of administrators i.e. users with administrator rights
    admins = ['avaa.johnsona', 'avaa.whitea', 'avac.whitec', 'avad.johnsond', 'avaf.whitef', 'avag.johnsong', 'avag.wilsong', 'avai.robinsoni', 'aval.wilsonl', 'avag.whiteg', 'avah.wilsonh', 'avam.robinsonm']
    # Empty list to be filled with user objects
    users = [] 
    
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

