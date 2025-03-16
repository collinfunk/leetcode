// Leetcode problem 1295: Find Numbers with Even Number of Digits.

struct Solution {}

impl Solution {
    pub fn convert_date_to_binary(date: String) -> String {
        date.split("-")
            .map(|x| format!("{:b}", x.parse::<u32>().unwrap()))
            .collect::<Vec<_>>()
            .join("-")
    }
}

fn main() {}
