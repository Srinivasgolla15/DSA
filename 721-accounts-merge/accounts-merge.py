class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = defaultdict(list)
        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            first = acc[1]

            graph[first]
            email_to_name[first] = name

            for mail in acc[2:]:
                email_to_name[mail] = name

                graph[first].append(mail)
                graph[mail].append(first)

        res = []
        visited = set()

        for email in graph:

            if email in visited:
                continue

            queue = deque([email])
            visited.add(email)

            emails = []

            while queue:
                mail = queue.popleft()
                emails.append(mail)

                for nei in graph[mail]:
                    if nei in visited:
                        continue

                    visited.add(nei)
                    queue.append(nei)

            emails.sort()

            res.append(
                [email_to_name[email]] + emails
            )

        return res