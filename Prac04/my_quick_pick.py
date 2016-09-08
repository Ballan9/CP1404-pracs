from random import randint


def main():
    pick_num = int(input("How many quick picks?"))
    pick_gen(pick_num)


def pick_gen(pick_num):
    for i in range(pick_num):
        num_list = []
        while len(num_list) != 6:
            random_num = randint(1, 45)
            if random_num not in num_list:
                num_list.append(random_num)
        print(*sorted(num_list), sep=' \t')

main()
