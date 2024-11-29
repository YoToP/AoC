footballers_and_nums = [("Fabregas", 4),
                        ("Beckham" ,10),
                        ("Yak", 9), 
                        ("DeJong", 13), 
                        ("DeJong", 8), 
                        ("Ronaldo", 7), 
                        ("Terry", 26), 
                        ("Van der Saar", 1), 
                        ("Yobo", 2)]

sorted_footballers_and_nums = sorted(footballers_and_nums, key=lambda index : index)
print("Original footballers and jersey numbers", footballers_and_nums) 
# Original footballers and jersey numbers [('Fabregas', 4), ('Beckham', 10), ('Yak', 9), ('Lampard', 8), ('Ronaldo', 7), ('Terry', 26), ('Van der Saar', 1), ('Yobo', 2)]


print("Sorted footballers by jersey numbers:", sorted_footballers_and_nums) 
# Sorted footballers by jersey numbers: [('Van der Saar', 1), ('Yobo', 2), ('Fabregas', 4), ('Ronaldo', 7), ('Lampard', 8), ('Yak', 9), ('Beckham', 10), ('Terry', 26)]