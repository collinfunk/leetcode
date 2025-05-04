// Leetcode problem 2843: Count Symmetric Integers.

struct Solution {}

impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut result = 0;
        for i in low..=high {
            if i < 100 && i % 11 == 0 {
                result += 1;
            } else if 1000 <= i && i < 10000 {
                let left = i / 1000 + (i % 1000) / 100;
                let right = (i % 100) / 10 + i % 10;
                if left == right {
                    result += 1;
                }
            }
        }
        result
    }
}

fn main() {}
