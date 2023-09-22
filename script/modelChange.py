# 输入文件路径
input_file_path = "../input/singleBlade-ModelChangeElemSets.txt"
# 输出文件路径
output_file_path = "../output/singleBlade-ModelChangeElemSets.txt"

count = 0

# 打开输入文件以读取
with open(input_file_path, 'r') as input_file:
    # 打开输出文件以写入
    with open(output_file_path, 'w') as output_file:
        # 逐行读取输入文件
        for line in input_file:
            # 检查行是否以*开头
            if line.startswith('*'):
                # 如果不以*开头，将行写入输出文件
                output_file.write(f"*Elset, elset=Set-{count}, instance=PART-1-1\n")
                count += 1
            else:
                output_file.write(line)
            
