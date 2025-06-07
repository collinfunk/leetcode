// Leetcode problem 2942: Find Words Containing Character.

struct Solution {}

impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        words
            .iter()
            .enumerate()
            .filter_map(|(i, word)| word.contains(x).then_some(i as i32))
            .collect()
    }
}

fn main() {}
