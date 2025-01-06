// Leetcode problem 1431: Kids With the Greatest Number of Candies.

struct Solution {}

impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let maximum = candies.iter().max().unwrap();
        let mut result = Vec::new();
        for candy in candies.iter() {
            result.push(*maximum <= candy + extra_candies);
        }
        result
    }
}

fn main() {}
