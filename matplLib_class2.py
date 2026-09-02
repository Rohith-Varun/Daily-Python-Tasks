#Bar Graphs
import matplotlib.pyplot as p
years = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
admissions = [300, 600, 400, 600, 800, 200, 1500]

p.bar(years, admissions)
p.xlabel("years")
p.ylabel("admissions")
p.title("CODEGNAN YEAR WISE ADMISSIONS")
p.grid(True)
p.show()
