// Leetcode problem 2094: Finding 3-Digit Even Numbers.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn find_even_numbers(digits: Vec<i32>) -> Vec<i32> {
        let mut nums = HashSet::new();
        for i in 0..digits.len() {
            for j in 0..digits.len() {
                for k in 0..digits.len() {
                    if i == j || j == k || i == k {
                        continue;
                    }
                    let num = digits[i] * 100 + digits[j] * 10 + digits[k];
                    if num >= 100 && num % 2 == 0 {
                        nums.insert(num);
                    }
                }
            }
        }
        let mut result: Vec<_> = nums.into_iter().collect();
        result.sort();
        result
    }
}

fn main() {}
