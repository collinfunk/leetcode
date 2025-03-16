// Leetcode problem 1837: Sum of Digits in Base K.

struct Solution {}

impl Solution {
    pub fn sum_base(n: i32, k: i32) -> i32 {
        let mut result = 0;
        let mut value = n;
        while 0 < value {
            result += value % k;
            value /= k;
        }
        result
    }
}

fn main() {}
