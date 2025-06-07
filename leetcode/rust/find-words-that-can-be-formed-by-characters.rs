// Leetcode problem 1160: Find Words That Can Be Formed by Characters.

struct Solution {}

impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        let mut char_set = vec![0; 26];
        for ch in chars.chars() {
            char_set[ch as usize - 'a' as usize] += 1;
        }
        let mut result = 0;
        for word in words {
            let mut word_set = vec![0; 26];
            for ch in word.chars() {
                word_set[ch as usize - 'a' as usize] += 1;
            }
            let mut good = true;
            for i in 0..26 {
                if char_set[i] < word_set[i] {
                    good = false;
                    break;
                }
            }
            if good {
                result += word.len();
            }
        }
        result as i32
    }
}

fn main() {}
