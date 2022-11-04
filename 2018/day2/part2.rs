use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() -> std::io::Result<()> {
    let file = File::open("input.txt")?;
    let content = BufReader::new(file);
    for line in content.lines() {
        let mut counts:HashMap<char, i32> = HashMap::new();
        let mut seen3 = false;
        let mut seen2 = false;
        for c in line?.trim().chars() {
            if !counts.contains_key(&c) {
                counts.insert(c, 0);
            }
            *counts.get_mut(&c)
                .unwrap() = *counts.get_mut(&c).unwrap()+1
        }
        for (_, count) in counts {
            if !seen2 && count == 2 {
                seen2 = true;
                two += 1;
            }
            if !seen3 && count == 3 {
                seen3 = true;
                three += 1;
            }

        }
    }
    println!("{}", three*two);
    Ok(())
}
