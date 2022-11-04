use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let file = File::open("input.txt")?;
    let content = BufReader::new(file);
    let mut total:i32 = 0;
    for line in content.lines() {
        let curr_num:i32 = line?.trim().parse::<i32>()
            .expect("invalid juice");
        total += curr_num;
    }
    println!("{}", total);
    Ok(())
}
