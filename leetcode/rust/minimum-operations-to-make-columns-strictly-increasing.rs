// Leetcode problem 3402: Minimum Operations to Make Columns Strictly Increasing.

struct Solution {}

impl Solution {
    pub fn minimum_operations(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut result = 0;
        for i in 0..n {
            let mut maximum = -1;
            for j in 0..m {
                let val = grid[j][i];
                maximum = val.max(maximum + 1);
                result += maximum - val;
            }
        }
        result
    }
}

fn main() {}
