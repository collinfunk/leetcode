// Leetcode problem 496: Next Greater Element I.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut result = vec![-1; nums1.len()];
        let mut table = HashMap::new();
        for (i, num) in nums2.iter().enumerate() {
            table.insert(num, i);
        }
        for (i, num) in nums1.iter().enumerate() {
            for j in *table.get(num).unwrap()..nums2.len() {
                if nums2[j] > *num {
                    result[i] = nums2[j];
                    break;
                }
            }
        }
        result
    }
}

fn main() {}
