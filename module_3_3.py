def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[123])

values_list = [7, "строка", [196]]
values_dict = {"a": 13, "b": "STR", "c": [396]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7, "ctr"]
print_params(*values_list_2, 42)
