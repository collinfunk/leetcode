// Leetcode problem 1298: Maximum Candies You Can Get from Boxes.

use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn max_candies(
        status: Vec<i32>,
        candies: Vec<i32>,
        keys: Vec<Vec<i32>>,
        contained_boxes: Vec<Vec<i32>>,
        initial_boxes: Vec<i32>,
    ) -> i32 {
        let n = status.len();
        let mut can_open = vec![false; n];
        let mut has_box = vec![false; n];
        let mut used = vec![false; n];
        for i in 0..n {
            can_open[i] = status[i] == 1;
        }
        let mut queue = VecDeque::new();
        let mut result = 0;
        for x in initial_boxes {
            has_box[x as usize] = true;
            if can_open[x as usize] {
                queue.push_back(x);
                used[x as usize] = true;
                result += candies[x as usize];
            }
        }
        while let Some(x) = queue.pop_front() {
            for key in &keys[x as usize] {
                can_open[*key as usize] = true;
                if !used[*key as usize] && has_box[*key as usize] {
                    queue.push_back(*key);
                    used[*key as usize] = true;
                    result += candies[*key as usize];
                }
            }
            for y in &contained_boxes[x as usize] {
                has_box[*y as usize] = true;
                if !used[*y as usize] && can_open[*y as usize] {
                    queue.push_back(*y);
                    used[*y as usize] = true;
                    result += candies[*y as usize];
                }
            }
        }
        result
    }
}

fn main() {}
