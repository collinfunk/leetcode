// Leetcode problem 2011: Final Value of Variable After Performing Operations.

struct Solution {}

impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        operations.iter().fold(0, |acc, operation| {
            if operation.contains("-") {
                acc - 1
            } else {
                acc + 1
            }
        })
    }
}

fn main() {}
