import json
# /////////////////////////////////
# This is name of file that will be processed
file_path = "output.json"
# /////////////////////////////////

# make list out of output.json file
def process_json_file():
    encodings_to_try = ['utf-8', 'iso-8859-1', 'windows-1252']
    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                file_content = file.read()
                file_content = file_content.strip()
                data = json.loads(file_content)
                print(f"Successfully loaded JSON data from {file_path} using {encoding} encoding")
                return data
        except UnicodeDecodeError:
            print(f"Couldn't decode with {encoding}, trying next encoding...")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")
            print("Hint: Make sure the file contains valid JSON. Each object should be separated by commas.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    
    print("Error: Unable to decode the file with any of the attempted encodings.")
    return None


if __name__ == "__main__":
    # Make list from file 'output.json'
    problem_list = process_json_file()

    # map to store the tags and number of problems
    problem_tags = {}

    # Count topics and no. of problems in the list
    total_problems = 0
    sum_of_types = 0
    for x in problem_list:
        for tag in x["tags"]:
            if tag in problem_tags:
                problem_tags[tag] += 1
            else:
                problem_tags[tag] = 1
            sum_of_types+=1
        total_problems+=1


    # make the dict to json format with indentation of 4
    json_str = json.dumps(problem_tags, indent=4)
    print(json_str)

    print(f"Total problems {total_problems}")
    print(f"Total types of problems {sum_of_types}")

