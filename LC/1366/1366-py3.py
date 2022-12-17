"""
["ABC","ACB","ABC","ACB","ACB"]
A - 5 x 1 - [5,0,0]
B - 2 X 2, 3 x 3 - [0,2,3]
C - 3 x 2, 2 x 3 - [0,3,2]


["WXYZ","XYZW"]
W - [1,0,0,1]
X - [1,1,0,0]
Y - [0,1,1,0]
Z - [0,0,1,1]

"""
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) <= 1:
            return "" if not votes else votes[0]
        
        team_set = set()
        for vote in votes:
            for team in vote:
                team_set.add(team)
        tiers_count = len(team_set)
        tiers = [[0] * tiers_count for _ in range(tiers_count)]
        team_map = dict()

        for i, team in enumerate(list(team_set)):
            team_map[team] = i
        
        for vote in votes:
            for rank, team in enumerate(vote):
                tiers[team_map[team]][rank] -= 1

        ranks = sorted(team_map.keys(), key=lambda team: (*tiers[team_map[team]], team))[:len(votes[0])]
        return "".join(ranks)
