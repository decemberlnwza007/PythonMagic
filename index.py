def draw_tree(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        leaves = '*' * (2 * i + 1)
        print(spaces + leaves)

    trunk_width = height // 3
    trunk_height = height // 3
    trunk_spaces = ' ' * (height - trunk_width // 2 - 1)
    for _ in range(trunk_height):
        print(trunk_spaces + '*' * trunk_width)

tree_height = 10
draw_tree(tree_height)

