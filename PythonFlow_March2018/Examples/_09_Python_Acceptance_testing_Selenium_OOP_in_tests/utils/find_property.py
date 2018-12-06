def find_property(source, path):
    if not isinstance(source, dict) or not len(path):
        return source
    path = path.split('.') if isinstance(path, str) else path
    return find_property(source.get(path.pop(0), None), path)


if __name__ == "__main__":
    data = {
        (1, 2): {
            'test': {
                1: 3
            }
        },
        'test3': {
            'test4': 5
        }
    }
    print(find_property(data, 'test3.test4'))
    print(find_property(data, [(1, 2), 'test', 1]))
