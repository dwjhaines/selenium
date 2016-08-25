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
    # Return the number of licenses added
    return 5
    
def addTenUserLicense (connection, cur):
    # Adds a license for ten users. Returns the number of licenses that have been added
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-in-house-only-10-users---------------973077d9-29b7-9d9e-424c-5552c8df2e46976209bd-b906-4ce2-9565-e02a2c26eee1ce237ac6-c448744df-98f5-4fc2d36aad1ce237a06a-378d-41a4-ba19-974aa5aafb4ab9fba00b-b99e-445e-b213-f35ba4b60c09027071f7-d2f0-47d2-ad94-0a73358212f8ea6365b7-f43d-4355-afe1-48e6aecc0b6b14f110b5-cca3-4db8-9b20-a8bc6022d89878572c28-8f18-49ec-95be-30f574d6f184110b6991-c874-4f05-8517-6d1fb43fd751120944a8-074e-4d89-8383-f12f00cd1654aada37b6-613e-4fdd-a7a9-0ec8035a47920e74353d-852e-4b1f-b991-9407d0f2721b19675c7d-6e12-400c-9bb9-02ddd6e83673d972c1f0-2077-42bb-8139-ee01a0693b83151703e0-0920-4865-b970-ae9a39418096cbd91e96-2f25-485b-8176-dc88810b9fcd6d1a761e-748a-4ce9-a73b-6041506470095b1b515c-b0a8-435a-910e-fe45196bbe1254c5a82d-85eb-4feb-ad29-6a77762b2476826e94f4-059d-408f-81bd-bae609663e4d1a1edebc-b6ea-49af-87ba-86ee29254cd87c40c1ce-615f-475e-a046-4a8bec48910350011c9b-bc6b-452c-86d3-18dae8f8bfaa78e8932d-309e-4d19-87ec-bf5fedd24f69ef192fe7-b98f-4da3-a462-ee15f0fcc77b5ca2b68b-8a8e-4b01-a2cd-de1725de4002')'''
    cur.execute(sql_command)
    connection.commit()
    # Return the number of licenses added
    return 10
    
def addUserLicenseIncorrectIPAddress (connection, cur):
    sql_command= '''
    INSERT INTO [session_db].[dbo].[Licenses]
    VALUES ('PVG-standalone-incorrect-IP-Address-----------------4a6f1d7d-0331-91fa-8140-eadca22908db45c3be61-e6bc-4d60-8c09-132b221f28a12da716c7-044874502-8d19-5dd232ee4912da716b8d-a075-4d20-b3a1-38c6f36fd7987ed7f264-433d-4319-bff2-6447ab755f81d7699b71-07b7-404f-b9dc-1e646aeb4a742a55b0f4-ef21-41f5-bc43-7b5f271bdc94840b931e-e925-428f-9a09-cdc5ed8960551f619249-7c41-4127-ad07-4b333a37748f960b9026-3be1-4078-b1ea-89c9db1a674966a780a5-4fac-400b-8aec-650b93f07260e24e92e7-d39c-4f7a-9264-768463860f26f099d0c6-6758-4575-8469-94223f2fef22e2f4f7b4-1535-4bf4-b6bc-dc2a1a4f21e58ba5b52c-7ce0-4c43-b340-825d9a64987074d6fca4-dadf-446f-994b-1d1fdff6a161d488af8d-f8d3-40c1-8c36-16347dea1531b0dba558-6dca-4d21-a1b8-b794211e7e555ecd892c-9117-4f23-8364-4fa9b7e96d9db70f798f-85d4-484c-b356-671ad1b424261c4b4736-e61f-474a-8d0c-afb37c8bf3b0fa6e4cd3-dff6-40e6-82e9-80ac69ffe6196a381e73-6686-46a1-8be0-6d7f2e42da75b08f2bc0-d82b-4bed-81e9-ff67cd1777c3f242a67d-47fc-4e6f-b7a2-fdebadbfaf8566896187-89db-4e74-8f94-b52d8530364d1d1ea67f-7b04-4cd1-89e9-c9cb4606d002')'''
    cur.execute(sql_command)
    connection.commit()
    return 0
    
def getNumberOfActiveUsers (connection, cur):
    sql_command= '''
    SELECT COUNT(*) 
    FROM [session_db].[dbo].[ActiveSessions]
    WHERE forcelogout = 0'''
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    return count

def getMaxConcurrentUsers (connection, cur):
    sql_command= """
    SELECT [Value]
    FROM [session_db].[dbo].[UMSettings]
    WHERE Setting = 'MaxConcurrentUsers'"""
    cur.execute(sql_command)
    count = int(str(cur.fetchall()[0][0]))
    return count
    
    



