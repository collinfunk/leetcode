// Leetcode problem 2780: Minimum Index of a Valid Split.

struct Solution {}

impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let mut x = nums[0];
        let mut count = 0;
        for num in &nums {
            if *num == x {
                count += 1;
            } else {
                count -= 1;
            }
            if count == 0 {
                x = *num;
                count = 1;
            }
        }
        let mut x_count = 0;
        for num in &nums {
            if *num == x {
                x_count += 1;
            }
        }
        let mut count = 0;
        for i in 0..nums.len() {
            if nums[i] == x {
                count += 1;
            }
            if count * 2 > i + 1 && (x_count - count) * 2 > nums.len() - i - 1 {
                return i as i32;
            }
        }
        -1
    }
}

fn main() {}
