use std::collections::{BTreeMap, LinkedList};
use std::io::Result;

#[derive(Debug)]
struct FS<'a> {
    fs: BTreeMap<LinkedList<&'a str>, u32>,
    location: LinkedList<&'a str>,
}

impl<'a> FS<'a> {
    pub fn new(content: &'a String) -> Self {
        let mut filesystem = FS{
            fs: BTreeMap::new(),
            location: LinkedList::new(),
        };
        for line in content.lines() {
            let com = line.trim().split(" ").collect::<Vec<&str>>();
            if com[0] == "$" {
                if com[1] == "cd" {
                    if com[2] == ".." {
                        filesystem.location.pop_back();
                    } else {
                        filesystem.location.push_back(com[2]);
                    }
                }
            } else if com[0].chars().next().unwrap().is_numeric() {
                let mut curr_loc = filesystem.location.clone();
                while curr_loc.len() > 0 {
                    let new_val = filesystem.fs[&curr_loc] + com[0].parse::<u32>().unwrap();
                    filesystem.fs.insert(curr_loc, new_val);
                    curr_loc.pop_back();
                }
            }
            eprintln!("unreachable")
        }
        filesystem
    }

    pub fn find_dirs(&self) -> u32{
        let mut total = 0;
        for data in self.fs.values() {
            total += data
        }
        total
    }
}

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;

    let fs = FS::new(&content);
    let size = fs.find_dirs();
    println!("{size}");
    Ok(())
}
