// Leetcode problem 3341: Find Minimum Time to Reach Last Room I.

use std::cmp::{max, Reverse};
use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let n = move_time.len();
        let m = move_time[0].len();
        let infinity = i32::MAX / 2;
        let mut d = vec![vec![infinity; m]; n];
        let mut v = vec![vec![false; m]; n];
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        let mut queue = BinaryHeap::new();
        d[0][0] = 0;
        queue.push(Reverse((0, 0_usize, 0_usize)));
        while let Some(Reverse((_, x, y))) = queue.pop() {
            if v[x][y] {
                continue;
            }
            v[x][y] = true;
            for (dx, dy) in directions {
                let nx = x as isize + dx;
                let ny = y as isize + dy;
                if nx < 0 || nx >= n as isize || ny < 0 || ny >= m as isize {
                    continue;
                }
                let nx = nx as usize;
                let ny = ny as usize;
                let distance = max(d[x][y], move_time[nx][ny]) + 1;
                if d[nx][ny] > distance {
                    d[nx][ny] = distance;
                    queue.push(Reverse((distance, nx, ny)));
                }
            }
        }
        d[n - 1][m - 1]
    }
}

fn main() {}
