use std::collections::HashSet;
use std::io::Result;

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;
    
    let mut total = 0;
    for (_, line) in content.lines().map(str::trim).enumerate() {
        line.split_once(",")
            .map(|(l, r)| {
                let l_set = l.split_once("-")
                    .map(|(x, y)| (x.parse::<u8>().unwrap(), y.parse::<u8>().unwrap()))
                    .map(|(s, e)| (s..e+1).collect::<HashSet::<u8>>())
                    .expect("Fuck you");
                let r_set = r.split_once("-")
                    .map(|(x, y)| (x.parse::<u8>().unwrap(), y.parse::<u8>().unwrap()))
                    .map(|(s, e)| (s..e+1).collect::<HashSet::<u8>>())
                    .expect("Fuck you");
                if !l_set.is_disjoint(&r_set) || !r_set.is_disjoint(&l_set) {
                    total +=1
                }
            });
    }
    
    println!("{total}");
    Ok(())
}
