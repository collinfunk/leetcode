// Leetcode problem 2824: Maximum Number of Words Found in Sentences.

struct Solution {}

impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        let mut result = 0;
        for sentence in sentences {
            let count = sentence.bytes().filter(|x| *x == b' ').count();
            if result < count {
                result = count;
            }
        }
        (result + 1) as i32
    }
}

fn main() {}
