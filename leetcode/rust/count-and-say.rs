// Leetcode problem 38: Count and Say.

use std::iter::once;

struct Solution {}

impl Solution {
    pub fn count_and_say(n: i32) -> String {
        let mut result = vec![1];
        for _ in 1..n {
            let mut next = vec![];
            let mut slow = 0;
            for fast in 0..=result.len() {
                if fast == result.len() || result[slow] != result[fast] {
                    next.extend(once((fast - slow) as u8).chain(once(result[slow] as u8)));
                    slow = fast;
                }
            }
            result = next;
        }
        result.into_iter().map(|x| (x + b'0') as char).collect()
    }
}

fn main() {}
