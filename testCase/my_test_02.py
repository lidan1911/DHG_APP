import yaml
import os

# yaml_str = "ymal的字符串"
# y = yaml.load(yaml_str)
# print(y)


cwd = os.getcwd()  # 当前文件所在文件夹地址
root = os.path.dirname(cwd)  # 父级目录
yaml_path = os.path.join(root, "common", "config.ymal")
with open(yaml_path, 'rb') as f:
    cont = f.read()
cf = yaml.load(cont)
print(cf)
print(type(cf))
f.close()
