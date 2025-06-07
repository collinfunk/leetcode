// Leetcode problem 1061: Lexicographically Smallest Equivalent String.

struct Solution {}

impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        fn get(root: &mut Vec<usize>, x: usize) -> usize {
            if x == root[x] {
                return x;
            }
            root[x] = get(root, root[x]);
            root[x]
        }
        fn union(root: &mut Vec<usize>, x: usize, y: usize) {
            let x = get(root, x);
            let y = get(root, y);
            if x == y {
                return;
            }
            if x < y {
                root[y] = x;
            } else {
                root[x] = y;
            }
        }
        let s1 = s1.chars().collect::<Vec<char>>();
        let s2 = s2.chars().collect::<Vec<char>>();
        let mut root: Vec<usize> = (0..26).collect();
        for i in 0..s1.len() {
            let u = (s1[i] as u8 - b'a') as usize;
            let v = (s2[i] as u8 - b'a') as usize;
            union(&mut root, u, v);
        }
        let mut result = String::new();
        for c in base_str.bytes() {
            let k = (c - b'a') as usize;
            let ch = get(&mut root, k) as u8 + b'a';
            result.push(ch as char);
        }
        result
    }
}

fn main() {}
