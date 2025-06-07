// Leetcode problem 3170: Lexicographically Minimum String After Removing Stars.

struct Solution {}

impl Solution {
    pub fn clear_stars(s: String) -> String {
        let mut table = vec![vec![]; 26];
        let mut chars = s.bytes().collect::<Vec<u8>>();
        let mut indices = Vec::new();
        for (i, &ch) in chars.iter().enumerate() {
            if ch != b'*' {
                table[(ch - b'a') as usize].push(i);
            } else {
                for entry in table.iter_mut().take(26) {
                    if let Some(index) = entry.pop() {
                        indices.push(index);
                        break;
                    }
                }
            }
        }
        for i in indices {
            chars[i] = b'*';
        }
        chars
            .into_iter()
            .filter(|&c| c != b'*')
            .map(|c| c as char)
            .collect()
    }
}

fn main() {}
