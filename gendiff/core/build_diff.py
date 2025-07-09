from gendiff import constans as cons


def build_diff(dict1, dict2):
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diff = []
    for key in keys:
        if key not in dict1:
            diff.append({'key': key, 'status': cons.ADDED, 'value': dict2[key]})
        elif key not in dict2:
            diff.append({'key': key, 'status': cons.REMOVED, 'value': dict1[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append({'key': key, 'status': cons.NESTED,
                         'children': build_diff(dict1[key], dict2[key])})
        elif dict1[key] == dict2[key]:
            diff.append({'key': key, 'status': cons.UNCHANGED, 'value': dict1[key]})
        else:
            diff.append({'key': key, 'status': cons.CHANGED,
                         'old_value': dict1[key], 'new_value': dict2[key]})
    return diff
