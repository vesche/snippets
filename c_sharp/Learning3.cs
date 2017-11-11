using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            // file io
            StreamReader myReader = new StreamReader("foo.txt");
            string line = "";

            while (line != null)
            {
                line = myReader.ReadLine();
                Console.WriteLine(line);
            }

            myReader.Close();

            // more string stuffs
            string fun = "";
            string[] stuff = new string[] { "this", "that", "other" };
            foreach (string thing in stuff)
            {
                fun += "---" + thing;
            }
            Console.WriteLine(fun);

            // because oop s.Whatever has fun things
            Console.WriteLine(fun.Substring(5, 10));
            Console.WriteLine(fun.Length);

            // datetime
            DateTime dt = DateTime.Now;
            Console.WriteLine(dt);
            // dt object now has fun things dt.Whatever
            Console.WriteLine(dt.ToLongDateString());
            Console.WriteLine(dt.AddDays(20));
            Console.WriteLine(dt.AddHours(3).ToLocalTime());
            // ESR told me never to never approach programming like a plumber
            // in a hardware store- forgive me father for i have sinned

            // using the Car class below
            Car myNewCar = new Car();
            myNewCar.Make = "Ford";
            myNewCar.Model = "Fusion";
            myNewCar.Year = 2013;
            myNewCar.Color = "Silver";
            Console.WriteLine("{0} {1} {2} {3}", myNewCar.Make, myNewCar.Model,
              myNewCar.Year, myNewCar.Color);

            // format string coolness
            Console.WriteLine("{0:C}", myNewCar.determineMarketValue());
        }

        /*
        private static double determineMarketValue(Car car)
        {
            // not very exciting lol
            double carValue = 100.00;
            return carValue;
        }
        */
    }

    class Car
    {
        // prop <tab> <tab>
        public string Make { get; set; }
        public string Model { get; set; }
        public int Year { get; set; }
        public string Color { get; set; }

        public double determineMarketValue()
        {
            double carValue = 100.00;
            return carValue;
        }
    }
}
