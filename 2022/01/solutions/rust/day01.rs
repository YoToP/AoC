use std::env;
use std::fs;
use std::process;
use std::error::Error;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err|{
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });
    let (p1,p2) = run(config).unwrap_or_else(|err|{
        println!("Application error: {err}");
        process::exit(1);
    });
    println!("Answer part1: {p1}");
    println!("Answer part2: {p2}");
}

struct Config{
    query: String,
    file_path: String,
}
impl Config{
    fn build(args: &[String]) -> Result<Config,&'static str>{
        if args.len() < 3 {
            return Err("not enough arguments");
        }
        let query = args[1].clone();
        let file_path = args[2].clone();
    
        Ok(Config{query,file_path})
    }
}
fn run(config: Config)->Result<(i32,i32),Box<dyn Error>>{
    let contents = fs::read_to_string(config.file_path)
        .expect("Should have been able to read the file");
    let mut temp :i32 = 0;
    let mut high :i32 = 0;
    let mut h2 :i32 = 0;
    let mut h3 :i32 = 0;
    for line in contents.lines(){
        if line.len() > 0{
            temp = temp +line.parse::<i32>().unwrap();
            //println!("temp = {temp}");
        }else{
            //println!("space");
            if temp > high{
                h3 = h2;
                h2 = high;
                high = temp;
            }else if temp > h2{
                h3 = h2;
                h2 = temp;
            }else if temp > h3{
                h3 = temp;
            }
            temp = 0;
        }
        
    }
    //println!("With text:\n{contents}");
    Ok((high,high+h2+h3))
}
