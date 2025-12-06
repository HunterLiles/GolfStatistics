CREATE OR ALTER PROCEDURE InsertCourse
    @CourseName         VARCHAR(100),
    @CourseDescription  VARCHAR(255),
    @CoursePar          SMALLINT
AS
BEGIN
    DECLARE @CourseID INT
    SET @CourseID = (SELECT MAX(CourseID) FROM Course)

    IF @CourseID IS NOT NULL
        SET @CourseID = @CourseID + 1
    ELSE
        SET @CourseID = 1

    IF (SELECT CourseName FROM Course WHERE CourseName = @CourseName) IS NULL
        BEGIN
            INSERT INTO Course (CourseID, CourseName, CourseDescription, CoursePar)
            VALUES (@CourseID,
                    @CourseName,
                    @CourseDescription,
                    @CoursePar);
        END
        ELSE
            PRINT 'Course already exists.'
        RETURN
END

EXEC InsertCourse 'Frasch', 'Sulphur course', 72