// Leetcode problem 1935: Maximum Number of Words You Can Type.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
        let broken_letters: HashSet<char> = broken_letters.chars().collect();
        let words: Vec<&str> = text.split(" ").collect();
        let mut result = 0;
        for word in words {
            let missing = word.chars().filter(|c| broken_letters.contains(c)).count();
            if missing == 0 {
                result += 1;
            }
        }
        result
    }
}

fn main() {}
