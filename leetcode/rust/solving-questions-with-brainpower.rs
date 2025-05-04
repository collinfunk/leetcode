// Leetcode problem 2140: Solving Questions With Brainpower.

struct Solution {}

impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        let mut table = vec![0; questions.len() + 1];
        for i in 0..questions.len() {
            table[i + 1] = table[i + 1].max(table[i]);
            let (points, brainpower) = (questions[i][0] as i64, questions[i][1] as i64);
            let j = (i + brainpower as usize + 1).min(questions.len());
            table[j] = table[j].max(table[i] + points);
        }
        table[questions.len()]
    }
}

fn main() {}
