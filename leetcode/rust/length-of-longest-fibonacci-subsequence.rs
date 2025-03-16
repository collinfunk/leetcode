// Leetcode problem 873: Length of Longest Fibonacci Subsequence.

struct Solution {}

impl Solution {
    pub fn len_longest_fib_subseq(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut dp = vec![vec![0; n]; n];
        let mut max_length = 0;
        for i in 2..n {
            let mut start = 0;
            let mut end = i - 1;
            while start < end {
                let sum = arr[start] + arr[end];
                if sum < arr[i] {
                    start += 1;
                } else if sum > arr[i] {
                    end -= 1;
                } else {
                    // sum == arr[i]
                    dp[end][i] = dp[start][end] + 1;
                    max_length = max_length.max(dp[end][i]);
                    end -= 1;
                    start += 1;
                }
            }
        }
        if max_length != 0 {
            max_length += 2;
        }
        max_length
    }
}

fn main() {}
