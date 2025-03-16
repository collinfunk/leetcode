// Leetcode problem 1967: Number of Strings That Appear as Substrings in Word.

struct Solution {}

impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        patterns.iter().filter(|x| word.contains(*x)).count() as i32
    }
}

fn main() {}
