// Leetcode problem 3068: Find the Maximum Sum of Node Values.

struct Solution {}

impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, _edges: Vec<Vec<i32>>) -> i64 {
        let mut result = nums.iter().map(|&x| x as i64).sum();
        let changes: Vec<i32> = nums.iter().map(|&x| (x ^ k) - x).collect();
        let positive_changes: Vec<i32> = changes
            .iter()
            .filter(|x| x.is_positive())
            .copied()
            .collect();
        result += positive_changes.iter().map(|x| *x as i64).sum::<i64>();
        if positive_changes.len() % 2 != 0 {
            let min = positive_changes.iter().min().unwrap();
            if let Some(&swap) = changes
                .iter()
                .filter(|x| x.is_negative() && x.abs() <= *min)
                .max()
            {
                result += swap as i64;
            } else {
                result -= *min as i64;
            }
        }
        result
    }
}

fn main() {}
