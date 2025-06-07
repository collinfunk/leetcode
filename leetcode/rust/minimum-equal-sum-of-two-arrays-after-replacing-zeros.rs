// Leetcode problem 2918: Minimum Equal Sum of Two Arrays After Replacing Zeros.

struct Solution {}

impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut sum1 = 0_i64;
        let mut zero1 = 0;
        for num in nums1 {
            sum1 += num as i64;
            if num == 0 {
                sum1 += 1;
                zero1 += 1;
            }
        }
        let mut sum2 = 0_i64;
        let mut zero2 = 0;
        for num in nums2 {
            sum2 += num as i64;
            if num == 0 {
                sum2 += 1;
                zero2 += 1;
            }
        }
        if (zero1 == 0 && sum2 > sum1) || (zero2 == 0 && sum1 > sum2) {
            -1
        } else {
            sum1.max(sum2)
        }
    }
}

fn main() {}
