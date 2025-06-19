// Leetcode problem 440: K-th Smallest in Lexicographical Order.

struct Solution {}

impl Solution {
    pub fn find_kth_number(n: i32, k: i32) -> i32 {
        fn count_prefix(n: i64, prefix: i64) -> i32 {
            let mut curr = prefix;
            let mut next = prefix + 1;
            let mut count = 0;
            while curr <= n {
                count += ((n + 1).min(next) - curr) as i32;
                curr *= 10;
                next *= 10;
            }
            count
        }
        let mut result = 1;
        let mut k = k - 1;
        while 0 < k {
            let step = count_prefix(n as i64, result as i64);
            if step <= k {
                result += 1;
                k -= step;
            } else {
                result *= 10;
                k -= 1;
            }
        }
        result
    }
}

fn main() {}
