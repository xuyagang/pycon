# subprocess 附加进程
# 提供了一种一致的方法创建和处理附加进程

# Popen类的构造函数根据参数建立新进程，使父进程可通过管道与之通信
# 很多需要开销的额外操作（如关闭文件描述符，确保管道关闭）都已内置，无需单独处理

# 运行外部命令
import subprocess

# simple commond
# 将shell设置为True会使subprocess创建一个中间shell进程
# 由这个进程运行命令
subprocess.call('echo $HOME',shell=True)

# 在windows 在子进程中使用echo，需要设置 shell =True，
# 因为 echo 不是单独的命令，而是window CMD 内置的命令