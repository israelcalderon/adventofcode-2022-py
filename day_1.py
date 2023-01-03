def main() -> None:
    calories_by_elf = [0]

    with open('day_1_input') as calories_file:
        for line in calories_file:
            if line == '\n':
                calories_by_elf.append(0)
                continue
            calories_by_elf[-1] += int(line)

    calories_by_elf.sort()

    print(f'The elf with more calories is carrying: {calories_by_elf[-1]}')
    print(f'Top 3 calories sum: {sum(calories_by_elf[-3:])}')


if __name__ == '__main__':
    main()
