// Leetcode problem 1769: Minimum Number of Operations to Move All Balls to Each Box.

struct Solution {}

impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let mut count = 0;
        let mut result = vec![0; boxes.len()];
        let mut acc = 0;
        for i in 0..boxes.len() {
            acc += count;
            if boxes.chars().nth(i) == Some('1') {
                count += 1;
            }
            result[i] += acc;
        }
        count = 0;
        acc = 0;
        for i in (0..boxes.len()).rev() {
            acc += count;
            if boxes.chars().nth(i) == Some('1') {
                count += 1;
            }
            result[i] += acc;
        }
        result
    }
}

fn main() {}
