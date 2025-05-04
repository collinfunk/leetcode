// Leetcode problem 1313: Decompress Run-Length Encoded List.

struct Solution {}

impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        nums.chunks(2)
            .flat_map(|x| [x[1]].repeat(x[0] as usize))
            .collect()
    }
}

fn main() {}
