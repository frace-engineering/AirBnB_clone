#!/usr/bin/python3
""" Create HBNBCommand class that inherites from cmd.Cmd class """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    define the class methods/command to be recorgnized by this class
    """
    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            }
    objects = {}

    def do_create(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name in self.classes:
                cls_instance = self.classes[cls_name]()
                cls_instance.save()
            else:
                print("** class doesn't exist **")

    def help_create(self):
        print("Create an instance of the BaseModel class\n")

    def do_show(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = cls_name.instance_id
        if key in self.objects:
            instance = self.objects[key]
            print(instance)
        else:
            print("** no instance found **")

    def help_show(self):
        print("Prints the string representation of an instance"
              "based on the class name and id")

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
