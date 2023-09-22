import os

# 指定输出文件路径
output_dir = "..\output"
output_file = os.path.join(output_dir, "genPy.txt")

os.makedirs(output_dir, exist_ok=True)

# 读取命令行输入，将每行写入输出文件
while True:
    try:
        user_input = input()
        with open(output_file, "a") as file:
            file.write(f"file.write(f\"{user_input}\\n\")\n")
    except EOFError:
        break

print("输入已写入到文件:", output_file)
