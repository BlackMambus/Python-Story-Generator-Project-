import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

print(f"{random.choice(when)}, {random.choice(who)} named {random.choice(name)} from {random.choice(residence)} went to the {random.choice(went)} and {random.choice(happened)}.")
name = input("Enter your name: ")
setting = input("Choose a setting (forest, city, castle): ")
print(f"Once upon a time, {name} found themselves in a {setting}, where an adventure awaited...")

