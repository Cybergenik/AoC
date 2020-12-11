import sys 

with open("inputs.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
inputs = [int(x.strip()) for x in content] 

print(inputs)
def day1(lines: list) -> int:
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            val = 2020 - (lines[i] + lines[j])
            if val in lines: 
                return lines[i]*lines[j]*lines[lines.index(val)]
    
print(day1(inputs))

