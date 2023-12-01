use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let file = File::open("input.txt")?;
    let content = BufReader::new(file);
    let mut total:u32 = 0;
    for line in content.lines().map(|l| l.unwrap()) {
        let (left, right) = line.trim().split_once(",").unwrap();
        let (lstart, lend) = left
            .split_once("-")
            .map(|(s, e)| (s.parse::<u32>().unwrap(), e.parse::<u32>().unwrap()))
            .unwrap();
        let (rstart, rend) = right
            .split_once("-")
            .map(|(s, e)| (s.parse::<u32>().unwrap(), e.parse::<u32>().unwrap()))
            .unwrap();
        if lstart <= rend && lend >= rstart {
            total += 1;
        }
    }
    println!("{}", total);
    Ok(())
}
