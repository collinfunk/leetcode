// Leetcode problem 3174: Clear Digits.

use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut queue: VecDeque<char> = VecDeque::with_capacity(s.len());
        s.chars().for_each(|x| {
            if x.is_numeric() {
                queue.pop_back();
            } else {
                queue.push_back(x);
            }
        });
        queue.iter().collect()
    }
}

fn main() {}
