CREATE OR ALTER PROCEDURE HCCalculation
AS
    BEGIN
        DECLARE @Handicap INT
        SELECT @Handicap = AVG(RoundScore) - 72 FROM (SELECT TOP 10 RoundScore FROM GolfRound ORDER BY RoundDate DESC) AS RecentRounds

        SELECT 'Your HC is: ' + CAST(@Handicap AS VARCHAR(10)) AS Result;
    END