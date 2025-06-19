// Leetcode problem 2643: Row With Maximum Ones.

struct Solution {}

impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = vec![0; 2];
        for (i, row) in mat.iter().enumerate() {
            let count = row
                .iter()
                .fold(0, |acc, &x| if x == 1 { acc + 1 } else { acc });
            if result[1] < count {
                result[0] = i as i32;
                result[1] = count;
            }
        }
        result
    }
}

fn main() {}
