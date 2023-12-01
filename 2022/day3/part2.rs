use std::collections::HashSet;
use std::io::Result;

fn get_val(x: char) -> u32 {
    let c = x as u32;
    match x.is_lowercase() {
        true => c - 96,
        false => c - 65 + 27
    }
}

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;

    let mut total = 0;
    let mut group = HashSet::new();

    let lines = content.lines().map(str::trim).enumerate();

    for (i, line) in lines {
        let char_set = line.chars().collect();
        if group.is_empty() {
            group = char_set;
        } else {
            group = group.intersection(&char_set).copied().collect();
        }
        let i = i+1;
        if i % 3 == 0 {
            total += group.drain().map(get_val).sum::<u32>();
        }
    }

    println!("{total}");
    Ok(())
}
