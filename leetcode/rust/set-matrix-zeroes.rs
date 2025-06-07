// Leetcode problem 73: Set Matrix Zeroes.

struct Solution {}

impl Solution {
    pub fn set_zeroes(matrix: &mut [Vec<i32>]) {
        let n = matrix.len();
        let m = matrix[0].len();
        let mut tmp = 1;
        for i in 0..n {
            if matrix[i][0] == 0 {
                tmp = 0;
            }
            for j in 1..m {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for i in (0..n).rev() {
            for j in (1..m).rev() {
                if matrix[i][0] == 0 || matrix[0][j] == 0 {
                    matrix[i][j] = 0;
                }
            }
            if tmp == 0 {
                matrix[i][0] = 0;
            }
        }
    }
}

fn main() {}
