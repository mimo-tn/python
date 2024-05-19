class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):	# added this line, takes a value
        new_node = SLNodes(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNodes(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self
    # def remove_from_front(self):
    #     # new_node = SLNodes(val)
    #     # new_node.next = self.head
    #     # print(self.head)
    #     self.head = None
    #     return self
class SLNodes:
    def __init__(self, val):
        self.value = val
        self.next = None
my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.remove_from_front().print_values()
