use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::collections::{HashSet};

fn get_val(x:char) -> u32{
    let c = x as u32;
    if x.is_lowercase(){
        return c-96;
    }
    return (c-65)+27;
}

fn main() -> std::io::Result<()> {
    let file = File::open("input.txt")?;
    let content = BufReader::new(file);
    let mut total:u32 = 0;
    let mut i = 0;
    let mut group: Option<HashSet<char>> = None;
    for line in content.lines().map(|l| l.unwrap()) {
        let l = line.trim();
        i += 1;
        let c_set = String::from(&l[..]).chars().collect::<HashSet<char>>();
        if group == None {
            group = Some(c_set);
        } else {
            group = Some(HashSet::from(group.unwrap()
                                        .intersection(&c_set)
                                        .map(|x| *x)
                                        .collect::<HashSet<char>>()));
        }
        if i % 3 == 0 {
            for c in group.unwrap() {
                total += get_val(c);
            }
            group = None;
        }
    }
    println!("{}", total);
    Ok(())
}
