use std::fs::File;
use std::io::{BufReader};
use std::io::prelude::*;

fn parse_stack(stacks: &mut Vec<Vec<char>>, line: String) {
    let mut idx = 0;
    for (i, c) in line.chars().enumerate() {
        if (i+1) % 4 == 0 {
            idx += 1;
        }
        if c.is_ascii_alphabetic() {
            while idx >= stacks.len() { stacks.push(vec![]); }
            stacks[idx].push(c);
        }
    }
}

fn parse_command(stacks: &mut Vec<Vec<char>>, line: String) {
    //parse
    let elements = line.split(" ").collect::<Vec<&str>>();
    let amount = elements[1].parse::<usize>().unwrap();
    let from = elements[3].parse::<usize>().unwrap() - 1;
    let to = elements[5].parse::<usize>().unwrap() - 1;
    //move
    for _ in 0..amount {
        let c = stacks[from].pop().unwrap();
        stacks[to].push(c);
    }
}

fn main() -> std::io::Result<()> {
    let file = File::open("input.txt")?;
    let content = BufReader::new(file);
    let mut stacks = Vec::new();
    for line in content.lines().map(|l| l.unwrap()) {
        match line.chars().nth(0) {
            Some(' ') | Some('[') => parse_stack(&mut stacks, line),
            Some('m') => parse_command(&mut stacks, line),
            None => {
                let mut new_stacks = Vec::new();
                for stack in stacks {
                    new_stacks.push(stack.iter().rev().map(|x| x.to_owned()).collect());
                }
                stacks = new_stacks;
            }
            _ => ()
        }
    }
    let letters: String = stacks.iter().map(|x| x.last().to_owned().unwrap()).collect();
    println!("{letters}");
    Ok(())
}
