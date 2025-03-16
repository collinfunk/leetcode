// Leetcode problem 2586: Count the Number of Vowel Strings in Range.

struct Solution {}

impl Solution {
    pub fn vowel_strings(words: Vec<String>, left: i32, right: i32) -> i32 {
        words[left as usize..=right as usize]
            .iter()
            .filter(|s| {
                s.starts_with(['a', 'e', 'i', 'o', 'u']) && s.ends_with(['a', 'e', 'i', 'o', 'u'])
            })
            .count() as i32
    }
}

fn main() {}
