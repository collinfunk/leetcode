// Leetcode problem 1108: Defanging an IP Address.

struct Solution {}

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        address.replace(".", "[.]")
    }
}

fn main() {}
