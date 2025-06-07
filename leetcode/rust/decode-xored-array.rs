// Leetcode problem 1720: Decode XORed Array.

struct Solution {}

impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        let mut result = Vec::with_capacity(encoded.len() + 1);
        result.push(first);
        for i in 0..encoded.len() {
            result.push(result[i] ^ encoded[i]);
        }
        result
    }
}

fn main() {}
