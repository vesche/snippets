using System;

namespace HelloWorld
{
    class FirstProgram
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, world!");

            int x = 10;
            Console.WriteLine(x);

            string name = "Jackson";
            Console.WriteLine("My name is " + name + " and my favorite number is " + x);

            bool test = true;
            if (test) {
                Console.WriteLine("It's true!");
            }

            // shit works just like C
            for (int foo = 3; foo > 0; foo--)
            {
                Console.WriteLine(foo);
            }

            byte number;
            number = 12;
            Console.WriteLine(number);

            Shit();

            int someNumber = 10;
            while (someNumber > 0)
            {
                Console.Write(someNumber + " ");
                --someNumber;
            }
            Console.Write("\n");

            // gotta force this shit or it will become a double
            float money = 20.95f;
            char letter = 'A';
            Console.WriteLine("Some letter: " + letter + ", Some money: " + money);

            // implicit variable dec
            var firstName = "Austin";
            Console.WriteLine(firstName);

            // thanks jesus format strings
            Console.WriteLine("My first name is {0} and last name is {1}", firstName, name);

            // byte is a struct has cool shit in it
            Console.WriteLine("{0} {1}", byte.MinValue, byte.MaxValue);

            const float Pi = 3.14f;

            // user input
            string input = Console.ReadLine();
            Console.WriteLine("You enentered: " + input);

            // try & except conv
            try
            {
                var stuff = "1234";
                byte b = Convert.ToByte(stuff);
                Console.WriteLine(b);
            }
            catch
            {
                Console.WriteLine("Error!");
            }

            int firstNumber = 12;
            int secondNumber = 100;
            Console.WriteLine(firstNumber + secondNumber);
            Console.WriteLine(firstNumber - secondNumber);
            Console.WriteLine(firstNumber * secondNumber);
            Console.WriteLine(firstNumber / secondNumber); // floor div
            Console.WriteLine((float)firstNumber / (float)secondNumber); // conv to float on fly

            // logic same as C ... ! not == equal != not equal && and || or
            Console.WriteLine(!(firstNumber == secondNumber));
        }

        static void Shit()
        {
            Console.WriteLine("shit");
        }
    }
}
