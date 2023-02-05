class world():
    def __init__(self):
        blocks_amount = input()
        self.blocks_state = [[i] for i in range(int(blocks_amount))]

    def get_input(self):
        input_str = ""
        while input_str != "quit":
            input_str = input()
            if "quit" == input_str:
                self.print_output()
                break
            block1 = int(input_str.split(" ")[1])
            block2 = int(input_str.split(" ")[3])
            # Check if legal move
            if block1 == block2:
                continue
            if self.find_in_which_stack_the_block_is(block1) == self.find_in_which_stack_the_block_is(block2):
                continue
            if "move" in input_str:
                if "onto" in input_str:
                    self.move_a_onto_b(block1, block2)

                if "over" in input_str:
                    self.move_a_over_b(block1, block2)

            if "pile" in input_str:
                if "onto" in input_str:
                    self.pile_a_onto_b(block1, block2)

                if "over" in input_str:
                    self.pile_a_over_b(block1, block2)

    def move_a_onto_b(self, a, b):
        self.return_blocks_ontop_block_to_original_places(b)
        self.move_a_over_b(a, b)

    def move_a_over_b(self, a, b):
        self.return_blocks_ontop_block_to_original_places(a)
        stack_location_b = self.find_in_which_stack_the_block_is(b)
        stack_location_a = self.find_in_which_stack_the_block_is(a)
        self.remove_block_from_stack(a, stack_location_a)
        self.add_block_to_stack(stack_location_b, a)

    def pile_a_onto_b(self, a, b):
        self.return_blocks_ontop_block_to_original_places(b)
        self.pile_a_over_b(a, b)

    def pile_a_over_b(self, a, b):
        stack_location_a = self.find_in_which_stack_the_block_is(a)
        stack_location_b = self.find_in_which_stack_the_block_is(b)
        loc_in_stack = self.blocks_state[stack_location_a].index(a)
        blocks_ontop_a = self.blocks_state[stack_location_a][loc_in_stack:]
        self.blocks_state[stack_location_b].extend(blocks_ontop_a)
        for block in blocks_ontop_a:
            self.remove_block_from_stack(block, stack_location_a)

    def print_output(self):
        for i in range(len(self.blocks_state)):
            if self.blocks_state[i]:
                print(f"{i}: " + ' '.join(map(str, self.blocks_state[i])))
            else:
                print(f"{i}:")

    def return_blocks_ontop_block_to_original_places(self, block):
        stack_num = self.find_in_which_stack_the_block_is(block)
        loc_in_stack = self.blocks_state[stack_num].index(block) + 1
        blocks_ontop = self.blocks_state[stack_num][loc_in_stack:]
        for block in blocks_ontop:
            self.blocks_state[block].append(block)
        self.blocks_state[stack_num] = self.blocks_state[stack_num][:loc_in_stack]

    def find_in_which_stack_the_block_is(self, block):
        for stack_num in range(len(self.blocks_state)):
            if block in self.blocks_state[stack_num]:
                return stack_num

    def remove_block_from_stack(self, block, stack_location):
        self.blocks_state[stack_location].remove(block)

    def add_block_to_stack(self, stack_num, block):
        self.blocks_state[stack_num].append(block)


if __name__ == '__main__':
    world().get_input()
