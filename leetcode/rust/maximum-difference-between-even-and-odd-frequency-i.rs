// Leetcode problem 3442: Maximum Difference Between Even and Odd Frequency I.

struct Solution {}

impl Solution {
    pub fn max_difference(s: String) -> i32 {
        let mut table = vec![0; 26];
        for ch in s.bytes() {
            table[(ch - b'a') as usize] += 1;
        }
        let mut highest_odd = 1;
        let mut lowest_even = s.len() as i32;
        for entry in table {
            if entry == 0 {
                continue;
            }
            if entry % 2 != 0 {
                highest_odd = highest_odd.max(entry);
            } else {
                lowest_even = lowest_even.min(entry);
            }
        }
        highest_odd - lowest_even
    }
}

fn main() {}
