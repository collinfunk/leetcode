// Leetcode problem 303: Range Sum Query - Immutable.

struct NumArray {
    nums: Vec<i32>,
}

impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        Self { nums: nums }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let mut result = 0;
        for i in left..=right {
            result += self.nums[i as usize];
        }
        result
    }
}
