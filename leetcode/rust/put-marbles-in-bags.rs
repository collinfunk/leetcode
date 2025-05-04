// Leetcode problem 2551: Put Marbles in Bags.

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn put_marbles(weights: Vec<i32>, k: i32) -> i64 {
        let mut increasing = BinaryHeap::with_capacity(weights.len() - 1);
        let mut decreasing = BinaryHeap::with_capacity(weights.len() - 1);
        for i in 1..weights.len() {
            increasing.push(weights[i] + weights[i - 1]);
            decreasing.push(Reverse(weights[i] + weights[i - 1]));
        }
        let mut min = (weights[0] + weights[weights.len() - 1]) as i64;
        let mut max = min;
        for _ in 1..k {
            max += increasing.pop().unwrap() as i64;
            min += decreasing.pop().unwrap().0 as i64;
        }
        max - min
    }
}

fn main() {}
