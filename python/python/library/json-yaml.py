"""Example for json and yaml prase."""

#!/usr/bin/env python3

import json

import yaml

# a = {"name": "John", "age": 30, "city": "New York"}
# b = json.dumps(a)
# print(b)

# c = json.loads(b)
# print(c)

users = ["zhangsan", "lisi", "wangwu"]

users_dumps = json.dumps(users)
print(users_dumps)
print(isinstance(users_dumps, str))


users_loads = json.loads(users_dumps)
print(users_loads)
print(isinstance(users_loads, list))

### yaml

info = """
name: tangx
age: 20
address:
  contry: China
  city: Beijing
"""

cfg = yaml.safe_load(info)
print(cfg)

cfg_dumps = yaml.safe_dump(cfg)
print(cfg_dumps)


cfg2 = yaml.load(info, Loader=yaml.SafeLoader)
cfg2_dumps = yaml.dump(cfg2, Dumper=yaml.SafeDumper)
