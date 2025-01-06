// Leetcode problem 9: Palindrome Number.

struct Solution {}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let mut reverse = 0;
        let mut value = x;
        while value != 0 {
            reverse = reverse * 10 + value % 10;
            value /= 10;
        }
        x == reverse
    }
}

fn main() {}
