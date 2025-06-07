// Leetcode problem 3158: Find the XOR of Numbers Which Appear Twice

struct Solution {}

impl Solution {
    pub fn duplicate_numbers_xor(nums: Vec<i32>) -> i32 {
        let mut table = [0; 51];
        let mut result = 0;
        for num in nums {
            table[num as usize] += 1;
            if table[num as usize] == 2 {
                result ^= num;
            }
        }
        result
    }
}

fn main() {}
