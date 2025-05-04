// Leetcode problem 2302: Count Subarrays With Score Less Than K.

struct Solution {}

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i64) -> i64 {
        let mut result = 0;
        let mut total = 0;
        let mut i = 0;
        for j in 0..nums.len() {
            total += nums[j] as i64;
            while i <= j && total * (j - i + 1) as i64 >= k {
                total -= nums[i] as i64;
                i += 1;
            }
            result += j - i + 1;
        }
        result as i64
    }
}

fn main() {}
