// Leetcode problem 1512: Number of Good Pairs.

struct Solution {}

impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut table = vec![0; 101];
        let mut result = 0;
        for number in nums {
            result += table[number as usize];
            table[number as usize] += 1;
        }
        result
    }
}

fn main() {}
