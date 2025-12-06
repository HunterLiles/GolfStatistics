CREATE OR ALTER PROCEDURE InsertRound
    @RoundScore SMALLINT,
    @CourseName VARCHAR(100),
    @RoundDate  DATETIME = NULL
AS
BEGIN
    DECLARE @RoundID    INT
    DECLARE @CourseID   INT
    SET @RoundID    = (SELECT MAX(RoundID) FROM GolfRound)
    SET @CourseID   = (SELECT CourseID FROM Course WHERE CourseName = @CourseName)

    IF @CourseID IS NULL
        RAISERROR ('Course not found', 16, 1)

    IF @RoundDate IS NULL
        SET @RoundDate = GETDATE()

    IF @RoundID IS NOT NULL
        SET @RoundID = @RoundID + 1
    ELSE
        SET @RoundID = 1

    INSERT INTO GolfRound(RoundID, RoundDate, RoundScore, CourseID)
    VALUES (@RoundID,
            @RoundDate,
            @RoundScore,
            @CourseID)
END

EXEC InsertRound 92, 'Graywood', '2025-10-03'


