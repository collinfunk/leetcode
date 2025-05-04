// Leetcode problem 3516: Find Closest Person.

struct Solution {}

impl Solution {
    pub fn find_closest(x: i32, y: i32, z: i32) -> i32 {
        let dist1 = (z - x).abs();
        let dist2 = (z - y).abs();
        if dist1 == dist2 {
            0
        } else if dist1 < dist2 {
            1
        } else {
            2
        }
    }
}

fn main() {}
