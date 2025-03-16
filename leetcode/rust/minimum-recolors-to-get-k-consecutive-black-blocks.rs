// Leetcode problem 2379: Minimum Recolors to Get K Consecutive Black Blocks.

struct Solution {}

impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let mut left = 0;
        let mut white_count = 0;
        let mut result = i32::MAX;
        let length = blocks.len();
        let blocks = blocks.as_bytes();
        for right in 0..length {
            if blocks[right] == 'W' as u8 {
                white_count += 1;
            }
            if right - left + 1 == k as usize {
                result = result.min(white_count);
                if blocks[left] == 'W' as u8 {
                    white_count -= 1;
                }
                left += 1
            }
        }
        result
    }
}

fn main() {}
