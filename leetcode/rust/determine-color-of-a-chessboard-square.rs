// Leetcode problem 1812: Determine Color of a Chessboard Square.

struct Solution {}

impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        coordinates.bytes().map(|x| x % 2).sum::<u8>() == 1
    }
}

fn main() {}
