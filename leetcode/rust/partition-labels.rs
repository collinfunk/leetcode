// Leetcode problem 763: Partition Labels.

struct Solution {}

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut table = [0; 26];
        let characters = s.into_bytes();
        for (i, character) in characters.iter().enumerate() {
            table[(character - ('a' as u8)) as usize] = i;
        }
        let mut start = 0;
        let mut end = 0;
        let mut result = Vec::new();
        for (i, character) in characters.iter().enumerate() {
            end = end.max(table[(character - ('a' as u8)) as usize]);
            if i == end {
                result.push((i - start + 1) as i32);
                start = i + 1;
            }
        }
        result
    }
}

fn main() {}
