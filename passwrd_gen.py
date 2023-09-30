import random
import os
import hashlib
from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt

symbols = list("~!@#$%^&*()_+-=[]{;}':;,./<>?")

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

def password_generator_sect1_1(num):
    f = open("dataset1_1-" + str(num) + ".txt", "a")
    for i in range (0, 100):
        length = random.randint(3, 7)   
        rand_lst = [random.randint(97, 122) for i in range(0,length)] #ASCII values for a-z
        rand_str_lst = list(map(chr, rand_lst))
        rand_str = "".join(rand_str_lst)
        f.write(rand_str + "\n")
    f.close()
    return

def password_generator_sect2_1(num):
    f = open("dataset2_1-" + str(num) + ".txt", "a")
    for i in range (0, 100):
        length = random.randint(3, 7)   
        rand_lst = [random.randint(65, 90) for i in range(0,length)] #ASCII values for A-Z
        rand_str_lst = list(map(chr, rand_lst))
        rand_str = "".join(rand_str_lst)
        f.write(rand_str + "\n")
    f.close()
    return

def password_generator_sect3_1(num):
    f = open("dataset3_1-" + str(num) + ".txt", "a")
    for i in range (0, 100):
        length = random.randint(3, 7)   
        rand_lst = [random.randint(48, 57) for i in range(0,length)] #ASCII values for 0-9
        rand_str_lst = list(map(chr, rand_lst))
        rand_str = "".join(rand_str_lst)
        f.write(rand_str + "\n")
    f.close()
    return

def password_generator_sect4_1(num):
    f = open("dataset4_1-" + str(num) + ".txt", "a")
    for i in range (0, 100):
        length = random.randint(3, 7)   
        rand_lst = [random.randint(33, 126) for i in range(0,length)] #ASCII values for all symbols
        rand_str_lst = list(map(chr, rand_lst))
        rand_str = "".join(rand_str_lst)
        f.write(rand_str + "\n")
    f.close()
    return

# def generate_wordlist(fname):
#     random_list = []
#     lines = open(fname).read().splitlines()
#     for i in range(0, 100):
#         random_list.append(random.choice(lines))
#     return random_list

def generate_wordlist(fname, num):
    cur_path = os.path. dirname(os.path.abspath(__file__))
    new_path = os.path.join(cur_path, fname)
    if not os.path.exists(new_path):
        print(f"El archivo '{fname}' no existe en la ubicación '{new_path}'")
        return
    with open(new_path, "r") as file:
        lines = file.read().splitlines()
    f = open("worldlist" + str(num) + ".txt", "a")
    i = 0
    while i < 100:
        word = random.choice(lines)
        if len(word) <= 7 and len(word) >= 3:
            f.write(word + "\n")
            i += 1

    f.close()
    return

def password_generator_sect1_2(fname, num):
    lines = open(fname).readlines()
    f = open("dataset1_2-" + str(num) + ".txt", "a")
    count = 0
    for line in lines:
        if len(line) <= 7 and len(line) >= 3 and count < 100:
            f.write(line.strip().lower() + "\n")
        count += 1;
        
    f.close()
    return 
    
def password_generator_sect2_2(fname, num):
    lines = open(fname).readlines()
    f = open("dataset2_2-" + str(num) + ".txt", "a")
    count = 0
    for line in lines:
        if len(line) <= 7 and len(line) >= 3 and count < 100:
            f.write(line.strip().upper() + "\n")
        count += 1; 
    
    f.close()
    return 

def password_generator_sect3_2(num):
    f = open("dataset3_2-" + str(num) + ".txt", "a")
    for i in range(0, 100):
        f.write(str(random.randint(100, 9999999)) + "\n")
    f.close()
    return

def password_generator_sect4_2(fname, num):
    lines = open(fname).readlines()
    f = open("dataset4_2-" + str(num) + ".txt", "a")
    count = 0
    for line in lines:
        if len(line) <= 7 and len(line) >= 3 and count < 100:
            line = line.strip()
            line = modify_string(line)
            f.write(line + "\n")
        count += 1
        
    f.close()
    return

def hash_passwords_1(fname, set, num):
    lines = open(fname).readlines()
    f = open("hash1_" + str(set) + "-" + str(num) + ".txt", "a")
    for line in lines:
        line = line.strip()
        line = hashlib.sha256(line.encode('UTF-8')).hexdigest()
        f.write(line + "\n")
    
    f.close()
    return 

def hash_passwords_2(fname, set, num):
    lines = open(fname).readlines()
    f = open("hash2_" + str(set) + "-" + str(num) + ".txt", "a")
    for line in lines:
        line = line.strip()
        line = hashlib.sha512(line.encode('UTF-8')).hexdigest()
        f.write(line + "\n")
    
    f.close()
    return 

def hash_passwords_3(fname, set, num):
    lines = open(fname).readlines()
    f = open("hash3_" + str(set) + "-" + str(num) + ".txt", "a")
    for line in lines:
        line = line.strip()
        line = md5_crypt.hash(line)
        f.write(line + "\n")
    
    f.close()
    return 

def main():
    
    wlst_eng1 = "wordlists/WordList English Gutenberg.txt"
    wlst_eng2 = "wordlists/WordList English Unix.txt"
    wlst_eng3 = "wordlists/WordList_English rommmcek (4+ letter words only).txt"
    wlst_esp1 = "wordlists/Wordlist Spanish.txt"
    wlst_esp2 = "wordlists/WordList_SpanishAbc rommmcek.txt"
    
    # for i in range(1,6): #Works
    #     password_generator_sect1_1(i)
    #     password_generator_sect2_1(i)
    #     password_generator_sect3_1(i)
    #     password_generator_sect4_1(i)
    
    for i in range(1,6): 
        generate_wordlist(wlst_eng1, i) 
        generate_wordlist(wlst_eng2, i) 
        generate_wordlist(wlst_eng3, i) 
        generate_wordlist(wlst_esp1, i) 
        generate_wordlist(wlst_esp2, i)  
    
    for i in range(1,6):
        password_generator_sect1_2("worldlist" + str(i) + ".txt", i)
        password_generator_sect2_2("worldlist" + str(i) + ".txt", i)
        password_generator_sect3_2(i)
        password_generator_sect4_2("worldlist" + str(i) + ".txt", i)
        
    for i in range(1,6):
        hash_passwords_1("dataset1_2-" + str(i) + ".txt", 1, i)
        hash_passwords_1("dataset2_2-" + str(i) + ".txt", 2, i)
        hash_passwords_1("dataset3_2-" + str(i) + ".txt", 3, i)
        hash_passwords_1("dataset4_2-" + str(i) + ".txt", 4, i)
        hash_passwords_2("dataset1_2-" + str(i) + ".txt", 1, i)
        hash_passwords_2("dataset2_2-" + str(i) + ".txt", 2, i)
        hash_passwords_2("dataset3_2-" + str(i) + ".txt", 3, i)
        hash_passwords_2("dataset4_2-" + str(i) + ".txt", 4, i)
        hash_passwords_3("dataset1_2-" + str(i) + ".txt", 1, i)
        hash_passwords_3("dataset2_2-" + str(i) + ".txt", 2, i)
        hash_passwords_3("dataset3_2-" + str(i) + ".txt", 3, i)
        hash_passwords_3("dataset4_2-" + str(i) + ".txt", 4, i)
        
if __name__ == "__main__":
    main()
    print("Done")
             