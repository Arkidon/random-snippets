from difflib import SequenceMatcher
from operator import itemgetter
strint_to_compare = "test"
product_list = []

for i in range(0, 1):
    query = input()
    product_list.append({'name': query, 'value': SequenceMatcher(None, query.lower(), strint_to_compare.lower()).ratio()})

product_list.sort(key=itemgetter('value'), reverse=True)

print(product_list)
