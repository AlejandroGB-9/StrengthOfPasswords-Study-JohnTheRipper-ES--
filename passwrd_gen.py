import random
import os
import hashlib

symbols = list("~!@#$%^&*()_+-=[]{;}'\"\":;,./<>?")

def modify_string(string):
    new_string = ""
    for i in range(0, len(string)):
        option = random.randint(1, 4)
        match option:
            case 1:
                new_string += string[i].upper()
            case 2:
                new_string += string[i].lower()
            case 3:
                new_string += str(random.randint(0, 9))
            case 4:
                new_string += random.choice(symbols)
            case default:
                print("Error")
    return new_string

def password_generator_lower(num, length):
    f = open("dataset1_" + str(num) + ".txt", "a")
    for i in range (0, 100):  
        rand_lst = [random.randint(97, 122) for i in range(0,length)] #ASCII values for a-z
        rand_str_lst = list(map(chr, rand_lst))
        rand_str = "".join(rand_str_lst)
        f.write(rand_str + "\n")
    f.close()
    return

def password_generator_upper(num, length):
    f = open("dataset2_" + str(num) + ".txt", "a")
    for i in range (0, 100):
        rand_lst = [random.randint(65, 90) for i in range(0,length)] #ASCII values for A-Z
        rand_str_lst = list(map(chr, rand_lst))
        rand_str = "".join(rand_str_lst)
        f.write(rand_str + "\n")
    f.close()
    return

def password_generator_numbers(num, length):
    f = open("dataset3_" + str(num) + ".txt", "a")
    for i in range (0, 100):
        rand_lst = [random.randint(48, 57) for i in range(0,length)] #ASCII values for 0-9
        rand_str_lst = list(map(chr, rand_lst))
        rand_str = "".join(rand_str_lst)
        f.write(rand_str + "\n")
    f.close()
    return

def password_generator_alphanum(num, length):
    f = open("dataset4_" + str(num) + ".txt", "a")
    round = 0
    while round < 100:
        count_symbs = 0
        count_nums = 0
        count_letters = 0
        rand_lst = [random.randint(33, 126) for i in range(0,length)] #ASCII values for all symbols
        for i in rand_lst:
            if i in range(33,48) or i in range(58,65) or i in range(91,97) or i in range(123,127):
                count_symbs += 1
            elif i in range(48,58):
                count_nums += 1
            elif i in range(65,91) or i in range(97,123):
                count_letters += 1
        if count_symbs > 0 and count_nums > 0 and count_letters > 0:
            rand_str_lst = list(map(chr, rand_lst))
            rand_str = "".join(rand_str_lst)
            f.write(rand_str + "\n")
            round += 1
    f.close()
    return

def password_generator_wordlist(fname, num, length):
    f = open("dataset5_" + str(num) + ".txt", "a")
    lines = open(fname).read().splitlines()
    iter = 0
    while iter < 100:
        word = random.choice(lines)
        if len(word) == length:
            strategy = random.randint(1, 3)
            match strategy:
                case 1:
                    f.write(word.lower() + "\n")
                case 2:
                    f.write(word.upper() + "\n")
                case 3:
                    word = modify_string(word)
                    f.write(word + "\n")
                case default:
                    print("Error")
            iter += 1
    f.close()
    return

def generate_wordlist(fname):
    cur_path = os.path. dirname(os.path.abspath(__file__))
    new_path = os.path.join(cur_path, fname)
    if not os.path.exists(new_path):
        print(f"El archivo '{fname}' no existe en la ubicación '{new_path}'")
        return
    with open(new_path, "r") as file:
        lines = file.read().splitlines()
    f = open("gen_wordlist.lst", "a")
    i = 0
    while i < 300:
        word = random.choice(lines)
        if len(word) <= 7 and len(word) >= 3:
            f.write(word + "\n")
            i += 1

    f.close()
    return

def generator_SHA256(fname, set, num):
    lines = open(fname).readlines()
    f = open("dataset" + str(set) + "_" + str(num) + "_SHA256" + ".txt", "a")
    for line in lines:
        line = line.strip()
        line = hashlib.sha256(line.encode()).hexdigest()
        f.write(line + "\n")
    
    f.close()
    return 

def generator_MD5(fname, set, num):
    lines = open(fname).readlines()
    f = open("dataset" + str(set) + "_" + str(num) + "_MD5" + ".txt", "a")
    for line in lines:
        line = line.strip()
        line = hashlib.md5(line.encode()).hexdigest()
        f.write(line + "\n")
    
    f.close()
    return 

def main():
    
    length = 2
    
    wlst_eng1 = "wordlists/WordList English Gutenberg.txt"
    wlst_eng2 = "wordlists/WordList English Unix.txt"
    wlst_eng3 = "wordlists/WordList_English rommmcek (4+ letter words only).txt"
    wlst_oth1 = "wordlists/Most-Popular-Letter-Passes.txt"
    wlst_oth2 = "wordlists/probable-v2-top1575.txt"
    wlst_oth3 = "wordlists/unkown-azul.txt"
    
    generate_wordlist(wlst_eng1) 
    generate_wordlist(wlst_eng2) 
    generate_wordlist(wlst_eng3) 
    generate_wordlist(wlst_oth1) 
    generate_wordlist(wlst_oth2)
    generate_wordlist(wlst_oth3)
    
    print("##########################################")
    print("WORDLIST GENERATED")
    print("##########################################")  
    
    for i in range(1,6):
        # password_generator_lower(i, length+i)
        # password_generator_upper(i, length+i)
        # password_generator_numbers(i, length+i)
        password_generator_alphanum(i, length+i)
        password_generator_wordlist("gen_wordlist.lst", i, length+i)
        
    print("##########################################")
    print("DATASETS GENERATED")
    print("##########################################")  
        
    for i in range(1,6):
        # generator_SHA256("dataset1_" + str(i) + ".txt", 1, i)
        # generator_SHA256("dataset2_" + str(i) + ".txt", 2, i)
        # generator_SHA256("dataset3_" + str(i) + ".txt", 3, i)
        generator_SHA256("dataset4_" + str(i) + ".txt", 4, i)
        generator_SHA256("dataset5_" + str(i) + ".txt", 5, i)
        
        # generator_MD5("dataset1_" + str(i) + ".txt", 1, i)
        # generator_MD5("dataset2_" + str(i) + ".txt", 2, i)
        # generator_MD5("dataset3_" + str(i) + ".txt", 3, i)
        generator_MD5("dataset4_" + str(i) + ".txt", 4, i)
        generator_MD5("dataset5_" + str(i) + ".txt", 5, i)
        
    print("##########################################")
    print("DATASETS HASHED")
    print("##########################################")  
        
if __name__ == "__main__":
    main()
    print("##########################################")
    print("DONE")
    print("##########################################")  
             