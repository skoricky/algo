from collections import deque


class Node:
    def __init__(self, value=None, count=None, left=None, right=None):
        self.value = value
        self.count = count
        self.left = left
        self.right = right


class Point:
    def __init__(self, value, count):
        self.value = value
        self.count = count


def get_point_dict(str_):
    values = []
    points = []
    for item in str_:
        if item not in values:
            values.append(item)
            points.append(Point(item, str_.count(item)))
    return sorted(points, key=lambda x: x.count)


def create_haff_tree(points):
    if len(points) == 1:
        return points

    haff = deque(points)

    left = haff.popleft()
    right = haff.popleft()

    node = Node(count=(left.count + right.count), left=left, right=right)

    if len(haff) == 0:
        haff.append(node)
    else:
        idx = None
        for item in haff:
            if item.count == node.count:
                idx = haff.index(item)
                break

        if idx is not None:
            haff.insert(idx, node)
        else:
            haff.append(node)

    return create_haff_tree(haff)


def get_haff_code(tree, dict_values, path=''):
    if tree.value is not None:
        dict_values.update({tree.value: path})
    else:
        if tree.left is not None:
            get_haff_code(tree.left, dict_values, f'{path}0')
        if tree.right is not None:
            get_haff_code(tree.right, dict_values, f'{path}1')
    return dict_values


dict_ = get_point_dict('beep boop been!')

print(get_haff_code(create_haff_tree(dict_)[0], {}))