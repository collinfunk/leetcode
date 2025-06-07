// Leetcode problem 2359: Find Closest Node to Given Two Nodes.

struct Solution {}

impl Solution {
    pub fn closest_meeting_node(edges: Vec<i32>, node1: i32, node2: i32) -> i32 {
        fn dfs(node: i32, edges: &Vec<i32>, dist: &mut Vec<i32>, visit: &mut Vec<bool>) {
            visit[node as usize] = true;
            let neighbor = edges[node as usize];
            if neighbor != -1 && !visit[neighbor as usize] {
                dist[neighbor as usize] = 1 + dist[node as usize];
                dfs(neighbor, edges, dist, visit);
            }
        }
        let n = edges.len();
        let mut dist1 = vec![i32::MAX; n];
        let mut dist2 = vec![i32::MAX; n];
        let mut visit1 = vec![false; n];
        let mut visit2 = vec![false; n];
        dist1[node1 as usize] = 0;
        dist2[node2 as usize] = 0;
        dfs(node1, &edges, &mut dist1, &mut visit1);
        dfs(node2, &edges, &mut dist2, &mut visit2);
        let mut result = -1;
        let mut current_min_dist = i32::MAX;
        for i in 0..n {
            if current_min_dist > dist1[i].max(dist2[i]) {
                result = i as i32;
                current_min_dist = dist1[i].max(dist2[i])
            }
        }
        result
    }
}

fn main() {}
