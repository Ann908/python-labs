import matplotlib.pyplot as plt

code_dict = {}
def analyze_log_file(log_file_path):
    try:
        with open(log_file_path) as file:
            for line in file:
                #print(line)
                res_split = line.split()
                #print(res_split)
                #print(res_split[8])
                if res_split[8] in code_dict:
                    code_dict[res_split[8]] += 1 #Writing in dictionary
                else:
                    code_dict[res_split[8]] = 1

    except FileNotFoundError:
        print("File is not found")
    except IOError:
        print("Error reading file")

    return code_dict

res = analyze_log_file("apache_logs.txt")
print(res)

list_code = list(code_dict.keys())
list_values = list(code_dict.values())

plt.plot(list_code, list_values)
plt.suptitle('Change in quantity according to code')
plt.ylabel('Number of code')
plt.xlabel('Code')
plt.show()

