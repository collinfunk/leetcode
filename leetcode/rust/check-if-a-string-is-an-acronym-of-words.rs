// Leetcode problem 2828: Check if a String Is an Acronym of Words.

struct Solution {}

impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        let bytes = s.as_bytes();
        let mut i = 0;
        for word in words {
            if i >= bytes.len() || bytes[i] != word.as_bytes()[0] {
                return false;
            }
            i += 1;
        }
        i == bytes.len()
    }
}

fn main() {}
