// Leetcode problem 2980: Check if Bitwise OR Has Trailing Zeros.

struct Solution {}

impl Solution {
    pub fn has_trailing_zeros(nums: Vec<i32>) -> bool {
        let mut result = 0;
        for num in nums {
            if 0 < num.trailing_zeros() {
                result += 1;
                if result == 2 {
                    return true;
                }
            }
        }
        false
    }
}

fn main() {}
