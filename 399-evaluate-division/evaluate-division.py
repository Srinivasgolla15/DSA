class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        graph = defaultdict(list)
        res = [-1.0]*len(queries)
        nodes = []
        for i in range(len(equations)):
            u,v = equations[i]
            if u not in nodes:
                nodes.append(u)
            if v not in nodes:
                nodes.append(v)
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        
        for i in range(len(queries)):
            u1,u2 = queries[i]
            if u1 not in nodes or u2 not in nodes:
                
                continue
            if u1 == u2:
                res[i] = 1.0
                continue
            
            queue = deque([])
            queue.append((u1,1.0))
            # ❌ set(u1): splits string into characters
            #    set("bc") -> {"b", "c"}
            # ✅ {u1}: keeps the variable as ONE node
            #    {"bc"}
            visited = {u1}
            while queue:
                start , product = queue.popleft()
                if start == u2:
                    res[i] = product
                    break
                for nei,wei in graph[start]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append(
                        (nei, product * wei)
                    )

        return res

        