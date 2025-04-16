using System;

public interface IPerson
{
    void DisplayInformation();
}

class Student : IPerson
{
    protected string studentName;
    protected int studentID;
    protected int age;

    public Student(string studentName, int studentID, int age)
    {
        this.studentName = studentName;
        this.studentID = studentID;
        this.age = age;
    }

    
    public string StudentName
    {
        get { return studentName; }
        set { studentName = value; }
    }

    public int StudentID 
    {
        get { return studentID; }
        set { studentID = value; }
    }

    public int Age 
    {
        get { return age; }
        set { age = value; }
    }

    public virtual void DisplayInformation()
    {
        Console.WriteLine($"Name: {studentName}, ID: {studentID}, Age: {age}");
    }

    public (string, int, int) GetStudentInfo()
    {
        return(studentName, studentID, age);
    }
}

class CollegeStudent : Student
{
    protected string subject;
    protected int average;

    public CollegeStudent(string studentName, int studentID, int age, string subject, int average)
        : base(studentName, studentID, age)
    {
        this.subject = subject;
        this.average = average;
    }

    public override void DisplayInformation()
    {
        base.DisplayInformation();  
        Console.WriteLine($"Subject: {subject}, Average: {average}");
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Enter Student Name: ");
        string studentName = Console.ReadLine();
        Console.WriteLine("Enter Student ID: ");
        int studentID = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter Age: ");
        int age = int.Parse(Console.ReadLine());
        Console.WriteLine("Enter Subject: ");
        string subject = Console.ReadLine();
        Console.WriteLine("Enter Average: ");
        int average = int.Parse(Console.ReadLine());

        Student student1 = new CollegeStudent(studentName, studentID, age, subject, average);
        student1.DisplayInformation();
        student1.Age = 12;
        student1.StudentName = "tom hanks";
        student1.DisplayInformation();
    }
}
