// Leetcode problem 2131: Longest Palindrome by Concatenating Two Letter Words.

struct Solution {}

impl Solution {
    pub fn longest_palindrome(words: Vec<String>) -> i32 {
        let mut table = vec![vec![0; 26]; 26];
        let mut result = 0;
        let mut unpaired = 0;
        for word in words {
            let mut chars = word.bytes();
            let a = (chars.next().unwrap() - b'a') as usize;
            let b = (chars.next().unwrap() - b'a') as usize;
            if a == b {
                if 0 < table[a][b] {
                    table[a][b] -= 1;
                    result += 4;
                    unpaired -= 1;
                } else {
                    table[a][b] += 1;
                    unpaired += 1;
                }
                continue;
            }
            if 0 < table[a][b] {
                table[a][b] -= 1;
                result += 4;
            } else {
                table[b][a] += 1;
            }
        }
        if 0 < unpaired {
            result + 2
        } else {
            result
        }
    }
}

fn main() {}
