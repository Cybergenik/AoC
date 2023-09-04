//use std::collections::HashSet;
use std::io::Result;

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;
    
    let lines = content.lines().map(str::trim).enumerate();

    println!("{lines:#?}");

    Ok(())
}
