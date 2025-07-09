import json
from gendiff import constans as cons


def format_json(diff):
    def build_tree(node):
        result = {
            'key': node['key'],
            'status': node['status']
        }

        if node['status'] == cons.NESTED:
            result['children'] = [build_tree(child) for child in node['children']]
        elif node['status'] == cons.CHANGED:
            result['old_value'] = node['old_value']
            result['new_value'] = node['new_value']
        else:
            if 'value' in node:
                result['value'] = node['value']
        return result

    return json.dumps([build_tree(item) for item in diff], indent=4)
