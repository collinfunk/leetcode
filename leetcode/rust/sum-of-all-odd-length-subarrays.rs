// Leetcode problem 1588: Sum of All Odd Length Subarrays.

struct Solution {}

impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        let mut result = 0;
        let n = arr.len() as i32;
        for (left, value) in arr.into_iter().enumerate() {
            let right = n - left as i32 - 1;
            result += value * (left as i32 / 2 + 1) * (right / 2 + 1);
            result += value * ((left as i32 + 1) / 2) * ((right + 1) / 2);
        }
        result
    }
}

fn main() {}
