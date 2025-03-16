// Leetcode problem 1281: Subtract the Product and Sum of Digits of an Integer.

struct Solution {}

impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 {
        let string = n.to_string();
        let digits = string.chars().map(|c| c.to_digit(10).unwrap() as i32);
        let product: i32 = digits.clone().product();
        let sum: i32 = digits.sum();
        product - sum
    }
}

fn main() {}
