// Leetcode problem 415: Add Strings.

struct Solution {}

impl Solution {
    pub fn add_strings(num1: String, num2: String) -> String {
        let mut rev1 = num1.bytes().rev();
        let mut rev2 = num2.bytes().rev();
        let mut result = Vec::with_capacity(num1.len().max(num2.len()) + 1);
        let mut carry = false;
        loop {
            let n1 = rev1.next().map(|c| c - b'0');
            let n2 = rev2.next().map(|c| c - b'0');
            if n1.is_none() && n2.is_none() && !carry {
                break;
            }
            let value = carry as u8 + n1.unwrap_or_default() + n2.unwrap_or_default();
            carry = 9 < value;
            result.push((b'0' + value % 10) as char);
        }
        result.iter().rev().collect()
    }
}

fn main() {}
