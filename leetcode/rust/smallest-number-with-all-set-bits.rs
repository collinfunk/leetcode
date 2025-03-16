// Leetcode problem 3370: Smallest Number With All Set Bits.

struct Solution {}

impl Solution {
    pub fn smallest_number(n: i32) -> i32 {
        let mut value = 1;
        let mut bit = 1;
        while value < n {
            value |= 1 << bit;
            bit += 1;
        }
        return value;
    }
}

fn main() {}
