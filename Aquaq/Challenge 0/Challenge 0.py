keypad = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}

lines = [
    [int(i) for i in l.strip().split(" ")]
    for l in open("input.txt", "r", encoding="utf-8").readlines()
]

output = ""
for line in lines:
    output += keypad[line[0]][line[1] - 1]

print(f"Output: {output}")
