// Leetcode problem 2287: Rearrange Characters to Make Target String.

struct Solution {}

impl Solution {
    pub fn rearrange_characters(s: String, target: String) -> i32 {
        let mut have = [0; 26];
        for ch in s.chars() {
            have[(ch as u8 - b'a') as usize] += 1;
        }
        let mut need = [0; 26];
        for ch in target.chars() {
            need[(ch as u8 - b'a') as usize] += 1;
        }
        let mut result = i32::MAX;
        for i in 0..26 {
            if need[i] != 0 {
                result = result.min(have[i] / need[i]);
            }
        }
        result
    }
}

fn main() {}
