// Leetcode problem 790: Domino and Tromino Tiling.

struct Solution {}

impl Solution {
    pub fn num_tilings(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = Vec::with_capacity(n + 3);
        dp.push(1);
        dp.push(2);
        dp.push(5);
        for i in 3..n {
            dp.push((((dp[i - 1] * 2) % 1000000007) + dp[i - 3]) % 1000000007);
        }
        dp[n - 1]
    }
}

fn main() {}
