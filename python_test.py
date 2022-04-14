import json
import random

def refined_main()->list:
    with open('data.txt', 'r') as file:
        parse_commands=[]
        copy_commands=[]
        functional_commands=[]
        random_commands=[]
        bad_commands=[]
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)
        for row in data:
            if('function' in row):
                if(row['function']=='parse'):
                    parse_commands.append(row.copy())
                    new_row = row.copy()
                    new_row['_list'] = 'parse'
                    new_row['_counter'] = len(parse_commands)
                    functional_commands.append(new_row)

                elif(row['function']=='copy'):
                    copy_commands.append(row.copy())
                    new_row = row.copy()
                    new_row['_list'] = 'copy'
                    new_row['_counter'] = len(parse_commands)
                    functional_commands.append(new_row)
                elif(row['function']=='bad value'):
                    bad_commands.append(row.copy())
            else:
                bad_commands.append(row.copy())
    return [parse_commands, copy_commands, functional_commands, random_commands, bad_commands]

# def main() -> (dict, dict, dict, dict,dict):
#     # NOTE: Get all the parse commands
#     with open('data.txt', 'r') as file:
#         data = json.loads(file.read())
#     parse_commands = []
#     for row in data:
#         if 'function' in row and row['function'] == 'parse':
#             parse_commands.append(row.copy())
#     print(f"parse_commands: {parse_commands}")

#     # NOTE: Get all the copy commands
#     with open('data.txt', 'r') as file:
#         data = json.loads(file.read())
#     copy_commands = []
#     for row in data:
#         if 'function' in row and row['function'] == 'copy':
#             copy_commands.append(row.copy())
#     print(f"copy_commands: {copy_commands}")

#     # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
#     functional_commands = []
#     counter = 0
#     for row in parse_commands:
#         counter += 1
#         new_row = row.copy()
#         new_row['_list'] = 'parse'
#         new_row['_counter'] = counter
#         functional_commands.append(new_row)
#     counter = 0
#     for row in copy_commands:
#         counter += 1
#         new_row = row.copy()
#         new_row['_list'] = 'copy'
#         new_row['_counter'] = counter
#         functional_commands.append(new_row)
    
#     print(f"functional_commands: {functional_commands}")

#     # NOTE: Get random sampling of data
#     random_commands = []
#     with open('data.txt', 'r') as file:
#         data = json.loads(file.read())
#         random_commands = random.sample(data, 2)
#     print(f"random_commands: {random_commands}")

#     # NOTE: Write the methodology to catch bad_commands
#     bad_commands = list()
#     bad_commands = [None]*3
#     return parse_commands, copy_commands, functional_commands, random_commands, bad_commands


# if __name__ == '__main__':
#     parse_commands, copy_commands, functional_commands, random_commands, bad_commands = refined_main()

#     assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
#     assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
#     assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
#     assert len(random_commands) == 2
#     assert len(bad_commands) == 3
