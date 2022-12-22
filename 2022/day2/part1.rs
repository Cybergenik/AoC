use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() -> std::io::Result<()> {
    let rps_map = HashMap::from([
        ("A", HashMap::from([
            ("Y", 6),
            ("X", 3),
            ("Z", 0),
        ])),
        ("B", HashMap::from([
            ("Z", 6),
            ("Y", 3),
            ("X", 0),
        ])),
        ("C", HashMap::from([
            ("X", 6),
            ("Z", 3),
            ("Y", 0),
        ])),
    ]);
    
    let rps_vals = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3),
    ]);
    let file = File::open("input.txt")?;
    let content = BufReader::new(file);
    content.lines()
    let mut total:i32 = 0;
    for line in content.lines() {
        let l = line.unwrap();
        let v:Vec<&str> = l
            .trim()
            .split(" ")
            .collect();
        total += rps_map[v[0]][v[1]];
        total += rps_vals[v[1]];
    }
    println!("{}", total);
    Ok(())
}
