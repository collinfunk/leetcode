// Leetcode problem 2367: Number of Arithmetic Triplets.

struct Solution {}

impl Solution {
    pub fn arithmetic_triplets(nums: Vec<i32>, diff: i32) -> i32 {
        nums.iter().fold(0, |acc, x| {
            if nums.contains(&(x + diff)) && nums.contains(&(x + diff * 2)) {
                acc + 1
            } else {
                acc
            }
        })
    }
}

fn main() {}
