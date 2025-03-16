// Leetcode problem 1295: Find Numbers with Even Number of Digits.

struct Solution {}

impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut result = 0;
        for num in nums {
            if num.to_string().len() % 2 == 0 {
                result += 1
            }
        }
        result
    }
}

fn main() {}
