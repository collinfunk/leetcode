// Leetcode problem 2283: Check if Number Has Equal Digit Count and Digit Value.

struct Solution {}

impl Solution {
    pub fn digit_count(num: String) -> bool {
        let mut table = [0; 10];
        for digit in num.bytes() {
            let value = digit - '0' as u8;
            table[value as usize] += 1;
        }
        for (i, digit) in num.bytes().enumerate() {
            let value = digit - '0' as u8;
            if table[i] != value {
                return false;
            }
        }
        true
    }
}

fn main() {}
