// Leetcode problem 349: Intersection of Two Arrays.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut table: HashMap<i32, i32> = nums1.into_iter().map(|x| (x, 1)).collect();
        let mut result = vec![];
        for num in nums2 {
            match table.get(&num) {
                Some(1) => {
                    result.push(num);
                    table.insert(num, 0);
                }
                _ => {}
            }
        }
        result
    }
}

fn main() {}
