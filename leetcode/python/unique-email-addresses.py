#!/usr/bin/env python3

""" Leetcode problem 929: Unique Email Addresses. """


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            parts = local.split('+')
            if len(local) != 1:
                local = parts[0]
            result.add(f'{local}@{domain}')
        return len(result)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
