use std::io::Result;

#[derive(Debug)]
struct MoveAction {
    from: usize,
    dest: usize,
    count: usize,
}

#[derive(Debug)]
struct StackAction {
    dest: usize,
    c: char,
}

fn parse_stack_row(line: &str) -> Vec<StackAction> {
    line.chars()
        .enumerate()
        .filter(|(_, c)| c.is_ascii_alphabetic()) 
        .map(|(i, c)| StackAction{ dest: ((i+3)/4)-1, c: c })
        .collect()
}

fn parse_move_row(line: &str) -> MoveAction {
    let action = line.split(" ")
        .filter(|x| x.chars().nth(0).unwrap().is_ascii_digit())
        .map(|x| x.parse::<usize>().unwrap())
        .collect::<Vec::<usize>>();
    MoveAction{
        from: action[1]-1,
        dest: action[2]-1,
        count: action[0],
    }
}

fn main() -> Result<()> {
    const N:usize = 9;
    let content = std::fs::read_to_string("input.txt")?;

    let mut stacks = Vec::<Vec<char>>::new();
    while stacks.len() < N { 
        stacks.push(Vec::new())
    }
    for line in content.lines() {
        if line == ""{
            continue;
        }
        //println!("Crates:\n{stacks:?}");
        match line.chars().nth(1) {
            Some('1') => {
                stacks = stacks.iter().map(|x| x.iter().rev().cloned().collect()).collect()
            },
            Some('o') => {
                let m_action = parse_move_row(line);
                //println!("    Moves:\n    {m_action:?}");
                for _ in 0..m_action.count {
                    let c = stacks[m_action.from].pop().unwrap();
                    stacks[m_action.dest].push(c);
                }
            },
            _ => {
                let actions = parse_stack_row(line);
                //println!("    Stacks:\n    {actions:?}");
                for s_action in actions {
                    stacks[s_action.dest].push(s_action.c)
                }
            },
        }
    }
    
    println!("");
    for stack in stacks {
        print!("{}", stack.last().unwrap())
    }
    println!("");
    Ok(())
}
