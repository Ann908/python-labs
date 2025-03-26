my_dict_status_problem = {'math': 'done', 'history': 'waiting', 'english': 'in process', 'germany': 'waiting'}
print(f"Original dictionary {my_dict_status_problem}")
def add_status(problem, status):
        my_dict_status_problem[problem] = status

add_status('math', 'in process')
add_status('spanish', 'done')
print(f"Add status {my_dict_status_problem}")

def del_status(problem):
    if problem in my_dict_status_problem:
        del my_dict_status_problem[problem]

del_status('spanish')
print(f"Delete status {my_dict_status_problem}")

def change_status(problem, new_status):
    if problem in my_dict_status_problem:
        my_dict_status_problem[problem] = new_status

change_status('english', 'done')
print(f"Change status {my_dict_status_problem}")

list_waiting = []
for item in my_dict_status_problem:
    if my_dict_status_problem[item] == 'waiting':
        list_waiting.append(item)

print(f"Name of problems have status 'waiting {list_waiting}'")
