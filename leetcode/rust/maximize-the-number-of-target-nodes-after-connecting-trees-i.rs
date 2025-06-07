// Leetcode problem 3372: Maximize the Number of Target Nodes After Connecting Trees I.

struct Solution {}

impl Solution {
    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        fn build(edges: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
            fn dfs(node: usize, parent: i32, children: &Vec<Vec<i32>>, k: i32) -> i32 {
                if k < 0 {
                    return 0;
                }
                let mut result = 1;
                for &child in &children[node] {
                    if child != parent {
                        result += dfs(child as usize, node as i32, children, k - 1);
                    }
                }
                result
            }
            let n = edges.len() + 1;
            let mut children = vec![vec![]; n];
            for edge in edges {
                let u = edge[0] as usize;
                let v = edge[1] as usize;
                children[u].push(v as i32);
                children[v].push(u as i32);
            }
            let mut result = vec![0; n];
            for (i, value) in result.iter_mut().enumerate().take(n) {
                *value = dfs(i, -1, &children, k);
            }
            result
        }
        let n = edges1.len() + 1;
        let count1 = build(edges1, k);
        let count2 = build(edges2, k - 1);
        let max_count2 = count2.iter().max().unwrap();
        let mut result = vec![0; n];
        for i in 0..n {
            result[i] = count1[i] + max_count2;
        }
        result
    }
}

fn main() {}
