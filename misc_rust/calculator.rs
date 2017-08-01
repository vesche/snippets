use std::io;

fn main() {
    println!("Calculator!");
    println!("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit");
    
    let x = 10;
    let y = 5;
    
    loop {
        println!("What would you like to do?");
        let mut choice = String::new();
        io::stdin().read_line(&mut choice);
        
        if choice.trim() == "1" {
            println!("{}", add(x, y));
        }
        else if choice.trim() == "2" {
            println!("{}", subtract(x, y));
        }
        else if choice.trim() == "3" {
            println!("{}", multiply(x, y));
        }
        else if choice.trim() == "4" {
            println!("{}", divide(x, y));
        }
        else if choice.trim() == "5" {
            break;
        }
        else {
            println!("Invalid choice!");
        }
    }
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}

fn subtract(x: i32, y: i32) -> i32 {
    x - y
}

fn multiply(x: i32, y: i32) -> i32 {
    x * y
}

fn divide(x: i32, y: i32) -> i32 {
    x / y
}