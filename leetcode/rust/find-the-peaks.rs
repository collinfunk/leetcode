// Leetcode problem 2951: Find the Peaks.

struct Solution {}

impl Solution {
    pub fn find_peaks(mountain: Vec<i32>) -> Vec<i32> {
        let mut result = Vec::new();
        for i in 1..mountain.len() - 1 {
            if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1] {
                result.push(i as i32);
            }
        }
        result
    }
}

fn main() {}
