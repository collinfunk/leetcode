// Leetcode problem 3541: Find Most Frequent Vowel and Consonant.

struct Solution {}

impl Solution {
    pub fn max_freq_sum(s: String) -> i32 {
        let mut table = [0; 26];
        for ch in s.bytes() {
            table[(ch - b'a') as usize] += 1;
        }
        let mut vowel_max = 0;
        let mut consonant_max = 0;
        for (i, &count) in table.iter().enumerate() {
            let ch = (i + ('a' as usize)) as u8;
            match ch {
                b'a' | b'e' | b'i' | b'o' | b'u' => {
                    if vowel_max < count {
                        vowel_max = count;
                    }
                }
                _ => {
                    if consonant_max < count {
                        consonant_max = count;
                    }
                }
            }
        }
        vowel_max + consonant_max
    }
}

fn main() {}
