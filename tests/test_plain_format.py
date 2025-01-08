from gendiff.formatters.format_plain import format_plain


def test_format_plain():
    diff = {
        'common': {
            'status': 'nested',
            'children': {
                'follow': {'status': 'added', 'value': False},
                'setting2': {'status': 'removed'},
                'setting3': {
                    'status': 'changed',
                    'old_value': True,
                    'new_value': None,
                },
                'setting4': {'status': 'added', 'value': 'blah blah'},
            },
        },
    }
    expected = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to null\n"
        "Property 'common.setting4' was added with value: 'blah blah'"
    )
    result = format_plain(diff)
    assert result == expected

