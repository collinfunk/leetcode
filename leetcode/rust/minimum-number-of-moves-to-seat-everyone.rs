// Leetcode problem 2037: Minimum Number of Moves to Seat Everyone.

struct Solution {}

impl Solution {
    pub fn min_moves_to_seat(seats: Vec<i32>, students: Vec<i32>) -> i32 {
        let max_position = *seats.iter().max().max(students.iter().max()).unwrap();
        let mut differences = vec![0; max_position as usize];
        for seat in seats {
            differences[seat as usize - 1] += 1;
        }
        for student in students {
            differences[student as usize - 1] -= 1;
        }
        let mut result = 0;
        let mut unmatched: i32 = 0;
        for difference in differences {
            result += unmatched.abs();
            unmatched += difference;
        }
        result
    }
}

fn main() {}
