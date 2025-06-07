// Leetcode problem 3362: Zero Array Transformation III.

use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn max_removal(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let mut queries = queries.clone();
        queries.sort_unstable();
        let mut heap = BinaryHeap::new();
        let mut delta = vec![0; nums.len() + 1];
        let mut operations = 0;
        let mut j = 0;
        for i in 0..nums.len() {
            operations += delta[i];
            while j < queries.len() && queries[j][0] == i as i32 {
                heap.push(queries[j][1]);
                j += 1;
            }
            while operations < nums[i] && !heap.is_empty() && *heap.peek().unwrap() >= i as i32 {
                operations += 1;
                delta[heap.pop().unwrap() as usize + 1] -= 1;
            }
            if operations < nums[i] {
                return -1;
            }
        }
        heap.len() as i32
    }
}

fn main() {}
