// Leetcode problem 2434: Using a Robot to Print the Lexicographically Smallest String.

struct Solution {}

impl Solution {
    pub fn robot_with_string(s: String) -> String {
        let mut table = [0; 26];
        for c in s.bytes() {
            table[(c - b'a') as usize] += 1;
        }
        let mut stack = Vec::new();
        let mut result = String::new();
        let mut min = b'a';
        for c in s.bytes() {
            stack.push(c);
            table[(c - b'a') as usize] -= 1;
            while min != b'z' && table[(min - b'a') as usize] == 0 {
                min += 1;
            }
            while !stack.is_empty() && stack.last().unwrap() <= &min {
                result.push(stack.pop().unwrap() as char);
            }
        }
        result
    }
}

fn main() {}
