// Leetcode problem 1780: Check if Number is a Sum of Powers of Three.

struct Solution {}

impl Solution {
    pub fn check_powers_of_three(n: i32) -> bool {
        let mut value = n;
        while 0 < value {
            if value % 3 == 2 {
                return false;
            }
            value /= 3;
        }
        return true;
    }
}

fn main() {}
