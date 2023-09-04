use std::collections::HashSet;
use std::io::Result;

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;
    
    let mut total = 0;
    for (_, line) in content.lines().map(str::trim).enumerate() {
        if let Some((l, r)) = line.split_once(",") {
            let ls:u8;
            let le:u8;
            let rs:u8;
            let re:u8;
            let (l_s, l_e) = l.split_once("-").expect("Fuck you");
            ls = l_s.parse::<u8>().expect("Fuck Me");
            le = l_e.parse::<u8>().expect("Fuck Me");
            let (r_s, r_e) = r.split_once("-").expect("Fuck you");
            rs = r_s.parse::<u8>().expect("Fuck Me");
            re = r_e.parse::<u8>().expect("Fuck Me");
            let mut l_set = HashSet::new();
            let mut r_set = HashSet::new();
            for i in ls..le+1 {
                l_set.insert(i);
            }
            for i in rs..re+1 {
                r_set.insert(i);
            }
            if l_set.is_subset(&r_set) || r_set.is_subset(&l_set) {
                total = total+1;
            }
        }
    }
    
    println!("{total}");
    Ok(())
}
