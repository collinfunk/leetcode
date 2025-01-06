// Leetcode problem 933: Number of Recent Calls.

use std::collections::VecDeque;
use std::convert::TryInto;

struct RecentCounter {
    queue: VecDeque<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RecentCounter {
    fn new() -> Self {
        Self {
            queue: VecDeque::new(),
        }
    }

    fn ping(&mut self, t: i32) -> i32 {
        while self.queue.front().map_or(false, |x| *x < t) {
            self.queue.pop_front();
        }
        self.queue.push_back(t + 3000);
        self.queue.len().try_into().unwrap()
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * let obj = RecentCounter::new();
 * let ret_1: i32 = obj.ping(t);
 */
fn main() {}
