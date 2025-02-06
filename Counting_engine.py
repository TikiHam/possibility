import sys
class Counting_engine:

    def __init__(self, n: int):
        self.n = n
        self.pick_list = []
        self.summ = 0
        self.counting_dict = {}
        self.pointer = 0

    def __str__(self):
        result = ''
        for key, value in self.counting_dict.items():
            result += f'The chance of {key} combination = {round(value/self.summ, 7)}\n'
        return result

    def eat_a_line(self, line: str):
        '''
        This function resieves a line, and letter by letter build a pick_list,
            moving pointer in that pick_list by this rule: pointer = (pointer +1) % len(pick_list)
            wich implements "conveyeer method"
        each pick_list it sends to add_to_dict method
        '''
        for character in line:
            self.pick_list[self.pointer] = character
            self.pointer = (self.pointer + 1) % self.n
            self.add_to_dict(self.pick_list, self.pointer)

    def add_to_dict(self, list, support_pointer: int):
        '''
        This function resieves a list of letters to add to dict and a pointer, that points on the oldest letter
            aka letter to start parcing from
        '''
        support_string = ''
        support_n = len(list)
        for _ in range(support_n):
            support_string += list[support_pointer]
            support_pointer = (support_pointer + 1) % support_n

        self.counting_dict[support_string] = self.counting_dict.get(support_string, 0) + 1
        self.summ += 1

    def go_file_way(self, file_list):
        '''
        This function resieves list of file names to call from userinput
        1. It takes first pick, if N > number off all characters in all files ValueError will be raise
            It stroes first_pick, pointer that points on the index of the next symbol when we done collecting first pick,
            and index of that file
        2. It sends first pick to dict
        3. It sends the remained text to engine
        4. It reads remained files starting from remained_text_in_stop_file+1 and send their content to engine
        '''
        first_pick, pointer_on_the_next_after_exit_symbol, index_stop_file = self.get_first_pick(file_list)
        self.pick_list = first_pick

        self.add_to_dict(self.pick_list, 0)

        with open(file_list[index_stop_file],'r') as file:
            _ = 0
            while _ != pointer_on_the_next_after_exit_symbol:
                content = file.read(1)
                if not content.isalnum():
                    continue
                _ += 1
            for content in file.readlines():
                content = content.strip().replace(' ','')
                self.eat_a_line(content)


        for file_name in file_list[index_stop_file+1:]:
            with open(file_name, 'r') as file:
                for content in file.readlines():
                    content = content.strip().replace(' ','')
                    self.eat_a_line(content)


    def go_user_input_way(self):
        '''
        This function resieves user input of txt,
        checks that len of input is grater than N,
        stores first N characthers to pick_list,
        sends pick_list to dict and
        sends the rest of line to the engine
        '''

        resulting_txt = ''
        print(f'''I will read your input and count the possobility of all unique combination in it
    please make sure, that totall number of symbols in it is bigger than {self.n}.
    When you done please press ctrl+D.

    User input:''')
        for line in sys.stdin:
            resulting_txt += line.strip().replace(' ', '')

        if len(resulting_txt) < self.n:
            raise ValueError

        self.pick_list = list(resulting_txt[:self.n])

        self.add_to_dict(self.pick_list, 0)

        resulting_txt = resulting_txt[self.n:]
        self.eat_a_line(resulting_txt)

    def get_first_pick(self, file_name_list: list):
        file_index = 0
        pointer = 0
        support_string = ''
        for _file in file_name_list:
            with open(_file, 'r') as file:
                for content in file.readlines():
                    for character in content:
                        if not character.isalnum():
                            continue
                        support_string += character
                        pointer += 1
                        if len(support_string) == self.n:
                            # first_pick, pointer_on_the_next_after_exit_symbol, index_stop_file
                            return (list(support_string), pointer, file_index)

            pointer = 0
            file_index += 1
        # If after reading all the files we never manage to fulfill len(support_string) == self.n we raise ValueError
        raise ValueError


    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        self._n = n

    @property
    def pick_list(self):
        return self._pick_list

    @pick_list.setter
    def pick_list(self, value: list):
        self._pick_list = value

    @property
    def summ(self):
        return self._summ

    @summ.setter
    def summ(self, value: int):
        self._summ = value

    @property
    def counting_dict(self):
        return self._counting_dict

    @counting_dict.setter
    def counting_dict(self, value: dict):
        self._counting_dict = {}

    @property
    def pointer(self):
        return self._pointer

    @pointer.setter
    def pointer(self, index: int):
        self._pointer = index

