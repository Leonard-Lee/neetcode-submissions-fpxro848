class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.ranks = [1] * n

    def find(self, v) -> int:
        if self.par[v] == v:
            return self.par[v]

        self.par[v] = self.find(self.par[v])
        return self.par[v]

    def union(self, v1, v2) -> bool:
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False

        if self.ranks[p1] > self.ranks[p2]:
            self.par[p2] = p1
        elif self.ranks[p2] > self.ranks[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.ranks[p2] += 1

        return True

    
class Solution:
    # Key is this part
    # 1. map all emails to its current idx
    # if an email mapping two idx, union these two idxes

    # 2. iterate through all the emails in the previous map
    # find their root idx, use the root idx to group all the belonging emails

    # 3. populate the output with the name the idx is mapping to 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccountIdx = {}
        for idx, account in enumerate(accounts):
            for i in range(1, len(account)):
                email = account[i]
                if email not in emailToAccountIdx:
                    emailToAccountIdx[email] = idx
                else:
                    uf.union(idx, emailToAccountIdx[email])

        # root idx mapping to emails
        res = []
        groups = defaultdict(list)
        for email, idx in emailToAccountIdx.items():
            rootIdx = uf.find(idx)
            groups[rootIdx].append(email)

        for rootIdx, emails in groups.items():
            name = accounts[rootIdx][0]
            res.append([name] + sorted(emails))

        return res


        