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
    //println!("{}", String::from("a").chars().next().unwrap() as u32);
    for line in content.lines().map(|l| l.unwrap()) {
        let l = line.trim();
        let mid:usize = l.len()/2;
        let f = String::from(&l[..mid]).chars().collect::<HashSet<char>>();
        let s = String::from(&l[mid..]).chars().collect::<HashSet<char>>();
        let shared = f.intersection(&s);
        //println!("{:#?}", shared);
        for c in shared {
            total += get_val(*c)
        }
    }
    println!("{}", total);
    Ok(())
}
