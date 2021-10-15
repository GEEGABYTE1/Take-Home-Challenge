def dfs(root_node, path=(), layers_lst=[], root=None):
        if root == None:
            root = root_node
        path = path + (root_node,)
        current_level_lst=[]
        
        for i in path:
            if not i.value in current_level_lst:
                current_level_lst.append(i.value)


        for node in root_node.children:
            new_path = dfs(node, path, layers_lst, root)
        
            if not new_path == None:
                return new_path 
        
        layers_lst.append(current_level_lst)

        
        last_lst = layers_lst[-1]
        if root.value == last_lst[-1]:
            return layers_lst 
        else:
            return None
