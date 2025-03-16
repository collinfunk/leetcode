// Leetcode problem 3340: Check Balanced String.

struct Solution {}

impl Solution {
    pub fn is_balanced(num: String) -> bool {
        let mut odd = 0;
        let mut even = 0;
        for (i, ch) in num.into_bytes().into_iter().enumerate() {
            let value = ch - b'0';
            if i & 1 == 0 {
                odd += value;
            } else {
                even += value;
            }
        }
        even == odd
    }
}

fn main() {}
