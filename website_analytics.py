# Tasks:
# Unique Visitors Across All Days
# Find the total number of unique visitors who visited on any of the three days.

# Returning Visitors on Tuesday
# Identify users who visited on both Monday and Tuesday.

# New Visitors Each Day
# Determine which users visited for the first time each day (i.e., not seen on previous days).

# Loyal Visitors
# Find users who visited the site on all three days.

# Daily Visitor Overlap Analysis
# Compare and print overlaps between each pair of days (e.g., Monday-Tuesday, Tuesday-Wednesday, etc.)


monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}

unique_visitors = monday_visitors | tuesday_visitors | wednesday_visitors
print(unique_visitors)

returning_visitors = monday_visitors & tuesday_visitors
print(returning_visitors)

monday_new_visitors = monday_visitors
tuesday_new_visitors = tuesday_visitors - monday_visitors
wednesday_new_visitors = wednesday_visitors - (monday_visitors | tuesday_visitors)

print()

print(monday_new_visitors)
print(tuesday_new_visitors)
print(wednesday_new_visitors)

# loyal_visitors = (monday_visitors & tuesday_visitors) & wednesday_visitors
# print(loyal_visitors)

loyal_visitors = monday_visitors & tuesday_visitors & wednesday_visitors
if loyal_visitors:
    print("Loyal visitors", loyal_visitors)
else:
    print("No loyal visitors found")

print(monday_visitors & tuesday_visitors)
print(tuesday_visitors & wednesday_visitors)
