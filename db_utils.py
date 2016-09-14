import pyodbc

def connectToDb():
    # Returns a connection to the sql databse specified in the connection string below
    connection = pyodbc.connect(r'Driver={SQL Server}; Server=10.165.250.251\MSSQL1; Database=session_db; uid=sa; pwd=0sql0')
    return connection
  
def closeConnection(connection, cur):
    # Closes the specified connection 
    cur.close()
    del cur
    connection.close()
    
def deleteAllLicenses (connection, cur):
    # Deletes all licenses from the database
    sql_command= 'DELETE FROM [session_db].[dbo].[Licenses]'
    cur.execute(sql_command)
    connection.commit()
    
def addFiveUserLicense (connection, cur):
    # Adds a license for five users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-in-house-only-5-users----------------814755e6-01f2-c7e7-5971-cac39bde5fbb525b7c9c-0dab-45b3-ad29-8d282ef2cb81fae144dd-d44874a6b-a28a-7d330028771fae144e06-63ff-4d69-b087-337badbb7c52ca7ca81f-5069-4b61-8799-d58c5e9e9d459f42d31f-cccf-426b-b839-e3c3a9c32fba5cf15e77-b64f-4de9-b88e-114fba3fb67a755c4441-b3de-4a48-a20f-3bd142cd2d8f566fb6a8-3b20-451b-b74f-06da965efbe5e85a72a9-e941-465d-a73b-275205fb55ae3a265fb4-ea8e-45ba-8a9e-d12a3143497779389c8b-8cf9-49f7-84a5-a56b7529771fa003f339-614d-431b-a15c-6e76d6654efa80c80a5e-1772-411d-bbe5-ad8f0fa95439a4c86fdf-bb50-40c8-9f79-3c98c34461ea6b42520a-91a9-4fd3-9558-d6fc6d6bd42cd9ea5b42-de91-4cdd-81ec-820bd824c03f29b6c5ae-c6b8-462c-9e16-b53c1ecddf64543e2763-9548-4f7f-be53-2e104a0b337667b94404-55ad-4d0d-89c7-b2cbae172d3f62fc523d-656d-41e9-bdeb-eabaed3d3da3c53d8cb5-fb2f-408f-970c-a6267740b9ce02a4aec5-199a-48e5-b7a3-cb3969480e6a916f07c5-0733-4790-82ca-beeb67bbdb598f4e3261-3ffa-4237-b95d-d11e6a897fa58b0402e1-e94a-4013-904a-42983a3fd5dbcc769362-5c42-4fae-a7dd-55b5133e8002')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 5
    
def addTenUserLicense (connection, cur):
    # Adds a license for ten users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-in-house-only-10-users---------------973077d9-29b7-9d9e-424c-5552c8df2e46976209bd-b906-4ce2-9565-e02a2c26eee1ce237ac6-c448744df-98f5-4fc2d36aad1ce237a06a-378d-41a4-ba19-974aa5aafb4ab9fba00b-b99e-445e-b213-f35ba4b60c09027071f7-d2f0-47d2-ad94-0a73358212f8ea6365b7-f43d-4355-afe1-48e6aecc0b6b14f110b5-cca3-4db8-9b20-a8bc6022d89878572c28-8f18-49ec-95be-30f574d6f184110b6991-c874-4f05-8517-6d1fb43fd751120944a8-074e-4d89-8383-f12f00cd1654aada37b6-613e-4fdd-a7a9-0ec8035a47920e74353d-852e-4b1f-b991-9407d0f2721b19675c7d-6e12-400c-9bb9-02ddd6e83673d972c1f0-2077-42bb-8139-ee01a0693b83151703e0-0920-4865-b970-ae9a39418096cbd91e96-2f25-485b-8176-dc88810b9fcd6d1a761e-748a-4ce9-a73b-6041506470095b1b515c-b0a8-435a-910e-fe45196bbe1254c5a82d-85eb-4feb-ad29-6a77762b2476826e94f4-059d-408f-81bd-bae609663e4d1a1edebc-b6ea-49af-87ba-86ee29254cd87c40c1ce-615f-475e-a046-4a8bec48910350011c9b-bc6b-452c-86d3-18dae8f8bfaa78e8932d-309e-4d19-87ec-bf5fedd24f69ef192fe7-b98f-4da3-a462-ee15f0fcc77b5ca2b68b-8a8e-4b01-a2cd-de1725de4002')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of users that can log in
    return 10
    
def addUserLicenseIncorrectIPAddress (connection, cur):
    # Adds a license with an incorrect IP address. i.e. one that is not 10.165.250.251
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-incorrect-IP-Address-----------------4a6f1d7d-0331-91fa-8140-eadca22908db45c3be61-e6bc-4d60-8c09-132b221f28a12da716c7-044874502-8d19-5dd232ee4912da716b8d-a075-4d20-b3a1-38c6f36fd7987ed7f264-433d-4319-bff2-6447ab755f81d7699b71-07b7-404f-b9dc-1e646aeb4a742a55b0f4-ef21-41f5-bc43-7b5f271bdc94840b931e-e925-428f-9a09-cdc5ed8960551f619249-7c41-4127-ad07-4b333a37748f960b9026-3be1-4078-b1ea-89c9db1a674966a780a5-4fac-400b-8aec-650b93f07260e24e92e7-d39c-4f7a-9264-768463860f26f099d0c6-6758-4575-8469-94223f2fef22e2f4f7b4-1535-4bf4-b6bc-dc2a1a4f21e58ba5b52c-7ce0-4c43-b340-825d9a64987074d6fca4-dadf-446f-994b-1d1fdff6a161d488af8d-f8d3-40c1-8c36-16347dea1531b0dba558-6dca-4d21-a1b8-b794211e7e555ecd892c-9117-4f23-8364-4fa9b7e96d9db70f798f-85d4-484c-b356-671ad1b424261c4b4736-e61f-474a-8d0c-afb37c8bf3b0fa6e4cd3-dff6-40e6-82e9-80ac69ffe6196a381e73-6686-46a1-8be0-6d7f2e42da75b08f2bc0-d82b-4bed-81e9-ff67cd1777c3f242a67d-47fc-4e6f-b7a2-fdebadbfaf8566896187-89db-4e74-8f94-b52d8530364d1d1ea67f-7b04-4cd1-89e9-c9cb4606d002')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseNotStarted (connection, cur):
    # Adds a license with a start date in the future. This license starts on 1st Sept 2016. Will need to be changed for tests after that date!!!!!!
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-Start-Date-Oct-1st-2016--------------6a5a53a5-9c4d-2a31-6dd8-94c23c90cd86cd533f37-0c5e-4465-9fb8-08b5275065417f5b509c-12ad74415-9828-099284a28317f5b50976-b4db-4cd1-be5d-c008d58df97a9cf9d0c7-7166-4cde-a012-f3d3f70f1fef49e0621a-794e-4d7a-a67c-1e5d52f146e3e7139295-7275-495a-a856-936e936665a6dcb42a8e-8d16-45a4-beed-92db6a626657e84a3111-96fb-4e10-9d94-1ccb525839aecdc6c1fa-5047-493f-a05b-fffbc6385675bc941bb7-720a-4426-81fd-ba4dcea1930dfe40c14d-ab2b-43aa-8e21-7e0df2bf9b1ccd47f373-7a24-498d-8584-9a629464f85a7a8f1f2d-f44b-48df-987f-6e048c25f105964ba43f-09ec-41b9-a8fc-e0ea5069366fa1c4b821-4817-414b-91b1-db73a59ca487b1771375-d85c-47f6-ae3c-d0521e3864b649096b5d-5557-4e68-874b-bb933c970dac0015c61f-0e92-4418-8995-750dafcdd1bdb60a8e97-ef28-4cf9-9eba-bc994357ef140f83656b-125b-43be-9254-4eb7c30c8fbc248ed822-7eeb-42bb-a1bc-07fc69537736199806b2-27b4-4ba4-85e0-b98d761397d49a6dd9da-e9a3-443b-b85a-0110c6b592795e3f096d-d83c-4e35-93ff-2bf111dd40f7c23496f5-5d56-4b4f-9794-560ba950caf03e12f389-8cf1-4f0c-bbb3-daa9cc247002')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseExpired (connection, cur):
    # Adds a license that has expired (ended 25th Aug 2016)
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-End-Date-Aug-25th-2016---------------e7b9a059-3050-54c4-cb03-4c80cf792c3d227cc1af-f56f-4efe-b848-7df52b340161bef4a2ff-c164f4a80-83b6-8f72b45afd1bef4a2ad6-ff65-492c-b192-af8a4ca56af1b46b4727-5a59-4339-8266-1c8549a28bd797ba2ab3-cc28-4a00-9e50-c6b395f23014e9dd2b1b-a8ef-499d-9124-dfe493b71fefc0ded0a0-cfdf-434a-9d6e-bf1522e6af59be4f42b4-3157-4e30-afe0-a84a9a1d47845ffc0db3-cc5b-4732-b1d4-b0f7a104c14fce24326c-d46d-4c7d-93ac-e9ab5f5d54e984b2d9dd-615f-40ef-af58-2cca2ba2531162278286-7e10-4fac-8f57-e35395e94ef5fac20682-481f-4c73-af0b-650c547d8638d13e5f30-21c5-45dc-908e-6a0eeb7638a08c662a74-0044-4012-bbd3-1f4fefdaebc33ada7601-fe94-4f31-a111-a9fcf68937b5e5ddc5d8-6ffb-43f9-ba26-1d28d6a288129e9510ec-dd1c-46de-9d8c-3604891e796f73631fdd-33f4-46b3-abe6-3ddd00ad83062d37d3a6-d59b-4987-8826-3decca253d971b41898c-95a5-434f-b2a0-9cf88b309871cf79f132-5966-43bf-8b88-32d1419f544e0719382d-7ce7-4e99-986a-ce29e6aea0fa2cf682fa-1301-4f36-9147-74eb4fe0b41af2173aa2-b95d-4a0f-9483-c6bb437a478c3fb60e5f-30e4-4468-88c6-66188e12f002')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0    
    
def addUserLicenseInvalidVersion (connection, cur):
    # Adds a license with the version number changed to be invalid. Version number set to 005
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-Invalid-Version-Number---------------a7b43259-cc8b-52f5-c701-c6506c490eb767c22eed-e0fc-4dfb-9058-13642aaa8871b65d135e-d44874375-9cf3-ae62bba4461b65d13592-e6f5-4fb7-b0bb-17ba19a23abeb13b142f-4e52-4394-8de5-81f33130d0a297ea8602-4a2f-4646-bb6a-5b7caadbcca8bd13b805-6d5a-49ba-9fe6-3c399359913e5a35dc4c-f3fc-4033-9f61-12df69b0e113e87c5ad4-2002-491f-b06c-f715533f2ea238af4437-a376-4b94-aa0c-a269f44ac78fbdfb2086-4dfe-49af-8427-7c9bc66389473d01295d-7489-4615-b9dc-dfa8e66aadaa638853bf-d7d2-477e-9d59-545f6d45efc563478df8-df2e-45e0-8c0a-e4d9e6048772fc7d687f-bcc1-4160-be94-e1e7f7d744dc01b1cfb1-a785-4146-af1b-44fb180fea0763265046-cc38-483a-bded-eb662c3bf3dae22b9b2c-22ba-45d1-b71b-2b00281bd8dcfff7e3a6-89af-4d9d-bde0-9e6503f90a22155037ae-b131-4a1c-a704-363820eaf446fa2cf431-bcb2-4c41-8049-1c9f73075e2c7cc297e3-5c7e-43d8-a0a5-2168081f440b8253a7a3-9b60-4d55-abe4-0b0e683352f443addf52-f55c-43eb-a387-b306451396e4fc650d04-3f20-4b29-b0c6-db9e4281af467542035b-e67e-424b-8bd9-6e8cff0365cc54a01281-de6a-4d7b-ae60-f61d0305e005')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def addUserLicenseCorrupted (connection, cur):
    # Adds a license with random characters altered
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-Corrupted-License--------------------954bc6be-4083-486d-5df6-a48adfb85296ba4c1e3d-3079-4a6d-9102-c5cd1dbe2340e798f441-5448749e3-a957-b6e1ece0270e798f42bc-c363-4a53-8246-8da5565605fb650651ef-5599-48ed-8b96-21aa216fd7480ea903d5-ec0f-4ec6-97da-62784764c9d27f5b99cc-7029-483f-b330-e8a82b0b6b9b11dcdce4-0888-4f80-b306-b93c011b0cda3e7c9098-34bc-40f1-be41-62a627c73274f4b67dc0-d4ae-44d7-aa7f-85ee307f2ac740172412-c7f9-4035-8cda-48accde91d0d3848646b-661f-4283-8858-bcf0a389a25f765d6b3d-3a81-4c4b-be81-786efcb36c0b7f9ab7ec-ef17-40c7-b4c3-3e5bb554af533efac88f-ab13-45ff-b413-4cb99ee193ce65308675-979d-43ec-8da9-2c836e5918299f94056e-9cea-43b0-be5f-b67d43ebab6cfaa705ce-6b80-4644-a175-9ad69307276b1b2b1f34-a349-42b0-b6f5-d8fc1f4dae19eb2c9cc9-d703-47b1-b6c2-f7bd2dc31bd99cb3928d-c32c-4ffc-913c-1e5ec6cc7bc5bee4625d-4119-42d9-8170-bb6a44aa8897b64b2394-d69b-4ced-9505-1c28f807e303743124c4-c1bc-4fc9-b79b-f953193d2f568ffc3c01-e47d-444a-81d3-a0df5d34d7cef4ded1bf-20b5-43a0-a939-4e69629742938c5f679e-0728-4bc6-8aa7-479fc2b7f002')'''
    cur.execute(sql_command)
    connection.commit()
    # Return
    return 0
    
def getNumberOfActiveUsers (connection, cur):
    # Returns the number of active users from the database
    sql_command= '''
    SELECT COUNT(*) 
    FROM [session_db].[dbo].[ActiveSessions]
    WHERE forcelogout = 0'''
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    return count

def getMaxConcurrentUsers (connection, cur):
    # Returns the max number of concurrent users from the database
    sql_command= """
    SELECT [Value]
    FROM [session_db].[dbo].[UMSettings]
    WHERE Setting = 'MaxConcurrentUsers'"""
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    return count
    
def isUserLoggedIn (connection, cur, user): 
    username = user.username
    sql_command= """
    SELECT COUNT(*)
    FROM [session_db].[dbo].[ActiveSessions]
    WHERE username = '""" + username + """'
    AND forcelogout = 0"""
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    if (count == 1):
        return True
    else:
        return False

def deleteLicencesTable (connection, cur): 
    # Delete the license table if it exists
    sql_command= """
    IF OBJECT_ID('[session_db].[dbo].[Licenses]', 'U') IS NOT NULL
    DROP TABLE [session_db].[dbo].[Licenses];"""
    cur.execute(sql_command)    
    connection.commit()

def createLicencesTable (connection, cur): 
    sql_command= 'CREATE TABLE [session_db].[dbo].[Licenses](license NCHAR(1024) NULL)'
    cur.execute(sql_command)    
    connection.commit()