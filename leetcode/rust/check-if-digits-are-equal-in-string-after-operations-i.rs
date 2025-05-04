// Leetcode problem 3461: Check If Digits Are Equal in String After Operations I.

struct Solution {}

impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        let mut characters: Vec<u32> = s.chars().map(|c| c.to_digit(10).unwrap()).collect();
        while characters.len() > 2 {
            characters = characters.windows(2).map(|c| (c[0] + c[1]) % 10).collect();
        }
        characters[0] == characters[1]
    }
}

fn main() {}
