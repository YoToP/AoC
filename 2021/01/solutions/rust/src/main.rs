use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let loc = &args[0];
    let filename = &args[1];
    
    println!("In file {}", loc);
    println!("In file {}", filename);
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    
}
