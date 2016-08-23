/****** Select list of administrators  ******/
SELECT TOP 1000 [session_db].[dbo].[aspnet_Users].[UserName]
      ,[session_db].[dbo].[aspnet_Roles].[RoleName]
  FROM [session_db].[dbo].[aspnet_UsersInRoles]
  INNER JOIN [session_db].[dbo].[aspnet_Users]
  ON [session_db].[dbo].[aspnet_UsersInRoles].UserId=[session_db].[dbo].[aspnet_Users].UserId
  INNER JOIN [session_db].[dbo].[aspnet_Roles]
  ON [session_db].[dbo].[aspnet_Roles].[RoleId]=[session_db].[dbo].[aspnet_UsersInRoles].[RoleId]
  WHERE [session_db].[dbo].[aspnet_Roles].[RoleName]='admin'
  ORDER BY [session_db].[dbo].[aspnet_Users].[UserName]
  