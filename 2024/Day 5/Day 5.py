from collections import defaultdict


def sort(orders, input):
    book = input[:]
    for p in range(len(book)):
        while not set(book[p + 1 :]).issubset(orders[book[p]]):
            book.append(book.pop(p))
    return book == input, book[len(book) // 2]


rules, p = [
    i.split("\n") for i in open("input.txt", "r", encoding="utf-8").read().split("\n\n")
]

books = [[int(j) for j in i.split(",")] for i in p if i != ""]

orders = defaultdict(set)
for rule in rules:
    bef, aft = [int(i) for i in rule.split("|")]
    orders[bef].add(aft)


checks = [sort(orders, book) for book in books]
part1 = sum([check[1] for check in checks if check[0]])
part2 = sum([check[1] for check in checks if not check[0]])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
