// Leetcode problem 1078: Occurrences After Bigram.

struct Solution {}

impl Solution {
    pub fn find_ocurrences(text: String, first: String, second: String) -> Vec<String> {
        text.split(' ')
            .collect::<Vec<_>>()
            .windows(3)
            .filter_map(|w| (w[..2] == [&first, &second]).then_some(w[2].to_string()))
            .collect()
    }
}

fn main() {}
