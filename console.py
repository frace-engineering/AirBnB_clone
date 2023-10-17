#!/usr/bin/python3
""" Create HBNBCommand class that inherites from cmd.Cmd class """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """
    define the class methods/command to be recorgnized by this class
    """
    prompt = "(hbnb) "

    def default(self, line):
        """method called on input line when command prefix is not
        recognized

        Args:
            - line: the command line

        Returns: mixed
        """

        self._precmd(line)

    def _precmd(self, line):
        """Runs commands for model.command() syntax

        Args:
            - line: the command line

        Returns: mixed
        """

        match = re.search(r"^(\w+).(\w+)\(([^)]*)\)$", line)
        if not match:
            return line

        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)

        id = args
        attrib = ""
        value = ""
        match2 = re.search(r'(^"(?:\w+-)+\w+"), ("\w+"), ("\w+@?\w+\.?\w+")',
                           args)
        match_id_and_args = match2
        if match_id_and_args:
            id = match_id_and_args.group(1)
            attrib = match_id_and_args.group(2)
            value = match_id_and_args.group(3)

        id = id.replace('"', '')
        attrib = attrib.replace('"', '')
        value = value.replace('"', '')
        command = method + " " + classname + " " + id
        command += " " + attrib + " " + value
        self.onecmd(command)
        return command

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
        """prints help for all command"""
        msg = "Prints all string representation of all"
        msg += " instances based or not on the class name"
        print(msg)

    def do_update(self, line):
        """Update an instance based on the class name and id
        by adding or updating attribute

        Args:
            - line: the command line

        Returns: None
        """

        if line == "" or line is None:
            print("** class name missing **")
            return

        args = line.split()
        classname = args[0]
        if classname not in storage.classes():
            print("*** class doesn't exist ***")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        id = args[1]
        key = "{}.{}".format(classname, id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attribute = args[2]

        if len(args) == 3:
            print("** value missing **")
            return
        value = args[3]

        cast = None
        if not re.search('^".*"$', value):
            if '.' in value:
                cast = float
            else:
                cast = int
        else:
            value = value.replace('"', '')
        attributes = storage.attributes()[classname]
        if attribute in attributes:
            value = attributes[attribute](value)
        elif cast:
            try:
                value = cast(value)
            except ValueError:
                pass  # value is string
        setattr(storage.all()[key], attribute, value)
        storage.all()[key].save()

        print(classname, id, attribute, value)

    def do_count(self, line):
        """Counts the number of instances of the class
        in the line

        Args:
            -line: the command line

        Returns: None
        """

        args = line.split()
        if not args[0]:
            print("** class name is missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        matches = [k for k in storage.all() if k.startswith(args[0] + '.')]
        print(len(matches))

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
