// Leetcode problem 1832: Check if the Sentence Is Pangram.

struct Solution {}

impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        let mut table = [0; 26];
        for character in sentence.as_bytes() {
            table[(character - b'a') as usize] += 1
        }
        table.iter().filter(|&x| *x == 0).count() == 0
    }
}

fn main() {}
