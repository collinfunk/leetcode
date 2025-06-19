// Leetcode problem 2000: Reverse Prefix of Word.

struct Solution {}

impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        if let Some(index) = word.chars().position(|x| x == ch) {
            word[0..index + 1].chars().rev().collect::<String>() + &word[index + 1..]
        } else {
            word
        }
    }
}

fn main() {}
