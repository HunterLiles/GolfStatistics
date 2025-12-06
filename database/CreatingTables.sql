CREATE TABLE Course
(
    CourseID          INT PRIMARY KEY,
    CourseName        VARCHAR(100),
    CourseDescription VARCHAR(255),
    CoursePar         SMALLINT
);


CREATE TABLE GolfRound
(
    RoundID    INT PRIMARY KEY,
    RoundDate  DATE DEFAULT GETDATE(),
    RoundScore SMALLINT,
    CourseID   INT REFERENCES Course (CourseID)
);