// Leetcode problem 1598: Crawler Log Folder.

struct Solution {}

impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut result = 0;
        for operation in logs {
            match operation.as_str() {
                "../" => {
                    if result > 0 {
                        result -= 1
                    }
                }
                "./" => continue,
                &_ => result += 1,
            }
        }
        result
    }
}

fn main() {}
