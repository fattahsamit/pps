Random random = new Random();
int coin = random.Next(0, 2);

Console.WriteLine($"{(coin == 0 ? "Heads" : "Tails")}");