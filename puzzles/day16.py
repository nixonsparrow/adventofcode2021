from .methods import txt_opener


def get_bin(char):
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    if char in letters:
        char = letters.index(char) + 10
    return format(int(char), 'b').zfill(4)


def translate_into_binary(sequence):
    return ''.join([get_bin(char) for char in sequence])


def get_version(binary_code):
    return int(binary_code[0:3], 2)


def get_id(binary_code):
    return int(binary_code[3:6], 2)


def get_length_type_id(binary_code):
    if get_id(binary_code) == 4:
        raise AttributeError
    return int(binary_code[6])


def read_literal_values(value):
    end = True if value[0] == '0' else False
    return value[1:], end


def compute(sequence, ver=0):
    if not ver:
        ver = get_version(sequence)
    p_id = get_id(sequence)

    print('ID:', p_id, 'VER:', ver)
    if p_id == 4:
        sequence = sequence[6:]
        sub_packets = []
        while True:
            sub_packet, end = read_literal_values(sequence[:5])
            sub_packets.append(sub_packet)
            sequence = sequence[5:]
            if end: break

    else:
        length_type_id = get_length_type_id(sequence)
        if length_type_id == 0:
            length_of_sub_packets = int(sequence[7:22], 2)
            ver = compute(sequence[22:22 + length_of_sub_packets], ver)
            sequence = sequence[22 + length_of_sub_packets:]

        elif length_type_id == 1:
            number_of_sub_packets = int(sequence[7:18], 2)
            print(int(sequence[7:18], 2), sequence[7:18], len(sequence), 'VER', ver)
            print('nr packets', number_of_sub_packets, 'VER', ver)
            sequence = sequence[18:]
            sub_packets = [sequence[i:i + 11] for i in range(0, number_of_sub_packets * 11, 11)]
            ver += sum([int(sub[:3], 2) for sub in sub_packets])
            print(sequence, len(sequence), 'VER', ver)
            sequence = sequence[number_of_sub_packets * 11:]
            print(sequence, len(sequence), 'VER', ver)

    if len(sequence) >= 11:
        ver += compute(sequence, ver)

    return ver


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    sequence = translate_into_binary(final_input)

    versions = 0
    print(sequence)
    while '1' in sequence:
        current_packet, sequence = compute(sequence)
        versions += current_packet['version']
        print(current_packet, sequence, current_packet['version'])

    return versions


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
