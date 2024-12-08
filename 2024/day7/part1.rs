use std::io::Result;

fn eval(nums: Vec<String>, total: u64) -> bool {
    fn rec_eval(curr_v: usize, curr_total: u64, nums: &Vec<String>, total: u64) -> bool {
        if curr_v == nums.len() {
            return curr_total == total;
        }
        let num = nums[curr_v].parse::<u64>().unwrap();
        let a_val = curr_total + num;
        let m_val = curr_total * num;
        return (a_val <= total && rec_eval(curr_v + 1, a_val, &nums, total)) 
            || (m_val <= total && rec_eval(curr_v + 1, m_val, &nums, total))
    }
    rec_eval(1, nums[0].parse::<u64>().unwrap(), &nums, total)
}

fn main() -> Result<()> {
    let content = std::fs::read_to_string("input.txt")?;

    let total = content.lines().fold(0, |total, l| {
        let (l, r) = l.trim().split_once(':').unwrap();
        let t = l.trim().parse::<u64>().unwrap();
        let nums = r.trim().split(" ").map(String::from).collect();
        //println!("{t} : {nums:?}");
        total + if eval(nums, t) { t } else { 0 }
    });
    println!("{total}");
    Ok(())
}
