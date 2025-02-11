// Leetcode problem 1422: Maximum Score After Splitting a String.

struct Solution {}

impl Solution {
    pub fn max_score(s: String) -> i32 {
        let mut result = 0;
        for i in 1..s.len() {
            let left = s[0..i].to_string();
            let right = s[i..].to_string();
            result = result.max(
                (left.chars().filter(|c| *c == '0').count()
                    + right.chars().filter(|c| *c == '1').count()) as i32,
            );
        }
        result
    }
}

fn main() {}
