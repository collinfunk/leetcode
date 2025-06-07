// Leetcode problem 2929: Distribute Candies Among Children II.

struct Solution {}

impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        fn calc(x: i32) -> i64 {
            if x < 0 {
                0
            } else {
                x as i64 * (x - 1) as i64 / 2
            }
        }
        calc(n + 2) - 3 * calc(n - limit + 1) + 3 * calc(n - (limit + 1) * 2 + 2)
            - calc(n - 3 * (limit + 1) + 2)
    }
}

fn main() {}
