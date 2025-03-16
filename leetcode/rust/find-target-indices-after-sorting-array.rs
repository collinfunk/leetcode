// Leetcode problem 2089: Find Target Indices After Sorting Array.

struct Solution {}

impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut target_count = 0;
        let mut smaller_count = 0;
        for num in nums {
            if num == target {
                target_count += 1;
            } else if num < target {
                smaller_count += 1;
            }
        }
        (smaller_count..smaller_count + target_count).collect()
    }
}

fn main() {}
