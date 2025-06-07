// Leetcode problem 3024: Type of Triangle.

struct Solution {}

impl Solution {
    pub fn triangle_type(nums: Vec<i32>) -> String {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort_unstable();
        if sorted_nums[0] + sorted_nums[1] <= sorted_nums[2] {
            "none".to_string()
        } else if sorted_nums[0] == sorted_nums[2] {
            "equilateral".to_string()
        } else if sorted_nums[0] == sorted_nums[1] || sorted_nums[1] == sorted_nums[2] {
            "isosceles".to_string()
        } else {
            "scalene".to_string()
        }
    }
}

fn main() {}
