from budget import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')


spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

# count categories frequencies
spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

# convert top5 into two lists 
categories, count = zip(*top5)

# fig as Figure top level container for graph
# ax as Axes containing figure elements
fig, ax = plt.subplots()

# bar charts with category counts
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

# display graph
plt.show()