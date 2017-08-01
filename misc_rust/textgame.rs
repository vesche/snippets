use std::io;
use std::io::Write;

const BANNER: &'static str = "
'||''|.   |''||''|     |    
 ||   ||     ||       |||   
 ||''|'      ||      |  ||  
 ||   |.     ||     .''''|. 
.||.  '|'   .||.   .|.  .||.
     Rust Text Adventure";

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
    let mut pos_y = 5;
    let mut pos_x = 10;
    let mut level = 0;

    // start game
    clear_screen();
    println!("{}\n", BANNER);
    let name = input("What's your name? ");
    println!("Hello there, {}!", name);
    
    // main game loop
    loop {
        // print map
        clear_screen();
        map[pos_y][pos_x] = "@";
        println!("RTA | {} | LV: {}", name, level);
        for i in 0..11 {
            println!("{}", map[i].join(""));
        }
        
        // reset map
        map[pos_y][pos_x] = "*";
        
        // get player move
        let mut player_move = String::new();
        player_move = input("> ");
        
        // player move control flow
        if player_move == "north" {
            if map[pos_y-1][pos_x] == " " {
                continue;
            }
            pos_y -= 1;
        }
        else if player_move == "south" {
            if map[pos_y+1][pos_x] == " " {
                continue;
            }
            pos_y += 1;
        }
        else if player_move == "east" {
            if map[pos_y][pos_x+1] == " " {
                continue;
            }
            pos_x += 1;
        }
        else if player_move == "west" {
            if map[pos_y][pos_x-1] == " " {
                continue;
            }
            pos_x -= 1;
        }
        else if player_move == "quit" {
            break;
        }
        else {
            println!("Invalid move!");
        }
    }
}

/*
fn map_desc(pos_y: i32, pos_x: i32) -> String {

    let coords = (pos_y, pos_x);
    let test = [[ (4, 10), ("Beach", 0) ], [ (5, 10), ("Jungle", 0) ]];
    
    for i in 0..2 {
        if test[i][0] == coords {
            "Test"
        }
    }

}
*/

fn input(prompt: &str) -> String {
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

fn clear_screen() {
    print!("{}[2J", 27 as char);
}