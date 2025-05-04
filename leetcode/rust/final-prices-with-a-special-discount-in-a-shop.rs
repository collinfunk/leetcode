// Leetcode problem 1475: Final Prices With a Special Discount in a Shop.

struct Solution {}

impl Solution {
    pub fn final_prices(prices: Vec<i32>) -> Vec<i32> {
        let mut result = prices.clone();
        let mut candidates = Vec::new();
        for (i, price) in prices.iter().enumerate() {
            while let Some(&largest_index) = candidates.last() {
                if result[largest_index] >= *price {
                    result[largest_index] -= price;
                    candidates.pop();
                } else {
                    break;
                }
            }
            candidates.push(i);
        }
        result
    }
}

fn main() {}
