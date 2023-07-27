lines = [l.strip() for l in open("input.txt", "r", encoding="utf-8").readlines()]


class field:
    def __init__(self, line):
        self.field, ranges = line.split(": ")
        self.valid_values = set()
        self.possible_columns = []
        self.column = None
        rs = ranges.split(" or ")
        for r in rs:
            st, end = [int(i) for i in r.split("-")]
            self.valid_values |= set(range(st, end + 1))

    def __repr__(self):
        return self.field

    def is_valid(self, value):
        return value in self.valid_values

    def initialize_possible(self):
        self.possible_columns = list(range(len(fields)))

    def remove_column(self, col):
        if col in self.possible_columns:
            self.possible_columns.remove(col)
        if len(self.possible_columns) == 1:
            self.column = self.possible_columns[0]
            fields.remove_column(self.column)

    @property
    def solved(self):
        return self.column is not None


class fieldsClass(list):
    def __init__(self):
        self.valid = set()
        super().__init__()

    def append(self, f: field):
        self.valid |= f.valid_values
        super().append(f)
        for f in self:
            f.initialize_possible()

    def is_valid(self, value):
        return value in self.valid

    def remove_column(self, col):
        for f in self:
            f.remove_column(col)

    @property
    def columns_known(self):
        return all([s.solved for s in self])


class ticket:
    def __init__(self, line):
        self.fields = [int(i) for i in line.split(",")]

    def error_rate(self):
        return sum([f for f in self.fields if not fields.is_valid(f)])

    @property
    def valid(self):
        return not any([f for f in self.fields if not fields.is_valid(f)])


fields = fieldsClass()
tickets = []
section = "fields"

for line in lines:
    if not line:
        continue
    if "your ticket" in line:
        section = "your_ticket"
        continue
    if "nearby tickets" in line:
        section = "nearby"
        continue

    if section == "fields":
        fields.append(field(line))
    elif section == "your_ticket":
        your_ticket = ticket(line)
    elif section == "nearby":
        tickets.append(ticket(line))

# for f in fields:
#     f.initialize_possible()

error_rate = sum([t.error_rate() for t in tickets])

valid_tickets = [t for t in tickets if t.valid]

while not fields.columns_known:
    for v in valid_tickets:
        for num in range(len(v.fields)):
            value = v.fields[num]
            for f in fields:
                if num in f.possible_columns and not f.is_valid(value):
                    f.remove_column(num)

departure_fields = [f.column for f in fields if "departure" in f.field]
part2 = 1
for col in departure_fields:
    part2 *= your_ticket.fields[col]

print(f"Part 1: {error_rate}")
print(f"Part 2: {part2}")
