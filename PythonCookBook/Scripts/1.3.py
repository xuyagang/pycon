from collections import deque
# deque有一个maxlen参数，当append的时候，如果超过，那么最前面的就被挤出队列
def search(lines, pattern, history=5):
    # 限制队列长度
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == "__main__":
    with open(r'D:/project/pycon/PythonCookBook/Scripts/1.3.txt',encoding="utf-8") as f:
        for line, prevlines in search(f, "Python", 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print("-" * 20)