import parse
parse.MY_FILE
type(parse.MY_FILE)

copy_my_file = parse.MY_FILE
copy_my_file
type(copy_my_file)

#var for where it is saved in the computer's memory. so not a copy. referencing.
id(copy_my_file)
id(parse.MY_FILE)

#testing
new_data = parse.parse(copy_my_file, ",")


type(new_data)

type(new_data[0])

type(new_data[0]["DayOfWeek"])


new_data[0].keys()
new_data[0].values()
len(new_data)

count = 0
for dict_item in new_data:
	count = count + 1
    print dict_item["Descript"], count

help(parse.parse)