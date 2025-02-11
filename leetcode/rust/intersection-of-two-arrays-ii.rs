// Leetcode problem 350: Intersection of Two Arrays II.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut table = HashMap::new();
        let mut result = vec![];
        for num in nums1 {
            *table.entry(num).or_insert(0) += 1;
        }
        for num in nums2 {
            match table.get(&num) {
                Some(i) => {
                    result.push(num);
                    if i - 1 == 0 {
                        table.remove(&num);
                    } else {
                        table.insert(num, i - 1);
                    }
                }
                _ => {}
            }
        }
        result
    }
}

fn main() {}
