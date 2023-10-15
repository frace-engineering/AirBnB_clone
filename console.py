#!/usr/bin/python3
""" Create HBNBCommand class that inherites from cmd.Cmd class """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    define the class methods/command to be recorgnized by this class
    """
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates and saves a new instance of Base Model
        Args:
            - line: the command line argument
        
        Returns: None
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if cls_name in storage.classes():
                new_instance = storage.classes()[cls_name]()
                new_instance.save()
                print(f"{new_instance.id}")
            else:
                print("** class doesn't exist **")

    def help_create(self):
        """Prints help for create"""

        print("Create an instance of the BaseModel class\n")

    def do_show(self, line):
        """prints the string representation of an instance
        based on the class name and id
        
        Args:
            - line: command line argument

        Returns: None
        """

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{cls_name}.{instance_id}"
        if key in storage.all():
            instance = storage.all()[key]
            print(instance)
        else:
            print("** no instance found **")

    def help_show(self):
        """Shows help for show command"""

        print("Prints the string representation of an instance"
              " based on the class name and id")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        
        Args:
            - line: command line arg

        Returns: None
        """

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        instance_id = args[1]
        key = f"{cls_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
            return

    def help_destroy(self):
        """Shows help for destroy command"""

        print("Deletes an instance based on the class name and id")

    def do_all(self, line):
        """prints all string representation of all instances
        based or not on the class namd
        
        Args:
            - line: command line arg
            
        Returns: None
        """

        args = line.split()
        if len(args) == 0:
            models = [str(value) for key, value in storage.all().items()]
            print(models)
        else:
            cls_name = args[0]
            if cls_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                models = [str(value) for key, value in storage.all().items()
                          if type(value).__name__ == cls_name]
                print(models)
       

    def help_all(self):
        print("Prints all string representation of all instances based or not on the class name")
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
