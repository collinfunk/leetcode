// Leetcode problem 1365: How Many Numbers Are Smaller Than the Current Number.

struct Solution {}

impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let mut table = vec![0; 101];
        for num in &nums {
            table[*num as usize] += 1;
        }
        for i in 1..101 {
            table[i] += table[i - 1];
        }
        nums.into_iter()
            .map(|x| if x == 0 { 0 } else { table[x as usize - 1] })
            .collect()
    }
}

fn main() {}
