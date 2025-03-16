// Leetcode problem 728: Self Dividing Numbers.

struct Solution {}

impl Solution {
    pub fn self_dividing_numbers(left: i32, right: i32) -> Vec<i32> {
        let mut result = Vec::new();
        for i in left..right + 1 {
            if i % 10 == 0 {
                continue;
            }
            let digits: Vec<u8> = i.to_string().bytes().map(|c| c - b'0').collect();
            let mut okay = true;
            for digit in digits {
                if digit == 0 || i % digit as i32 != 0 {
                    okay = false;
                    break;
                }
            }
            if okay {
                result.push(i);
            }
        }
        result
    }
}

fn main() {}
