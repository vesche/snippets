use std::io;
use std::io::Write;
use std::thread;

const BANNER: &'static str = "
'||''|.   |''||''|     |    
 ||   ||     ||       |||   
 ||''|'      ||      |  ||  
 ||   |.     ||     .''''|. 
.||.  '|'   .||.   .|.  .||.
     Rust Text Adventure";

const HELP_TEXT: &'static str = "
n - move north
s - move south
e - move east
w - move west
q - quit the game
h - display this help text
i - inventory";

fn main() {
    // define map
    let mut map = [
    [" ","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_", "_","_","_"," "],
    ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ", " "," "," ","|"],
    ["|"," "," "," ","*"," "," "," "," "," "," ","*","*"," "," "," "," "," ", " "," "," ","|"],
    ["|"," "," "," ","*","*"," "," "," ","*","*","*","*","*"," "," "," "," ", " "," "," ","|"],
    ["|"," "," "," ","*","*","*"," "," "," ","*","*","*","*"," ","*","*","*", " "," "," ","|"],
    ["|"," "," "," "," "," ","*","*"," ","*","*","*"," ","*","*","*","*","*", " "," "," ","|"],
    ["|"," "," "," ","*","*","*","*","*","*","*","*"," "," ","*","*","*"," ", " "," "," ","|"],
    ["|"," "," "," ","*","*","*","*","*","*"," ","*","*","*","*","*"," "," ", " "," "," ","|"],
    ["|"," "," "," "," ","*","*","*","*","*"," "," ","*","*","*"," "," "," ", " "," "," ","|"],
    ["|"," "," "," "," "," ","*","*"," "," "," "," "," "," "," "," "," "," ", " "," "," ","|"],
    ["|","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_", "_","_","_","|"]];
    
    // starting position
    let mut pos_y: i32 = 5;
    let mut pos_x: i32 = 10;
    
    // initial variables
    let mut mod_y: i32 = 0;
    let mut mod_x: i32 = 0;
    let mut level = 0;
    let mut message = "You awake in a dark, damp jungle on a mysterious island...";
    let mut inventory = ["lamp", "sword", "hat"];

    // start game
    clear_screen();
    println!("{}\n", BANNER);
    let name = input("What's your name? ");
    
    // main game loop
    loop {
        // clear the screen
        clear_screen();
        
        // set player position
        map[pos_y as usize][pos_x as usize] = "@";
        
        // display game - stats, map, message, and tile description
        println!("RTA | {} | LV: {} | y: {} x: {}", name, level, pos_y, pos_x);
        for i in 0..11 {
            println!("{}", map[i].join(""));
        }
        xprint(message);
        tile_desc(pos_y, pos_x);
        
        // reset player position and message
        map[pos_y as usize][pos_x as usize] = "*";
        message = "";
        mod_y = 0;
        mod_x = 0;
        
        // get player move
        let mut player_move = String::new();
        player_move = input("> ");
        player_move = player_move.to_lowercase();
        
        // act on player move
        match player_move.as_ref() {
            "n" => mod_y = -1,
            "s" => mod_y =  1,
            "e" => mod_x =  1,
            "w" => mod_x = -1,
            "q" => break,
            "h" => message = HELP_TEXT,
            "i" => message = "inv",
            _   => message = "Invalid move!",
        };
        
        // move in direction if possible
        if map[(pos_y + mod_y) as usize][(pos_x + mod_x) as usize] == " " {
            message = "You can't go that way!";
        } else {
            pos_y += mod_y;
            pos_x += mod_x;
        }
        
    }
}

fn tile_desc(pos_y: i32, pos_x: i32) {
    // Print tile description given a (y, x) coordinate

    let coords = [(4, 10), (5, 10)];
    let test = ["Beach", "Jungle"];
    
    for i in 0..coords.len() {
        if coords[i].0 == pos_y && coords[i].1 == pos_x {
            xprint(test[i]);
        }
    }
}

fn input(prompt: &str) -> String {
    // Returns a user input string without a trailing new line.
    // Accepts a prompt to display to the user before input.

    // write prompt to screen
    print!("{}", prompt);
    io::stdout().flush().unwrap();
    
    // prompt user for input
    let mut user_input = String::new();
    io::stdin().read_line(&mut user_input)
        .expect("Failed to read input");
    
    // strip new line and return
    user_input.pop();
    user_input
}

fn xprint(words: &str) {
    // Given a string, prints each character with .05 second increments

    for i in 0..words.len() {
        // print single letter
        print!("{}", words.chars().nth(i).unwrap());
        io::stdout().flush().unwrap();

        // sleep for .05 seconds
        thread::sleep_ms(50);
    }
    println!();
}

fn clear_screen() {
    print!("{}[2J", 27 as char);
}
