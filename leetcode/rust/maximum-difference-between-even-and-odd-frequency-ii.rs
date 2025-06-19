// Leetcode problem 3445: Maximum Difference Between Even and Odd Frequency II.

struct Solution {}

impl Solution {
    pub fn max_difference(s: String, k: i32) -> i32 {
        let n = s.len();
        let mut result = i32::MIN;
        let s = s.bytes().collect::<Vec<u8>>();
        for a in [b'0', b'1', b'2', b'3', b'4', b'5'] {
            for b in [b'0', b'1', b'2', b'3', b'4', b'5'] {
                if a == b {
                    continue;
                }
                let mut best = [i32::MAX; 4];
                let mut count_a = 0;
                let mut count_b = 0;
                let mut prev_a = 0;
                let mut prev_b = 0;
                let mut left = -1;
                for right in 0..n {
                    count_a += (s[right] == a) as i32;
                    count_b += (s[right] == b) as i32;
                    while (right as i32 - left) >= k && (count_b - prev_b) >= 2 {
                        let left_status = (((prev_a & 1) << 1) | (prev_b & 1)) as usize;
                        best[left_status] = best[left_status].min(prev_a - prev_b);
                        left += 1;
                        prev_a += (s[left as usize] == a) as i32;
                        prev_b += (s[left as usize] == b) as i32;
                    }
                    let right_status = (((count_a & 1) << 1) | (count_b & 1)) as usize;
                    if best[right_status ^ 0b10] != i32::MAX {
                        result = result.max(count_a - count_b - best[right_status ^ 0b10]);
                    }
                }
            }
        }
        result
    }
}

fn main() {}
