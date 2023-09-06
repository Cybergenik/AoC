use std::collections::{HashSet};
use std::io::Result;

fn is_start_message(slice: &str) -> bool {
    return slice.len() == slice.chars().collect::<HashSet<char>>().len()
}

fn main() -> Result<()> {
    const N:usize = 14;
    let content = std::fs::read_to_string("input.txt")?;

    for line in content.lines() {
        for i in N..line.trim().len() {
            if is_start_message(&line[i-N..i]) {
                println!("{i}");
                return Ok(())
            }
        }
    }
    Ok(())
}
