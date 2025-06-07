// Leetcode problem 3337. Total Characters in String After Transformations II.

struct Solution {}

struct Matrix {
    a: [[i64; 26]; 26],
}

impl Matrix {
    fn new() -> Self {
        Matrix { a: [[0; 26]; 26] }
    }

    fn copy_from(&mut self, other: &Matrix) {
        for i in 0..26 {
            for j in 0..26 {
                self.a[i][j] = other.a[i][j];
            }
        }
    }

    fn mul(&self, other: &Matrix) -> Matrix {
        let mut result = Matrix::new();
        for i in 0..26 {
            for j in 0..26 {
                for k in 0..26 {
                    result.a[i][j] =
                        (result.a[i][j] + self.a[i][k] * other.a[k][j]) % 1_000_000_007;
                }
            }
        }
        result
    }
}

fn identity_matrix() -> Matrix {
    let mut result = Matrix::new();
    for i in 0..26 {
        result.a[i][i] = 1;
    }
    result
}

fn quick_mul(x: &Matrix, mut y: i32) -> Matrix {
    let mut result = identity_matrix();
    let mut current = Matrix::new();
    current.copy_from(x);
    while y > 0 {
        if y & 1 == 1 {
            result = result.mul(&current);
        }
        current = current.mul(&current);
        y >>= 1;
    }
    result
}

impl Solution {
    pub fn length_after_transformations(s: String, t: i32, nums: Vec<i32>) -> i32 {
        let mut matrix1 = Matrix::new();
        for (i, x) in nums.iter().enumerate().take(26) {
            for j in 1..=*x as usize {
                matrix1.a[(i + j) % 26][i] = 1;
            }
        }
        let matrix2 = quick_mul(&matrix1, t);
        let mut f = [0; 26];
        for ch in s.bytes() {
            f[(ch - b'a') as usize] += 1;
        }
        let mut result: i64 = 0;
        for i in 0..26 {
            for (j, x) in f.iter().enumerate() {
                result = (result + matrix2.a[i][j] * x) % 1_000_000_007;
            }
        }
        result as i32
    }
}

fn main() {}
