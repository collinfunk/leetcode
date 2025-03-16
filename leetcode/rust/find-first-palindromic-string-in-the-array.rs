// Leetcode problem 2108: Find First Palindromic String in the Array.

struct Solution {}

impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        for word in words {
            let characters = word.clone().into_bytes();
            if characters.len() == 1 {
                return word;
            }
            let mut low = 0;
            let mut high = characters.len() - 1;
            let mut found = true;
            while low <= high {
                if characters[low] != characters[high] {
                    found = false;
                    break;
                }
                low += 1;
                high -= 1;
            }
            if found {
                return word;
            }
        }
        "".to_string()
    }
}

fn main() {}
