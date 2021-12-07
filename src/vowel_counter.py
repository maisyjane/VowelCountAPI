def count_vowels(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowel_counter = 0
    if(string != ""):
        for s in string:
            for vowel in vowel_list:
                if s == vowel:
                    vowel_counter+=1
        return vowel_counter    
    else:
        return 0

   


