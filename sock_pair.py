
id = [10,5,10,1,20,50,15,30]
# id2 = []
# pair = 0
# for index_1, item_1 in enumerate(id):
#     print(f"Level 1 => {index_1} + {item_1}")
#     for index_2, item_2 in id[1:]:
#         print(f"Level 2 => {index_2} + {item_2}")
#         if item_1 == item_2:
#             print(f"Matching combo => {item_1} + {item_2}")
#             id.pop(index_1)
#             id.pop(index_2)
#             pair += 1
            
# rather look at putting it in the dict:
item_counter = {}


for item in id:
    if item in item_counter:
        item_counter[item] += 1
        
    else:
        item_counter[item] = 1
        
# print(item_counter)


pair = 0
for key, value in item_counter.items():
    if value % 2 == 0:
        print(key)
        pair += 1

print(pair)