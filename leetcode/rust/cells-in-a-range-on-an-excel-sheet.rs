// Leetcode problem 2194: Cells in a Range on an Excel Sheet.

struct Solution {}

impl Solution {
    pub fn cells_in_range(s: String) -> Vec<String> {
        let s = s.as_bytes();
        let mut result = Vec::with_capacity(10);
        for column in s[0]..=s[3] {
            for row in s[1]..=s[4] {
                result.push(format!("{}{}", column as char, row as char));
            }
        }
        result
    }
}

fn main() {}
