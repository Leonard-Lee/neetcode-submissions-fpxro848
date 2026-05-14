class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create a map that maps 
        parents = {}
        ranks = {}
        emailToNameMap = {}

        for account in accounts:
            name = account[0]

            for i in range(1, len(account)):
                email = account[i]
                parents[email] = email
                ranks[email] = 0
                emailToNameMap[email] = name

        # return the root email
        def find(email) -> str:
            if parents[email] == email:
                return email

            parents[email] = find(parents[email])
            return parents[email]

        # return True/False means if it merges successfully or not
        def union(email1, email2) -> bool:
            p1, p2 = find(email1), find(email2)

            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p2] > ranks[p1]:
                parents[p1] = p2
            else:
                parents[p1] = p2
                ranks[p2] += 1
            
            return True

        # format the result
        for account in accounts:
            first = account[1]
            for i in range(2, len(account)):
                union(first, account[i])

        groups = defaultdict(list)
        for email in emailToNameMap.keys():
            root = find(email)
            groups[root].append(email)  

        res = []
        for root, emails in groups.items():
            name = emailToNameMap[root]
            res.append([name] + sorted(emails))

        return res



        