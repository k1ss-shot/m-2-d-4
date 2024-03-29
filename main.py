# """
# 1) Задача
# Посчитать количество одинаковых элементов в списке
# Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое число.
# Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается 
# три раза, число 3 - два раза, числа 2 и 4 - по одному разу.
# """

# class MyList:

#     def __init__(self, num_list) -> None:
#         self.num_list = num_list
    
#     def get_num_rep_count(self):
#         result = {}

#         for num in self.num_list:
#             if num in result:
#                 result[num] += 1
#             else:
#                 result[num] = 1

        
#         for k, v in result.items():
#             print(f'Число {k} встречается {v}')

#     def __str__(self) -> str:
#         return f'Объект список: {self.num_list}'

# my_list = MyList([1, 1, 3, 2, 1, 3, 4])
# my_list.get_num_rep_count()
# print(my_list)


# class Star:
#     def __init__(self,text) -> None:
#         self.text = text
        
#     def replace_space_to_star(self):
#         result = ''
#         for t in self.text.strip().split():
#             result += result
#             result += '*'
            
#         print(result[:-1])
        
# star = Star('     Hello  World! ')
# star.replace_space_to_star()


# import os 
 
 
# path = r'C:\Users\kairo\OneDrive\Рабочий стол'
# result = []
# for name in os.listdir(path):
#     if os.path.isfile(os.path.join(path,name)):
#         if name.split('.')[-1] in ('pdf', 'txt', 'epub'):
#             print(f'{name} - расширение {name.split('.')[-1]}')
            
            
# class Path:
#     def __init__(self,path):
#         self.path = path
        
#     def print_files_ext(self):
#         for name in os.listdir(self.path):
#             if os.path.isfile(os.path.join(self.path,name)):
#                 if name.split('.')[-1] in ('pdf', 'txt', 'epub'):
#                     print(f'{name.split('.')[0]} - расширение {name.split('.')[-1]}')

# ath = Path(r'C:\Users\kairo\OneDrive\Рабочий стол')
# ath.print_files_ext()



# '35732'

# number = 35732
# # str.str_number = number

# result = 0
# for n in str(number):
#     result += int(n)
    
# class Number:
#     def __init__(self, number):
#         self.number = number
        
#     def get_num_sum(self):
#         result = 0
#         for n in str(self.number):
#             result += int(n)
            
#         return result
    
# number = Number(35732)
# print(number.get_num_sum())