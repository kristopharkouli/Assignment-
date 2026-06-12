
from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce

# Activity record format:
# {
#     "user": str,
#     "action": str,
#     "duration": float
# }

def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:
    users = {log["user"] for log in logs}

    return {
        user: reduce(
            lambda total, log: total + log["duration"]
            if log["user"] == user else total,
            logs,
            0.0
        )
        for user in users
    }

def most_active_users(logs: List[Dict], k: int) -> List[str]:
    totals = defaultdict(float)

    for log in logs:
        totals[log["user"]] += log["duration"]

    return [
        user for user, _ in
        sorted(totals.items(),
               key=lambda item: item[1],
               reverse=True)[:k]
    ]

def unique_actions(logs: List[Dict]) -> Set[str]:
    return {log["action"] for log in logs}


# Sample Data
logs = [
    {"user": "CSB24001", "action": "YouTube", "duration": 45.5},
    {"user": "CSB24002", "action": "Instagram", "duration": 30.0},
    {"user": "CSB24001", "action": "Google", "duration": 20.0},
    {"user": "CSB24003", "action": "WhatsApp", "duration": 60.0},
    {"user": "CSB24002", "action": "YouTube", "duration": 25.0},
]

print("Total Time Per User:")
print(total_time_per_user(logs))

print("\nMost Active Users:")
print(most_active_users(logs, 2))

print("\nUnique Actions:")
print(unique_actions(logs))

"""
Complexity Analysis

1. Time Complexity for Top K Users:
   - Building totals dictionary: O(n)
   - Sorting users: O(m log m)
     where m = number of unique users
   - Total: O(n + m log m)

2. Space Complexity:
   - totals dictionary: O(m)
   - unique actions set: O(a)
     where a = number of unique actions
   - Overall auxiliary space: O(m + a)
"""
