def  filter_ips(input_file_path, output_file_path, allowed_ips):
    try:
        result_ips = {}
        with open(input_file_path) as file:
            for line in file:
                file_splited = line.split()
                #print(file_splited)
                #print(file_splited[0])
                if file_splited[0] in allowed_ips:
                    if file_splited[0] in result_ips:
                        result_ips[file_splited[0]] += 1
                    else:
                        result_ips[file_splited[0]] = 1
        print(result_ips)

    except FileNotFoundError:
        print("Input file is not found")

    try:
        with open(output_file_path, 'w') as file2:
            for item, key in result_ips.items():
                file2.write(f"{item} - {key}\n")
    except IOError:
        print("Error writing to output file")


filter_ips("apache_logs.txt", "result_file.txt", allowed_ips = ["93.114.45.13", "83.149.9.216", "110.136.166.128"])

