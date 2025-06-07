// Leetcode problem 75: Sort Colors.

struct Solution {}

impl Solution {
    pub fn sort_colors(nums: &mut [i32]) {
        let mut i = 0;
        let mut j = 0;
        let mut k = nums.len() - 1;
        while j <= k {
            match nums[j] {
                0 => {
                    nums.swap(i, j);
                    i += 1;
                    j += 1;
                }
                1 => {
                    j += 1;
                }
                2 => {
                    nums.swap(j, k);
                    if k == 0 {
                        break;
                    }
                    k -= 1;
                }
                _ => {}
            }
        }
    }
}

fn main() {}
