// Leetcode problem: Number of Sub-arrays With Odd Sum.

struct Solution {}

impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let mut prefix_sum = 0;
        let mut odd_count = 0;
        let mut even_count = 1;
        let mut count = 0;
        for number in arr {
            prefix_sum += number;
            if prefix_sum % 2 == 0 {
                count += odd_count;
                even_count += 1;
            } else {
                count += even_count;
                odd_count += 1;
            }
            count %= i32::pow(10, 9) + 7
        }
        count
    }
}

fn main() {}
