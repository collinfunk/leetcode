// Leetcode problem 492: Construct the Rectangle.

struct Solution {}

impl Solution {
    pub fn construct_rectangle(area: i32) -> Vec<i32> {
        let mut maximum = (area as f32).sqrt() as i32;
        while area % maximum != 0 {
            maximum -= 1;
        }
        vec![area / maximum, maximum]
    }
}

fn main() {}
