// Leetcode problem 367: Valid Perfect Square.

struct Solution {}

impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        let mut left = 0;
        let mut right = 46340;
        while left <= right {
            let middle = left + ((right - left) / 2);
            let square = middle * middle;
            if square == num {
                return true;
            } else if square < num {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        false
    }
}

fn main() {}
