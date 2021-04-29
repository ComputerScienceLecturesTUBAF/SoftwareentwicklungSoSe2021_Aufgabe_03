import random 

items = [
    'Variant_0.md',
    'Variant_1.md'
]

readmefilename = "README.md"

taskname = random.sample(items,  1)

with open(readmefilename, 'r') as readmefilehandle:
        readmecontent = readmefilehandle.read()

with open(taskname, 'r') as taskfilehandle:
        taskcontent = taskfilehandle.read()

newreadmecontent = readmecontent.split("## Aufgabenvariante")[0] + taskcontent

with open(readmefilename, 'w') as readmefilehandle:
        readmefilehandle.write(newreadmecontent)

print("Aus die Maus!")
