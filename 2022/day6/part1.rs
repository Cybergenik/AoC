use std::fs::File;
use std::io::{BufReader};
use std::collections::{HashSet};
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let file = File::open("input.txt")?;
    let line = BufReader::new(file).lines().nth(0).unwrap()?;
    for i in 4..line.len() {
        let set = line[i-4..i].chars().collect::<HashSet<char>>();
        if set.len() == 4 {
            println!("{i}");
            break;
        }
    }
    Ok(())
}
