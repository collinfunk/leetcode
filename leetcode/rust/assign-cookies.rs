// Leetcode problem 455: Assign Cookies.

use std::convert::TryInto;

struct Solution {}

impl Solution {
    pub fn find_content_children(g: Vec<i32>, s: Vec<i32>) -> i32 {
        let mut greed = g;
        let mut size = s;
        let mut count = 0;

        greed.sort();
        size.sort();

        for cookie in size {
            if count < greed.len().into() && cookie >= greed[count] {
                count += 1;
            }
        }
        count.try_into().unwrap()
    }
}

fn main() {}
