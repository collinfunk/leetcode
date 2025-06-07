// Leetcode problem 135: Candy.

struct Solution {}

impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        if ratings.is_empty() {
            return 0;
        }
        let mut result = 1;
        let mut up = 0;
        let mut down = 0;
        let mut peak = 0;
        for i in 0..ratings.len() - 1 {
            let prev = ratings[i];
            let curr = ratings[i + 1];
            if prev < curr {
                up += 1;
                down = 0;
                peak = up;
                result += up + 1;
            } else if prev == curr {
                up = 0;
                down = 0;
                peak = 0;
                result += 1;
            } else {
                up = 0;
                down += 1;
                result += 1 + down;
                if peak >= down {
                    result -= 1;
                }
            }
        }
        result
    }
}

fn main() {}
