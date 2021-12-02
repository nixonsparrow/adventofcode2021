
if __name__ == '__main__':
    for day in range(3, 26):
        nr = day if len(str(day)) > 1 else f'0{day}'
        open(f'day{nr}_test.txt', 'w+')
        open(f'day{nr}_final.txt', 'w+')
