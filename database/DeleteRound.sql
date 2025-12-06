CREATE OR ALTER PROCEDURE DeleteRound @RoundID    INT,
                                      @RoundDate  DATETIME,
                                      @CourseName VARCHAR(50)
AS
BEGIN
    DECLARE @CourseID   INT
    SET @CourseID   = (SELECT CourseID FROM Course WHERE CourseName = @CourseName)
    SET @RoundDate  = CONVERT(DATETIME, @RoundDate, 101)

    IF @CourseID IS NULL
        RAISERROR ('Course not found', 16, 1)
    IF @RoundID IS NULL
        RAISERROR ('Round not found', 16, 1)
    IF @RoundDate IS NULL
        RAISERROR ('Round date not found', 16, 1)

    IF @RoundID IS NOT NULL AND @RoundDate IS NOT NULL AND @CourseName IS NOT NULL
           DELETE GolfRound WHERE RoundID = @RoundID AND RoundDate = @RoundDate AND CourseID = @CourseID
END