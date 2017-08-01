
fn main() {
    let mut x = 5;
    println!("The value of x is {}", x);
    x = 6;
    println!("The value of x is {}", x);

    const MAX_POINTS: u32 = 100_000;
    println!("{}", MAX_POINTS);
    
    
    x += 1;
    println!("The value of x is {}", x);
    
    let name = "Austin";
    println!("The length of Austin is {}", name.len());
    
    // you cannot mutate a variables type
    // let mut name = "Austin";
    // name = 3; // THIS WILL ERROR
    
    let numb: u32 = "42".parse().expect("Not a number.");
    println!("numb: {}", numb);
    
    let thousand = 1_000;
    println!("one more than a thousand is {}", thousand+1);
    
    let a = 2.0;
    let b: f32 = 3.0;
    println!("a: {}, b: {}", a, b);
    
    let sum = 5 + 10;
    let dif = 5 - 10;
    let pro = 5 * 10;
    let quo = 5 / 10;
    let rem = 5 % 10;
    println!("sum {} dif {} pro {} quo {} rem {}", sum, dif, pro, quo, rem);
    
    let t = true;
    let f: bool = false;  //explicit
    println!("t is {} and f is {}", t, f);
    
    let tup = (8, 9, 10);
    let (x, y, z) = tup;
    println!("{} {} {}", x, y, z);
    
    let mut i = 0;
    let a = [0, 1, 2, 3, 4, 5];
    loop {
        println!("{}", a[i]);
        i += 1;
        if i == 5 {
            break;
        }
    }
    
    let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                  "Sep", "Oct", "Nov", "Dec"];
    println!("{}", months[11]);
}
