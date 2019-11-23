def render_file(input_path, output_path, strings=None):
    """Render part of input file to output file. If
    strings not specified, uses all file, otherwise
    take only selected strings.

    Parameters
    ----------
    input_path : str
        Path to input file.
    output_path : str
        Path to output file.
    strings : set of int
        Numbers of strings to render, default None.
    """
    with open(input_path) as input_file, open(output_path, 'w') as output_file:
        if strings:
            string_count = 0
            for line in input_file:
                if string_count in strings:
                    output_file.write(line)
                string_count += 1

        else:
            for line in input_file:
                output_file.write(line)


if __name__ == '__main__':
    input_p = '..\\.gitignore'
    render_file(input_p, 'test1.txt', strings={1, 3, 5})
    render_file(input_p, 'test2.txt')
