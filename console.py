#!/usr/bin/python3
""" Create HBNBCommand class that inherites from cmd.Cmd class """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    define the class methods/command to be recorgnized by this class
    """
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Press ctrl + D or enter 'EOF' to exit the program\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
