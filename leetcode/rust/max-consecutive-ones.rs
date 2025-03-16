// Leetcode problem 485: Max Consecutive Ones.

struct Solution {}

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut current = 0;
        let mut max = 0;
        for num in nums {
            if num == 1 {
                current += 1;
                if max < current {
                    max = current;
                }
            } else {
                current = 0;
            }
        }
        max
    }
}

fn main() {}
