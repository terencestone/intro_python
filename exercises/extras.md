# Extras

## Strings and Lists
1. Convert this string `'145'` to an integer and print it.
2. Turn this list `['I', 'love', 'ruby']` into this list: `['I', 'love', 'python', '.']`. Hint: use `pop()` and `append()`.
3. Using list indexes (i.e. `some_list[0]`), turn this list `['I', 'love', 'python', '.']` into this string: `I love python.` Hint: use basic concatenation.
4. Split this string: `'admin.admin.com'` such that the output returns `['admin', 'admin', 'com']`.
5. Do the same as the above with this string: `'admin@admin.com'`.
6. Loop through this list `['Emphasize', 'every', 'single', 'word', 'with', 'separate', 'lines']` and print each word.
7. Construct this list `[0, 1, 2, 3, 4, 5]` with the python `range()` function. If you don't know what that is, google it.

## Loops
### The zoo
1. Set this list (`['lion', 'bear', 'koala', 'snake', 'monkey']`) equal to `zoo`.
2. Set the animal in the 1st position equal to a variable. Hint: use the list index to get the animal.
3. Add the string `'zebra'` to `zoo`. Hint: `zoo` should now be equal to `['lion', 'bear', 'koala', 'snake', 'monkey', 'zebra']`
4. Remove `'koala'` from `zoo`

### String to numbers
1. Split this string `"1-2-3-4-5-6-7-8"` into a list of all 8 numbers and set it to a variable `string_num_list`. Hint: Use the `split()` method.
2. Now that you have your list (should look like `['1', '2', '3'...etc.]`), create a new variable called `num_list` and set it equal to an empty list (`[]`).
3. Loop through `string_num_list` converting each item to an integer, and then adding it to `num_list`. Hint: Use a `for loop`, then inside of the loop, use the `int()` function and the `append()` method.
4. Now that you have filled `num_list` (should look like `[1, 2, 3...etc.]`), loop through `num_list` and print each number. Hint: Use the print() function inside the loop.
5. BONUS: Do the above with a list comprehension. Look it up if you don't know what it is. Hint: You will set the list comprehension equal to `num_list` instead of an empty list.
