// Leetcode problem 1931: Painting a Grid With Three Different Colors.

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn color_the_grid(m: i32, n: i32) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let mut table = HashMap::new();
        for mask in 0..3_i32.pow(m as u32) {
            let mut color = Vec::new();
            let mut current = mask;
            for _ in 0..m {
                color.push(current % 3);
                current /= 3;
            }
            let mut check = true;
            for i in 0..m - 1 {
                if color[i] == color[i + 1] {
                    check = false;
                    break;
                }
            }
            if check {
                table.insert(mask, color);
            }
        }
        let mut adjacent = HashMap::new();
        for (mask1, color1) in &table {
            for (mask2, color2) in &table {
                let mut check = true;
                for i in 0..m {
                    if color1[i] == color2[i] {
                        check = false;
                        break;
                    }
                }
                if check {
                    adjacent.entry(mask1).or_insert(Vec::new()).push(mask2);
                }
            }
        }
        let mut f = HashMap::new();
        for mask in table.keys() {
            f.insert(mask, 1);
        }
        for _ in 1..n {
            let mut g = HashMap::new();
            for mask2 in table.keys() {
                let mut total = 0;
                if let Some(list) = adjacent.get(mask2) {
                    for mask1 in list {
                        total = (total + f.get(mask1).unwrap_or(&0)) % 1_000_000_007;
                    }
                }
                g.insert(mask2, total);
            }
            f = g;
        }
        let mut result = 0;
        for num in f.values() {
            result = (result + num) % 1_000_000_007;
        }
        result
    }
}

fn main() {}
