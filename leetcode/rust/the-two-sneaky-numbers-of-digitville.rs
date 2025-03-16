// Leetcode problem 3289: The Two Sneaky Numbers of Digitville.

struct Solution {}

impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut table = [0; 100];
        let mut result = vec![0; 2];
        let mut index = 0;
        for num in nums {
            table[num as usize] += 1;
            if 1 < table[num as usize] {
                result[index] = num;
                index += 1;
            }
            if index == 2 {
                break;
            }
        }
        result
    }
}

fn main() {}
