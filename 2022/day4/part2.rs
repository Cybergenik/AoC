use std::collections::HashSet;
use std::io::Result;

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;
    
    let mut total = 0;
    for line in content.lines().map(str::trim) {
        let (l, r) = line.split_once(",").expect("Unable to split by comma");
        let l_set = l.split_once("-")
            .map(|(x, y)| (x.parse::<u8>().unwrap()..y.parse::<u8>().unwrap()+1))
            .expect("Failed creating range set")
            .collect::<HashSet::<u8>>();
        let r_set = r.split_once("-")
            .map(|(x, y)| (x.parse::<u8>().unwrap()..y.parse::<u8>().unwrap()+1))
            .expect("Failed creating range set")
            .collect::<HashSet::<u8>>();
        if !l_set.is_disjoint(&r_set) || !r_set.is_disjoint(&l_set) {
            total +=1
        }
    }
    
    println!("{total}");
    Ok(())
}
