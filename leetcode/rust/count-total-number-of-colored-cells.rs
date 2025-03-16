// Leetcode problem 2579: Count Total Number of Colored Cells.

struct Solution {}

impl Solution {
    pub fn colored_cells(n: i32) -> i64 {
        1 + n as i64 * (n as i64 - 1) * 2
    }
}

fn main() {}
