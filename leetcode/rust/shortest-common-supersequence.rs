// Leetcode problem 1092: Shortest Common Supersequence.

struct Solution {}

impl Solution {
    pub fn shortest_common_supersequence(str1: String, str2: String) -> String {
        let s1 = str1.as_bytes();
        let s2 = str2.as_bytes();
        let mut dp = vec![vec![0; s2.len() + 1]; s1.len() + 1];
        for i in 1..s1.len() + 1 {
            for j in 1..s2.len() + 1 {
                if s1[i - 1] == s2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]);
                }
            }
        }
        let mut i = s1.len();
        let mut j = s2.len();
        let mut result = String::new();
        while 0 < i && 0 < j {
            if s1[i - 1] == s2[j - 1] {
                result.insert(0, s1[i - 1] as char);
                i -= 1;
                j -= 1;
            } else if dp[i - 1][j] > dp[i][j - 1] {
                result.insert(0, s1[i - 1] as char);
                i -= 1;
            } else {
                result.insert(0, s2[j - 1] as char);
                j -= 1;
            }
        }
        while i > 0 {
            result.insert(0, s1[i - 1] as char);
            i -= 1;
        }
        while j > 0 {
            result.insert(0, s2[j - 1] as char);
            j -= 1;
        }
        result
    }
}

fn main() {}
