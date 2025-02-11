// Leetcode problem 335: Minimum Amount of Time to Fill Cups.

struct Solution {}

impl Solution {
    pub fn fill_cups(amount: Vec<i32>) -> i32 {
        let mut result = 0;
        let mut sorted_amount = amount.clone();
        loop {
            sorted_amount.sort_unstable();
            if *sorted_amount.last().unwrap() == 0 {
                break;
            }
            sorted_amount
                .iter_mut()
                .rev()
                .take(2)
                .for_each(|cup| *cup -= 1);
            result += 1;
        }
        result
    }
}

fn main() {}
