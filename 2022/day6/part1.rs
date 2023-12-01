use std::collections::{HashSet};
use std::io::Result;

fn is_start_packet(slice: &str) -> bool {
    return slice.len() == slice.chars().collect::<HashSet<char>>().len()
}

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;

    for line in content.lines() {
        for i in 4..line.trim().len() {
            if is_start_packet(&line[i-4..i]) {
                println!("{i}");
                return Ok(())
            }
        }
    }
    Ok(())
}
