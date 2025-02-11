// Leetcode problem 80: Remove Duplicates from Sorted Array II.

struct Solution {}

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut previous = i32::MIN;
        let mut seen = 0;
        let mut index = 0;
        for i in 0..nums.len() {
            if nums[i] == previous {
                seen += 1;
            } else {
                seen = 0;
            }
            if seen < 2 {
                nums[index] = nums[i];
                index += 1;
            }
            previous = nums[i]
        }
        index as i32
    }
}

fn main() {}
