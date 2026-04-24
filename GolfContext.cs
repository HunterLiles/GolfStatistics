using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

public class Course
{
    [Key]
    public int CourseID { get; set; }
    public required string CourseName { get; set; }
    public string? CourseDescription { get; set; }
    public short CoursePar { get; set; }
}

public class GolfRound
{
    [Key]
    public int RoundID { get; set; }
    public DateTime RoundDate { get; set; }
    public short RoundScore { get; set; }
    public int CourseID { get; set; }
    public required Course Course { get; set; }
}

public class GolfContext : DbContext
{
    public GolfContext(DbContextOptions<GolfContext> options)
        : base(options) { }

    public DbSet<Course> Courses { get; set; }
    public DbSet<GolfRound> GolfRounds { get; set; }
}
