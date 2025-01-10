import json


def format_json(diff):
    def process_node(node):
        if node.get('status') == 'nested':
            children = {child['key']: process_node(child)
                        for child in node.get('children', [])}
            return {
                "status": "nested",
                "children": children
            }
        else:
            return {key: value for key, value in node.items() if key != 'key'}
    result = {item['key']: process_node(item) for item in diff}
    return json.dumps(result, indent=4)
