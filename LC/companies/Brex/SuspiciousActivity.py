"""
Link: https://leetcode.com/discuss/interview-question/2023712/Brex-Technical-Phone-Screen-2022-Suspicious-Activity

Question:
We have a set of known suspicious user activities and a batch of new user activities. An activity is an ordered tuple of attributes.
Using the known set, we want to find activities in the new batch that are suspicious.

To do so, we have set up a simple hypothesis -

An activity is suspicious if it is “similar” to any other suspicious activity, including suspicious activities from the new batch.
An activity is similar to another activity if they have the same values for at least k attributes.
Given the set of known suspicious activities, similarity factor k and the set of new activities,
determine which of the new activities are suspicious according to the above hypothesis.

suspicious_activities = [
       ("Albert", "San Francisco", "deposit"),
       ("Brad", "San Francisco", "withdraw"),
       ("Claire", "New York", "withdraw")
]

new_activities = [
       ("Joe", "Miami", "withdraw"),
       ("John", "San Francisco", "deposit"),
       ("Diana", "London", "withdraw"),
       ("Diana", "San Francisco", "withdraw"),
       ("Albert", "London", "withdraw"),
       ("Joe", "New York", "update_address"),
       ("Claire", "Miami", "deposit"),
       ("Diana", "New York", "deposit"),
       ("Albert", "Chicago", "withdraw"),
       ("Brad", "Paris", "deposit"),
       ("Claire", "Paris", "deposit"),
       ("Diana", "Vancouver", "file_dispute"),
       ("John", "Mumbai", "withdraw")
]

# Number of equal attributes for "similarity", k = 2;

new_suspicious_activities = [
  ("John", "San Francisco", "deposit"),
  ("Diana", "San Francisco", "withdraw"),
  ("Diana", "London", "withdraw"),
  ("Albert", "London", "withdraw"),
  ("Albert", "Chicago", withdraw")
]
"""
from typing import List, Tuple

def find_suspicious_activities(suspicious_activities: List[Tuple], new_activities: List[Tuple], k: int) -> List[Tuple]:
  if not suspicious_activities or not new_activities:
    return []
  
  new_suspicious_activities = []

  # Current activity is marked suspicious
  marked_suspicious = [False] * len(new_activities)
  i = 0

  while i < len(new_activities):
    # Skip if marked suspicious already
    if marked_suspicious[i]:
      i += 1
      continue

    if is_suspicious_activity(suspicious_activities, new_activities[i], k) or\
        is_suspicious_activity(new_suspicious_activities, new_activities[i], k):
      new_suspicious_activities.append(new_activities[i])

      # Start from the beginning of the list since newly added activity
      # can be "similar" to already iterated activities
      marked_suspicious[i] = True
      i = 0
      continue

    i += 1

  return new_suspicious_activities

def is_suspicious_activity(suspicious_activities: List[Tuple], activity: List[Tuple], k: int) -> bool:
  if not suspicious_activities:
    return False
  
  for suspicious_activitiy in suspicious_activities:
    union_set = set(suspicious_activitiy + activity)
    if len(union_set) == len(suspicious_activitiy):
      return False
    if len(union_set) - len(suspicious_activitiy) < k:
      return True

  return False

print('Expected: False, actual: ', is_suspicious_activity([
       ("Albert", "San Francisco", "deposit"),
       ("Brad", "San Francisco", "withdraw"),
       ("Claire", "New York", "withdraw")
], ("Joe", "Miami", "withdraw"), 2))

print('Expected: True, actual: ', is_suspicious_activity([
       ("Albert", "San Francisco", "deposit"),
       ("Brad", "San Francisco", "withdraw"),
       ("Claire", "New York", "withdraw")
], ("Diana", "San Francisco", "withdraw"), 2))

print('Expected: True, actual: ',is_suspicious_activity(
  [('John', 'San Francisco', 'deposit'),
    ('Diana', 'San Francisco', 'withdraw'),
    ('Diana', 'London', 'withdraw')
  ],
  ("Albert", "London", "withdraw"),
2))

print(find_suspicious_activities([
       ("Albert", "San Francisco", "deposit"),
       ("Brad", "San Francisco", "withdraw"),
       ("Claire", "New York", "withdraw")
], [
       ("Joe", "Miami", "withdraw"),
       ("John", "San Francisco", "deposit"),
       ("Diana", "London", "withdraw"),
       ("Diana", "San Francisco", "withdraw"),
       ("Albert", "London", "withdraw"),
       ("Joe", "New York", "update_address"),
       ("Claire", "Miami", "deposit"),
       ("Diana", "New York", "deposit"),
       ("Albert", "Chicago", "withdraw"),
       ("Brad", "Paris", "deposit"),
       ("Claire", "Paris", "deposit"),
       ("Diana", "Vancouver", "file_dispute"),
       ("John", "Mumbai", "withdraw")
], 2))
