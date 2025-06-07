// Leetcode problem 2901: Longest Unequal Adjacent Groups Subsequence II.

struct Solution {}

impl Solution {
    pub fn check(s1: &str, s2: &str) -> bool {
        if s1.len() != s2.len() {
            return false;
        }
        let mut difference = 0;
        for (c1, c2) in s1.chars().zip(s2.chars()) {
            if c1 != c2 {
                difference += 1;
                if difference > 1 {
                    return false;
                }
            }
        }
        difference == 1
    }

    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let n = groups.len();
        let mut dp = vec![1; n];
        let mut previous = vec![-1; n];
        let mut max_index = 0;
        for i in 1..n {
            for j in 0..i {
                if Self::check(&words[i], &words[j]) && dp[j] + 1 > dp[i] && groups[i] != groups[j]
                {
                    dp[i] = dp[j] + 1;
                    previous[i] = j as i32;
                }
            }
            if dp[i] > dp[max_index] {
                max_index = i;
            }
        }
        let mut result = Vec::new();
        let mut i = max_index as i32;
        while 0 <= i {
            result.push(words[i as usize].clone());
            i = previous[i as usize];
        }
        result.into_iter().rev().collect()
    }
}

fn main() {}
