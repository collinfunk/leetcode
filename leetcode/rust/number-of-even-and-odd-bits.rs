// Leetcode problem 2595: Number of Even and Odd Bits.

struct Solution {}

impl Solution {
    pub fn even_odd_bit(n: i32) -> Vec<i32> {
        let mut result = vec![0; 2];
        for i in 0..32 {
            if (n & (1 << i)) != 0 {
                result[(i % 2) as usize] += 1;
            }
        }
        result
    }
}

fn main() {}
