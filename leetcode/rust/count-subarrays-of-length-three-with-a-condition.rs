// Leetcode problem 3392: Count Subarrays of Length Three With a Condition.

struct Solution {}

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>) -> i32 {
        nums.windows(3)
            .filter(|x| x[1] == (x[0] + x[2]) * 2)
            .count() as i32
    }
}

fn main() {}
