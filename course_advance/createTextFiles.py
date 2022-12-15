import json
from types import SimpleNamespace
import json
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
            return o.__dict__

f = open('course.json')
#data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
data = json.load(f)
data1 = json.dumps(data,ensure_ascii=False)
# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data1, object_hook=lambda d: SimpleNamespace(**d))
for task in x.lessons:
    task.textMarkup = "lesson1/{}.text".format(task.id)
    task.pitch = "lesson1/{}.pitch".format(task.id)
    task.sound = "lesson1/{}.mp3".format(task.id)
    task.video = "lesson1/{}.mp4".format(task.id)
    task.image = None
    f = open("lesson1/{}.text".format(task.id),'w')
    f.write(task.text)
courseJson = json.dumps(x.__dict__,ensure_ascii=False, cls=CustomEncoder,indent=2)
print(courseJson)
with open("Course.json", "w") as outfile:
    outfile.write(courseJson)
    
