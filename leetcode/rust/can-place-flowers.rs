// Leetcode problem 605: Can Place Flowers.

struct Solution {}

impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        if n == 0 {
            return true;
        }
        let mut working = flowerbed.clone();
        let mut remaining = n;
        for i in 0..working.len() {
            if working[i] == 0 {
                if (i == 0 || working[i - 1] == 0)
                    && (i == working.len() - 1 || working[i + 1] == 0)
                {
                    remaining -= 1;
                    if remaining == 0 {
                        return true;
                    }
                    working[i] = 1;
                }
            }
        }
        false
    }
}

fn main() {}
