// Leetcode problem 2999: Count the Number of Powerful Integers.

struct Solution {}

impl Solution {
    pub fn calculate(x: &str, s: &str, limit: i32) -> i64 {
        if x.len() < s.len() {
            return 0;
        }
        if x.len() == s.len() {
            if x >= s {
                return 1;
            } else {
                return 0;
            }
        }
        let pre_len = x.len() - s.len();
        let suffix = &x[pre_len..];
        let mut count = 0i64;
        for i in 0..pre_len {
            let digit = x.chars().nth(i).unwrap().to_digit(10).unwrap() as i32;
            if limit < digit {
                count += ((limit + 1) as i64).pow((pre_len - i) as u32);
                return count;
            }
            count += (digit as i64) * ((limit + 1) as i64).pow((pre_len - 1 - i) as u32);
        }
        if suffix >= s {
            count += 1;
        }
        count
    }

    pub fn number_of_powerful_int(start: i64, finish: i64, limit: i32, s: String) -> i64 {
        let start = (start - 1).to_string();
        let finish = finish.to_string();
        Self::calculate(&finish, &s, limit);
        Self::calculate(&start, &s, limit);
        Self::calculate(&finish, &s, limit) - Self::calculate(&start, &s, limit)
    }
}

fn main() {}
