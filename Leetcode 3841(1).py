class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        stack = [(0, -1, 0, 0)] # u, p, d, state
        parent[0] = -1       
        # Standard recursive DFS is usually fine for depth if limit is raised, 
        # but let's use an optimized iterative post-order/pre-order traversal stack or standard DFS.
        import sys
        sys.setrecursionlimit(200000)
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            size = 1
            max_sub = 0
            heavy_v = -1
            for v in adj[u]:
                if v != p:
                    sub_size = dfs1(v, u, d + 1)
                    size += sub_size
                    if sub_size > max_sub:
                        max_sub = sub_size
                        heavy_v = v
            heavy[u] = heavy_v
            return size
        dfs1(0, -1, 0)
        # 2. Second DFS to assign positions for HLD
        cur_pos = 0
        stack = [0]
        # Using iterative stack for dfs2 to avoid recursion overhead
        head[0] = 0        
        # Iterative HLD position assignment
        # We can simulate dfs2 using a stack of (u, h)
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1           
            # Push light children first so heavy child is processed last (popped first)
            hv = heavy[u]
            for v in reversed(adj[u]):
                if v != parent[u]:
                    if v == hv:
                        stack.append((v, h))
                    else:
                        stack.append((v, v))
        # 3. Iterative Segment Tree setup (Power of 2 padding for speed)
        size = 1
        while size < n:
            size <<= 1         
        tree = [0] * (2 * size)        
        # Initialize leaf nodes
        chars = [1 << (ord(char) - 97) for char in s]
        for i in range(n):
            tree[size + pos[i]] = chars[i]           
        # Build tree iteratively
        for i in range(size - 1, 0, -1):
            tree[i] = tree[i << 1] ^ tree[(i << 1) | 1]
        def update(idx, val):
            i = size + pos[idx]
            tree[i] = val
            i >>= 1
            while i > 0:
                tree[i] = tree[i << 1] ^ tree[(i << 1) | 1]
                i >>= 1
        def query_range(l, r):
            res = 0
            l += size
            r += size + 1
            while l < r:
                if l & 1:
                    res ^= tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= tree[r]
                l >>= 1
                r >>= 1
            return res
        def get_path_xor(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query_range(pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_range(pos[u], pos[v])
            return res
        ans = []
        app = ans.append
        for q in queries:
            if q[0] == 'u':
                # fast parse for "update u c"
                _, u_str, c = q.split()
                u = int(u_str)
                update(u, 1 << (ord(c) - 97))
            else:
                # fast parse for "query u v"
                _, u_str, v_str = q.split()
                u = int(u_str)
                v = int(v_str)
                path_mask = get_path_xor(u, v)
                app((path_mask & (path_mask - 1)) == 0)
        return ans
