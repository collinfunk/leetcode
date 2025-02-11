// Leetcode problem 441: Arranging Coins.

struct Solution {}

impl Solution {
    pub fn arrange_coins(n: i32) -> i32 {
        ((0.25 + 2.0 * (n as f64)).sqrt() - 0.5).floor() as i32
    }
}

fn main() {}
