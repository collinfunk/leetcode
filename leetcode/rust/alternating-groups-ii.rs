// Leetcode problem 3208: Alternating Groups II.

struct Solution {}

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, k: i32) -> i32 {
        let mut result = 0;
        let mut alternating_count = 1;
        let mut last_color = colors[0];
        for i in 1..colors.len() + k as usize - 1 {
            let index = i % colors.len();
            if colors[index] == last_color {
                alternating_count = 1;
                last_color = colors[index];
                continue;
            }
            alternating_count += 1;
            if k <= alternating_count {
                result += 1;
            }
            last_color = colors[index];
        }
        result
    }
}

fn main() {}
