// Leetcode problem 598: Range Addition II.

struct Solution {}

impl Solution {
    pub fn max_count(m: i32, n: i32, ops: Vec<Vec<i32>>) -> i32 {
        if ops.is_empty() {
            return m * n;
        }
        let mut m_max = i32::MAX;
        let mut n_max = i32::MAX;
        for op in ops {
            m_max = m_max.min(op[0]);
            n_max = n_max.min(op[1]);
        }
        m_max * n_max
    }
}

fn main() {}
