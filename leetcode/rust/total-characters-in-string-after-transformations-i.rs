// Leetcode problem 3335: Total Characters in String After Transformations I.

struct Solution {}

impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        let mut table = [0; 26];
        for ch in s.bytes() {
            table[(ch - b'a') as usize] += 1;
        }
        for _ in 0..t {
            let mut next = [0; 26];
            next[0] = table[25];
            next[1] = (table[25] + table[0]) % 1_000_000_007;
            next[2..26].copy_from_slice(&table[(2 - 1)..(26 - 1)]);
            table = next
        }
        table.iter().fold(0, |acc, x| (acc + x) % 1_000_000_007)
    }
}

fn main() {}
