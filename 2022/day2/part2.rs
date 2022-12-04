use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() -> std::io::Result<()> {
    let rps_map = HashMap::from([
        ("X", HashMap::from([
            ("A", 3),
            ("B", 1),
            ("C", 2),
        ])),
        ("Y", HashMap::from([
            ("A", 4),
            ("B", 5),
            ("C", 6),
        ])),
        ("Z", HashMap::from([
            ("A", 8),
            ("B", 9),
            ("C", 7),
        ])),
    ]);
    let file = File::open("input.txt")?;
    let content = BufReader::new(file);
    let mut total:i32 = 0;
    for line in content.lines() {
        let l = line.unwrap();
        let v:Vec<&str> = l
            .trim()
            .split(" ")
            .collect();
        total += rps_map[v[1]][v[0]];
    }
    println!("{}", total);
    Ok(())
}
