// Leetcode problem 1342: Number of Steps to Reduce a Number to Zero.

struct Solution {}

impl Solution {
    pub fn number_of_steps(num: i32) -> i32 {
        if num == 0 {
            return 0;
        }
        let mut result = 0;
        let mut n = num;
        while n != 0 {
            if n & 1 == 1 {
                result += 2;
            } else {
                result += 1;
            }
            n >>= 1;
        }
        result - 1
    }
}

fn main() {}
