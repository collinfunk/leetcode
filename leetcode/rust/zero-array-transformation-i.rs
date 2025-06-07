// Leetcode problem 3355: Zero Array Transformation I.

struct Solution {}

impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> bool {
        let mut differences = vec![0; nums.len() + 1];
        for query in queries {
            differences[query[0] as usize] += 1;
            differences[query[1] as usize + 1] -= 1;
        }
        let mut operations = Vec::with_capacity(differences.len());
        let mut current = 0;
        for difference in differences {
            current += difference;
            operations.push(current);
        }
        for i in 0..nums.len() {
            if operations[i] < nums[i] {
                return false;
            }
        }
        true
    }
}

fn main() {}
