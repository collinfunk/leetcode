// Leetcode problem 2616: Minimize the Maximum Difference of Pairs.

struct Solution {}

impl Solution {
    pub fn minimize_max(nums: Vec<i32>, p: i32) -> i32 {
        fn count_valid_pairs(nums: &[i32], threshold: i32) -> i32 {
            let mut index = 0;
            let mut count = 0;
            while index < nums.len() - 1 {
                if nums[index + 1] - nums[index] <= threshold {
                    count += 1;
                    index += 1;
                }
                index += 1;
            }
            count
        }
        let mut nums = nums.clone();
        nums.sort_unstable();
        let mut left = 0;
        let mut right = nums[nums.len() - 1] - nums[0];
        while left < right {
            let mid = left + (right - left) / 2;
            if p <= count_valid_pairs(&nums, mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}

fn main() {}
