using System;

// initialize variables - graded assignments 
int examAssignments = 5;

// Student names
string[] studentNames = new string[] { "Sophia", "Andrew", "Emma", "Logan" };

int[] sophiaScores = new int[] { 90, 86, 87, 98, 100, 94, 90 };
int[] andrewScores = new int[] { 92, 89, 81, 96, 90, 89 };
int[] emmaScores = new int[] { 90, 85, 87, 98, 68, 89, 89, 89 };
int[] loganScores = new int[] { 90, 95, 87, 88, 96, 96 };

int[] studentScores = new int[10];
string currentStudentLetterGrade = "";

Console.WriteLine("Student\t\tExam Score\tOverall Grade\tExtra Credit\n");

foreach (string name in studentNames)
{
    string currentStudent = name;  

    if (currentStudent == "Sophia")
    {        
        studentScores = sophiaScores;
    }
    else if (currentStudent == "Andrew")
    {        
        studentScores = andrewScores;
    }
    else if (currentStudent == "Emma")
    {        
        studentScores = emmaScores;
    }
    else if (currentStudent == "Logan")
    {        
        studentScores = loganScores;
    }
    else
        continue;

    int sumAssignmentScores = 0;
    int sumAssignmentScoresWithExtraCredit = 0;
    int extraCredit = 0;
    
    decimal currentStudentGrade = 0;
    decimal overallStudentGrade = 0;
    decimal extraCreditValue = 0;

    int gradedAssignments = 0;
        
    foreach (int score in studentScores)
    {
        gradedAssignments++;
        if (gradedAssignments <= examAssignments)
        {
            sumAssignmentScores += score;
            sumAssignmentScoresWithExtraCredit += score;
        }
        else
        {
            sumAssignmentScoresWithExtraCredit += score / 10;
            extraCredit += score/10;

        }

    }

    currentStudentGrade = (decimal)sumAssignmentScores / examAssignments;
    overallStudentGrade = (decimal)sumAssignmentScoresWithExtraCredit / examAssignments;
    extraCreditValue = (decimal)extraCredit / examAssignments;

    if (overallStudentGrade >= 97)
    {
        currentStudentLetterGrade = "A+";
    }
    else if (overallStudentGrade >= 93)
    {
        currentStudentLetterGrade = "A";
    }
    else if (overallStudentGrade >= 90)
    {
        currentStudentLetterGrade = "A-";
    }
    else if (overallStudentGrade >= 87)
    {
        currentStudentLetterGrade = "B+";
    }
    else if (overallStudentGrade >= 83)
    {
        currentStudentLetterGrade = "B";
    }
    else if (overallStudentGrade >= 80)
    {
        currentStudentLetterGrade = "B-";
    }
    else if (overallStudentGrade >= 77)
    {
        currentStudentLetterGrade = "C+";
    }
    else if (overallStudentGrade >= 73)
    {
        currentStudentLetterGrade = "C";
    }
    else if (overallStudentGrade >= 70)
    {
        currentStudentLetterGrade = "C-";
    }
    else if (overallStudentGrade >= 67)
    {
        currentStudentLetterGrade = "D+";
    }
    else if (overallStudentGrade >= 63)
    {
        currentStudentLetterGrade = "D";
    }
    else if (overallStudentGrade >= 60)
    {
        currentStudentLetterGrade = "D-";
    }
    else
    {
        currentStudentLetterGrade = "F";
    }

    Console.WriteLine($"{currentStudent}\t\t" + $"{currentStudentGrade}\t\t" +  overallStudentGrade + $"\t{currentStudentLetterGrade}" + $"\t{(int)currentStudentGrade} ({extraCreditValue} pts)");
}

Console.WriteLine("Press the Enter key to continue");
Console.ReadLine();
