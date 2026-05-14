class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n

    def find(self, v) -> int:
        if self.parents[v] == v:
            return v
        self.parents[v] = self.find(self.parents[v])
        return self.parents[v]

    def union(self, v1, v2) -> bool:
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False

        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        elif self.ranks[p2] > self.ranks[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccountIdx = {}
        for idx, account in enumerate(accounts):
            name = account[0]

            for i in range(1, len(account)):
                email = account[i]
                if email not in emailToAccountIdx:
                    emailToAccountIdx[email] = idx
                else:
                    uf.union(emailToAccountIdx[email], idx)

            
        group = defaultdict(list)
        for email, idx in emailToAccountIdx.items():
            rootIdx = uf.find(idx)
            group[rootIdx].append(email)

        res = []
        for idx, emails in group.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails))
        return res


        