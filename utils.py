from graphql_relay.node.node import from_global_id


def input_to_dictionary(input):
    """Конвертируем Graphene input в словарь"""
    dictionary = {}
    for key in input:
        # Конвертируем GraphQL global id в database id
        if key[-2:] == 'id' and input[key] != 'unknown':
            input[key] = from_global_id(input[key])[1]
        dictionary[key] = input[key]
    return dictionary

