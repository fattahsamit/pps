using System;

// initialize variables - graded assignments 
int currentAssignments = 5;

// Student names
string[] studentNames = ["Sophia", "Andrew", "Emma", "Logan"];

int[] sophiaScores =  [90, 86, 87, 98, 100];
int[] andrewScores = [92, 89, 81, 96, 90];
int[] emmaScores =  [90, 85, 87, 98, 68];
int[] loganScores =  [90, 95, 87, 88, 96];

Console.WriteLine("Student\t\tGrade\n");

foreach (string name in studentNames){
    if (name == "Sophia")
    {        
        int sophiaSum = 0;
        decimal sophiaScore;
        
        foreach (int score in sophiaScores)
        {
            sophiaSum += score;
        }

        sophiaScore = (decimal)sophiaSum / currentAssignments;

        Console.WriteLine($"{name}:\t\t" + sophiaScore + "\t?");
    }
    else if (name == "Andrew")
    {    
        int andrewSum = 0;
        decimal andrewScore;

        foreach (int score in andrewScores)
        {
            andrewSum += score;
        }

        andrewScore = (decimal)andrewSum / currentAssignments;

        Console.WriteLine($"{name}:\t\t" + andrewScore + "\t?");
    }
    else if (name == "Emma")
    {     
        int emmaSum = 0;
        decimal emmaScore;

        foreach (int score in emmaScores)
        {
            emmaSum += score;
        }

        emmaScore = (decimal)emmaSum / currentAssignments;

        Console.WriteLine($"{name}:\t\t" + emmaScore + "\t?");
    }
    else if (name == "Logan")
    {       
        int loganSum = 0;
        decimal loganScore;

        foreach (int score in loganScores)
        {
            loganSum += score;
        }

        loganScore = (decimal)loganSum / currentAssignments;

        Console.WriteLine($"{name}:\t\t" + loganScore + "\t?");
    }
}

Console.WriteLine("Press the Enter key to continue");
Console.ReadLine();
