use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

use std::collections::HashSet;

fn main() -> std::io::Result<()> {
    let mut seen:HashSet<i32> = HashSet::new();
    let mut total:i32 = 0;
    loop { 
        let file = File::open("input.txt")?;
        let content = BufReader::new(file);
        for line in content.lines() {
            let curr_num:i32 = line?.trim().parse::<i32>()
                .expect("invalid juice");
            total += curr_num;
            if seen.contains(&total) {
                println!("{}", total);
                return Ok(());
            }
            seen.insert(total);
        }
    }
}
