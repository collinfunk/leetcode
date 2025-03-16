// Leetcode problem 1662: Check If Two String Arrays are Equivalent.

struct Solution {}

impl Solution {
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        word1.join("") == word2.join("")
    }
}

fn main() {}
