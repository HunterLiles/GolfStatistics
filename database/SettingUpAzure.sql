-- 1. Create the Login (Server Level)
CREATE LOGIN golfadmin WITH PASSWORD = '#Addison18';

-- 3. Create the User (Database Level)
CREATE USER golfadmin FOR LOGIN golfadmin;

-- 4. Give permissions
ALTER ROLE db_datareader ADD MEMBER golfadmin;
ALTER ROLE db_datawriter ADD MEMBER golfadmin;
ALTER ROLE db_ddladmin ADD MEMBER golfadmin;
GRANT EXECUTE ON SCHEMA::dbo TO golfadmin;
