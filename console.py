#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """end-of-file cmd: exit the program"""
        return True

    def help_EOF(self):
        """Help to exit the program"""
        print("end-of-file: exit the program\n")

    def do_quit(self, line):
        """Quit the program"""
        return True

    def help_quit(self):
        """Help to quit the program"""
        print("Exit the program\n")

    def emptyline(self):
        """
        If this method is not overriden, it repeats
        the last nonempty cmd entered
        """
        return False

if __name__ == '__main__':
     HBNBCommand().cmdloop()
