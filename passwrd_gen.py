import random
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

def generate_wordlist(fname):
    random_list = []
    lines = open(fname).read().splitlines()
    for i in range(0, 100):
        random_list.append(random.choice(lines))
    return random_list

def password_generator_sect1_2(fname, num):
    random_list = []
    lines = open(fname).readlines()
    for line in lines:
        if len(line) <= 7 and len(line) >= 3 and len(random_list) < 100:
            random_list.append(line.strip().lower())
     
    f = open("dataset1_2-" + str(num) + ".txt", "a")
    for i in random_list:
        f.write(i + "\n")
    f.close()
    return 
    
def password_generator_sect2_2(fname, num):
    random_list = []
    lines = open(fname).readlines()
    for line in lines:
        if len(line) <= 7 and len(line) >= 3 and len(random_list) < 100:
            random_list.append(line.strip().upper())
     
    f = open("dataset2_2-" + str(num) + ".txt", "a")
    for i in random_list:
        f.write(i + "\n")
    f.close()
    return 

def password_generator_sect3_2(num):
    f = open("dataset3_2-" + str(num) + ".txt", "a")
    for i in range(0, 100):
        f.write(str(random.randint(100, 9999999)) + "\n")
    f.close()
    return

def password_generator_sect4_2(fname, num):
    random_list = []
    lines = open(fname).readlines()
    for line in lines:
        if len(line) <= 7 and len(line) >= 3 and len(random_list) < 100:
            line = line.strip()
            line = modify_string(line)
            random_list.append(line)
    
    f = open("dataset4_2-" + str(num) + ".txt", "a")
    for i in random_list:
        f.write(i + "\n")
    f.close()
    return

def hash_passwords_1(fname, num):
    random_list = []
    lines = open(fname).readlines()
    for line in lines:
        line = line.strip()
        line = hashlib.sha256(line.encode('UTF-8')).hexdigest()
        random_list.append(line)
    
    f = open("dataset5-" + str(num) + ".txt", "a")
    for i in random_list:
        f.write(i + "\n")
    f.close()
    return

def hash_passwords_2(fname, num):
    random_list = []
    lines = open(fname).readlines()
    for line in lines:
        line = line.strip()
        line = hashlib.sha512(line.encode('UTF-8')).hexdigest()
        random_list.append(line)
    
    f = open("dataset5-" + str(num) + ".txt", "a")
    for i in random_list:
        f.write(i + "\n")
    f.close()
    return

def hash_passwords_3(fname, num):
    random_list = []
    lines = open(fname).readlines()
    for line in lines:
        line = line.strip()
        line = md5_crypt.hash(line)
        random_list.append(line)
    
    f = open("dataset5-" + str(num) + ".txt", "a")
    for i in random_list:
        f.write(i + "\n")
    f.close()
    return          