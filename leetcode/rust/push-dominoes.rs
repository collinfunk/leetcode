// Leetcode problem 838: Push Dominoes.

struct Solution {}

impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let n = dominoes.len();
        let mut forces = Vec::with_capacity(n);
        let mut force: i32 = 0;
        for ch in dominoes.chars() {
            match ch {
                'R' => force = n as i32,
                'L' => force = 0,
                '.' => force = (force - 1).max(0),
                _ => unreachable!(),
            }
            forces.push(force);
        }
        force = 0;
        let mut i = n - 1;
        for ch in dominoes.chars().rev() {
            match ch {
                'L' => force = n as i32,
                'R' => force = 0,
                '.' => force = (force - 1).max(0),
                _ => unreachable!(),
            }
            forces[i] -= force;
            i -= 1;
        }
        let mut result = String::with_capacity(n);
        for value in forces {
            if 0 < value {
                result.push('R');
            } else if value < 0 {
                result.push('L');
            } else {
                result.push('.');
            }
        }
        result
    }
}

fn main() {}
