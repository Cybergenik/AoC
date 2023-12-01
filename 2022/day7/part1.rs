use std::fs::File;
use std::io::{BufReader};
use std::collections::{BTreeMap};
use std::io::prelude::*;

struct FS<'a> {
    fs: BTreeMap<&'a str, u32>,
    loc: String
}

fn trim_last_dir(loc: &mut String) {
    while loc.pop() != Some('/') {}
}

impl<'a> FS<'a> {
    pub fn new() -> Self {
        FS {
            fs: BTreeMap::new(),
            loc: "".to_string()
        }
    }
    pub fn parse_cmds(&mut self, lines: Vec<String>) {
        for line in lines {
            let mut com = line.split(" ");
            let com_type = com.next().expect("fucking my life");
            let first_com_type = com_type.chars().nth(0);
            match first_com_type {
                Some('$') => {
                    let command = com.next();
                    match command {
                        Some("cd") => {
                            let _dir = com.next();
                            match _dir {
                                Some("..") => {
                                    trim_last_dir(&mut self.loc);
                                },
                                //default state
                                Some("/") => { self.loc.push('/'); }, 
                                //change state
                                Some(_) => {
                                    self.loc.push('/');
                                    for c in _dir.unwrap().chars() {
                                        self.loc.push(c);
                                    }
                                }
                                _ => eprintln!("error parsing dir: {line}"),
                            }
                            println!("New Location: {}", self.loc);
                        },
                        Some("ls") => println!("ls"),
                        _ => eprintln!("error parsing command {:?} : {line}", command),
                    }
                },
                Some('1'..='9') => {
                    let mut curr_loc = self.loc.clone().to_string();
                    while curr_loc != "" {
                        let loc = curr_loc.as_str();
                        if !self.fs.contains_key(loc) {
                            self.fs.insert(loc, com_type.parse::<u32>().unwrap());
                        }
                        trim_last_dir(&mut curr_loc)
                    }
                    println!("{line}")
                },
                Some ('d') => {},//println!("dir"),
                _ => eprintln!("error parsing type: {line}"),
            }
        }
    }
    pub fn dirs_of_size(&self, n: u32) {
        todo!("Fuck you, World {n}")
    }
}

fn main() -> std::io::Result<()> {
    let file = File::open("test.txt")?;
    let content = BufReader::new(file);
    let mut fs = FS::new();
    fs.parse_cmds(content.lines().map(|l| l.unwrap()).collect());
    fs.dirs_of_size(32);
    println!("Final location: {}", fs.loc);
    println!("Sizes: {:?}", fs.fs);
    Ok(())
}
