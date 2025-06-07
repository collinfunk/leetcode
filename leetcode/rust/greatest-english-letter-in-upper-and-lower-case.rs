// Leetcode problem 2309: Greatest English Letter in Upper and Lower Case.

use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn greatest_letter(s: String) -> String {
        let table = s.chars().fold(HashSet::new(), |mut map, x| {
            map.insert(x);
            map
        });
        for i in (0..=26).rev() {
            let lowercase = (b'a' + i as u8) as char;
            let uppercase = (b'A' + i as u8) as char;
            if table.contains(&lowercase) && table.contains(&uppercase) {
                return uppercase.to_string();
            }
        }
        "".to_string()
    }
}

fn main() {}
