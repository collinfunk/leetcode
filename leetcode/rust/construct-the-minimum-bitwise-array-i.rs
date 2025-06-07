// Leetcode problem 3314: Construct the Minimum Bitwise Array I.

struct Solution {}

impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        nums.iter()
            .map(|&x| {
                if x % 2 == 0 {
                    return -1;
                }
                for i in 1..x {
                    if (i | (i + 1)) == x {
                        return i;
                    }
                }
                -1
            })
            .collect()
    }
}

fn main() {}
