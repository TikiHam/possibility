import sys
import argparse
from Counting_engine import Counting_engine


def positive_int(value):
    try:
        int_value = int(value)
        print('Hello GitHub')
        if int_value < 1:
            raise argparse.ArgumentTypeError(f'{value} is not >= 1')
        return int_value
    except ValueError:
        raise argparse.ArgumentTypeError(f'{value} should be an integer >= 1')



def main():
    parser = argparse.ArgumentParser('Counting a possibility of unique N letter sequence')
    parser.add_argument('file_list', type=str, nargs='*', help='file list')
    parser.add_argument('n', help = 'len of the seq.', type = positive_int)
    arg = parser.parse_args()


    engine = Counting_engine(arg.n)

    if arg.file_list:
        try:
            engine.go_file_way(arg.file_list)
        except ValueError:
            sys.exit('Please type greater N or give file(s) with bigger amount of letters')
        except FileNotFoundError:
            sys.exit('One of the files names is invalid')
        print(engine)

    else:
        try:
            engine.go_user_input_way()
        except ValueError:
            sys.exit('Please type greater N or type more letters')
        print(engine)

if __name__ == '__main__':
    main()
