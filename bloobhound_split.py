import json

file_name = "20210312152708_computers.json"
type = "computers"
object_limit = 10000

print(f"[*] loading {file_name}")
data = json.loads(open(file_name,'r').read().encode().decode('utf-8-sig'))
total_objects = data['meta']['count']

object_count = 0
file_count = 0

while object_count < total_objects:
    a = {}
    a[type] = data[type][object_count:][:object_limit]
    object_count += len(a[type])

    a['meta'] = data['meta']
    a['meta']['count'] = object_count

    f_split = file_name.split(".")
    file_name_out = f"{f_split[0]}_{file_count}.{f_split[1]}"

    print(f"[*] writing {file_name_out} - {object_count} of {total_objects}")
    f_out = open(file_name_out, "w")
    json.dump(a, f_out)
    f_out.close()
    file_count += 1