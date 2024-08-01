import main
problem_set = main.process_json_file()

# Modify these list to find your required problems range
find_on_tags = ["bitmasks"]
find_on_rating = ["800"]


problems_found = 0
problems = []
for x in problem_set:
    for tag in find_on_tags:
        if tag in x["tags"]:
            for rating in find_on_rating:
                if rating == x['problem_rating']:
                    problems.append(x["url"])
                    print(x['url'])
                    problems_found+=1

print(f"Total problems found {problems_found}")
