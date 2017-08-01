
fn main() {
    println!("Hello, world!");
    let test = another_func(5, 6);
    println!("{}", test);
    
    println!("{}", plus_one(99));
    
    let high_five = fiver();
    println!("Did it work? {}", high_five);
}

fn another_func(x: i32, y: i32) -> i32 {
    println!("Another function! x: {} y: {}", x, y);
    x + y
}

fn plus_one(x: i32) -> i32 {
    x + 1
}

fn fiver() -> i32 {
    5
}