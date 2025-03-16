// Leetcode problem 1957: Delete Characters to Make Fancy String.

struct Solution {}

impl Solution {
    pub fn make_fancy_string(s: String) -> String {
        let mut characters: Vec<char> = s.chars().collect();
        if characters.len() < 3 {
            return s;
        }
        let mut j = 2;
        for i in 2..characters.len() {
            if characters[i] != characters[j - 1] || characters[i] != characters[j - 2] {
                characters[j] = characters[i];
                j += 1;
            }
        }
        characters.truncate(j);
        characters.into_iter().collect()
    }
}

fn main() {}
