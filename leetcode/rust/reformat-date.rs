// Leetcode problem 1507: Reformat Date.

struct Solution {}

impl Solution {
    pub fn reformat_date(date: String) -> String {
        let months = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
        ];
        let parts = date.split_whitespace().collect::<Vec<_>>();
        let mut day_index = 0;
        for (i, ch) in parts[0].chars().enumerate() {
            if !ch.is_digit(10) {
                day_index = i;
                break;
            }
        }
        let day = format!("{:02}", parts[0][..day_index].parse::<i8>().unwrap());
        let month = format!(
            "{:02}",
            months.iter().position(|m| *m == parts[1]).unwrap() + 1
        );
        [parts[2], &month, &day].join("-")
    }
}

fn main() {}
