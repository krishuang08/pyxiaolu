# 已经发布到PyPI，https://pypi.org/manage/projects/

# 导入库的方式：
from pyxiaolu import pyxiaolu

# pyxiaolu包括以下方法：
## login(username,password)
username:小陆同学用户名

password:小陆同学密码

### 返回值:

当不成功，返回布尔值False

当成功，返回字符串token，该token需要保存好

## execute(code,token)
code:要执行的代码，可以使用三个双引号来执行多行代码

token:login方法中返回的字符串token

### 返回值:

当不成功，返回布尔值False

当成功，返回这些代码的stdout
