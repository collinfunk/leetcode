// Leetcode problem 151: Reverse Words in a String.

struct Solution {}

impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut words = s.split_ascii_whitespace().rev();
        let mut reversed = String::new();
        if let Some(word) = words.next() {
            reversed.push_str(&word);
            for word in words {
                reversed.push(' ');
                reversed.push_str(&word);
            }
        }
        reversed
    }
}

fn main() {}
