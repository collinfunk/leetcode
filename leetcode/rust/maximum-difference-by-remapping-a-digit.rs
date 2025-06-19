// Leetcode problem 2566: Maximum Difference by Remapping a Digit.

struct Solution {}

impl Solution {
    pub fn min_max_difference(num: i32) -> i32 {
        fn get_number(digits: Vec<i32>) -> i32 {
            digits.iter().fold(0, |acc, x| acc * 10 + x)
        }
        let mut digits = vec![];
        let mut value = num;
        while 0 < value {
            digits.push(value % 10);
            value /= 10;
        }
        digits.reverse();
        let mut i = 0;
        while i < digits.len() - 1 && digits[i] == 9 {
            i += 1;
        }
        get_number(
            digits
                .iter()
                .map(|&x| if x == digits[i] { 9 } else { x })
                .collect(),
        ) - get_number(
            digits
                .iter()
                .map(|&x| if x == digits[0] { 0 } else { x })
                .collect(),
        )
    }
}

fn main() {}
