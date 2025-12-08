CREATE OR ALTER PROCEDURE HCCalculation
AS
    BEGIN
        DECLARE @Handicap INT
        SELECT @Handicap = AVG(RoundScore) - 72 FROM (SELECT TOP 10 RoundScore FROM GolfRound ORDER BY RoundDate DESC) AS RecentRounds

        -- This is written as a select and not a print because Streamlit wants a table and not
        -- A print statement. So, I made a temporary table that Streamlit can take from for the information.
        SELECT 'Your HC is: ' + CAST(@Handicap AS VARCHAR(10)) AS Result;
    END