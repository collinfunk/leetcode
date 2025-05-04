// Leetcode problem 1002: Find Common Characters.

struct Solution {}

impl Solution {
    pub fn common_chars(words: Vec<String>) -> Vec<String> {
        let mut table = [0; 26];
        for character in words[0].as_bytes() {
            table[(character - ('a' as u8)) as usize] += 1;
        }
        for word in words.into_iter().skip(1) {
            let mut current = [0; 26];
            for character in word.as_bytes() {
                current[(character - ('a' as u8)) as usize] += 1;
            }
            for i in 0..26 {
                table[i] = table[i].min(current[i]);
            }
        }
        let mut result = Vec::with_capacity(26);
        for i in 0..26 {
            let mut j = 0;
            while j < table[i] {
                result.push(((i as u8 + ('a' as u8)) as char).to_string());
                j += 1;
            }
        }
        result
    }
}

fn main() {}
