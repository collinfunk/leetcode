// Leetcode problem 1137: N-th Tribonacci Number.

struct Solution {}

impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut table = vec![0, 1, 1];
        if n == 0 {
            return 0;
        } else if n == 1 {
            return 1;
        } else if n == 2 {
            return 1;
        } else {
            for i in 0..n {
                table.push(table[i as usize] + table[i as usize + 1] + table[i as usize + 2]);
            }
        }
        table[n as usize]
    }
}

fn main() {}
