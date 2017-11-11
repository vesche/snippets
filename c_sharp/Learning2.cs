using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Testing
    {

        private static string superSecretFormula()
        {
            return "Hello, world!";
        }

        private static string newSecretForumala(string name)
        {
            return String.Format("Hello, {0}!", name);
        }

        static void Main(string[] args)
        {
            string myValue = superSecretFormula();
            Console.WriteLine(myValue);

            Console.WriteLine(newSecretForumala("Jackson"));

            string foo = "bar";

            if (foo == "bar")
            {
                Console.WriteLine("1");
            }
            else if (foo == "test")
            {
                Console.WriteLine("2");
            }
            else
            {
                Console.WriteLine("3");
            }


            // integer array

            /*
            int[] numbers = new int[5];
            numbers[0] = 4;
            numbers[1] = 8;
            numbers[2] = 15;
            numbers[3] = 16;
            numbers[4] = 23;
            */

            int[] numbers = new int[] { 4, 8, 15, 16, 23, 42 };

            // numbers[1] = 1337;
            Console.WriteLine(numbers[1].ToString());

            string[] names = new string[] { "Austin", "Jackson", "this" };
            // Console.WriteLine(names[2]);

            // foreach! god bless python style for loops
            foreach (string name in names)
            {
                Console.WriteLine(name);
            }

            string stuff = "The quick brown dog jumped over the lazy dog.";

            // split into letters
            char[] charArray = stuff.ToCharArray();
            Array.Reverse(charArray);
            foreach (char test in charArray)
            {
                Console.Write(test);
            }
            Console.WriteLine();

        }

    }
}
