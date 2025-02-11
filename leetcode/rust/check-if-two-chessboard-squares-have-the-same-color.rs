// Leetcode problem 3274: Check if Two Chessboard Squares Have the Same Color.

struct Solution {}

impl Solution {
    pub fn is_black(coordinate1: String) -> bool {
        let mut chars = coordinate1.chars();
        match chars.next() {
            Some('a') | Some('c') | Some('e') | Some('g') => match chars.next() {
                Some('1') | Some('3') | Some('5') | Some('7') => true,
                Some('2') | Some('4') | Some('6') | Some('8') => false,
                Some(_) => unreachable!(),
                None => unreachable!(),
            },
            Some('b') | Some('d') | Some('f') | Some('h') => match chars.next() {
                Some('1') | Some('3') | Some('5') | Some('7') => false,
                Some('2') | Some('4') | Some('6') | Some('8') => true,
                Some(_) => unreachable!(),
                None => unreachable!(),
            },
            Some(_) => unreachable!(),
            None => unreachable!(),
        }
    }

    pub fn check_two_chessboards(coordinate1: String, coordinate2: String) -> bool {
        Self::is_black(coordinate1) == Self::is_black(coordinate2)
    }
}

fn main() {}
