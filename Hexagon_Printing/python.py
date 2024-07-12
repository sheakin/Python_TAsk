# Case 1: 4 rows, 7 columns
r1 = 4
c1 = 7

print(f"For {r1} rows and {c1} columns:")
for j in range(c1 - (c1 - r1)):
    print(" ___    ", end="")
print()

for i in range(r1):
    for j in range(c1 - (c1 - r1)):
        print("/   \___", end="")
    print()

    for j in range(c1 - (c1 - r1)):
        print("\___/   ", end="")
    print()

print()

# Case 2: 3 rows, 5 columns
r2 = 3
c2 = 5

print(f"For {r2} rows and {c2} columns:")
for j in range(c2 - (c2 - r2)):
    print(" ___    ", end="")
print()

for i in range(r2):
    for j in range(c2 - (c2 - r2)):
        print("/   \___", end="")
    print()

    for j in range(c2 - (c2 - r2)):
        print("\___/   ", end="")
    print()