// Leetcode problem 2294: Partition Array Such That Maximum Difference Is K.

struct Solution {}

impl Solution {
    pub fn partition_array(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums.clone();
        nums.sort_unstable();
        let mut result = 1;
        let mut min = nums[0];
        for num in nums {
            if k < num - min {
                result += 1;
                min = num;
            }
        }
        result
    }
}

fn main() {}
