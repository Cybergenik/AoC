use std::collections::{BTreeMap, LinkedList};
use std::io::Result;

#[derive(Debug)]
struct FS<'a> {
    fs: BTreeMap<LinkedList<&'a str>, u32>,
    location: LinkedList<&'a str>,
    size: u32,
}

impl<'a> FS<'a> {
    pub fn new(content: &'a String, size: u32) -> Self {
        let mut filesystem = FS{
            fs: BTreeMap::new(),
            location: LinkedList::new(),
            size: size,
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
                    if filesystem.fs.contains_key(&curr_loc) {
                        *filesystem.fs.get_mut(&curr_loc).unwrap() += com[0].parse::<u32>().unwrap();
                    } else {
                        filesystem.fs.insert(curr_loc.clone(), com[0].parse::<u32>().unwrap());
                    }
                    curr_loc.pop_back();
                }
            }
        }
        filesystem
    }

    pub fn dir_sizen(&self, target_size: u32) -> u32{
        let mut total = 0;
        for size in self.fs.values() {
            if *size <= target_size {
                total += size
            }
        }
        total
    }

    pub fn min_del(&self, free_size: u32) -> u32{
        let mut min_dir = self.size;
        let root_dir = LinkedList::from(["/"]);
        let free = self.size - self.fs[&root_dir];
        for size in self.fs.values() {
            if free+size >= free_size && *size < min_dir{
                min_dir = *size
            }
        }
        min_dir
    }
}

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;

    let fs = FS::new(&content, 70_000_000);
    println!("Part 1: {}", fs.dir_sizen(100_000));
    println!("Part 2: {}", fs.min_del(30_000_000));
    Ok(())
}
