from tree import TreeNode


def dfs(root_node, goal, path=()):
    path = path + (root_node,)
    if root_node.value == goal:
        return path 
    else:
        for child in root_node.children:
            new_path = dfs(child, goal, path)

            if new_path:
                return new_path 
    
    return None

