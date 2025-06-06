// Leetcode problem 1773: Count Items Matching a Rule.

struct Solution {}

impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        let key_index = match &rule_key[..] {
            "type" => 0,
            "color" => 1,
            "name" => 2,
            _ => unreachable!(),
        };
        items
            .iter()
            .filter(|item| item[key_index] == rule_value)
            .count() as i32
    }
}

fn main() {}
