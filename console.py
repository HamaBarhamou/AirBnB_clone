#!/usr/bin/python3
import cmd
import sys
import json
import models
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}

    def do_create(self, classNam):
        """Creates a new instance of BaseModel"""
        if len(classNam) == 0:
            print('** class name missing **')
        elif classNam not in HBNBCommand.classes.keys():
            print("** class doesn't exist**")
        else:
            new = HBNBCommand.classes[classNam]()
            new.save()
            print(new.id)

    def do_show(self, classNam):
        """Print string representation of an instance"""
        base_list = classNam.split()
        if len(base_list) == 0:
            print("** class name missing **")
            return
        elif base_list[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(base_list) == 1:
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            keys = base_list[0] + '.' + base_list[1]
            if keys in instances:
                print(instances[keys])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        className = line.split()

        if len(className) == 0:
            print("** class name missing **")
            return
        elif className[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(className) == 1:
            print("** instance id missing **")
        else:
            instances = className[0] + "." + className[1]
            if instances  in models.storage.all():
                del models.storage.all()[instances]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, classNam):
        """Print a string of an instance based on class name"""
        args = classNam.split(" ")
        if args[0] == "" or args[0]in HBNBCommand.classes:
            string = []
            objs = storage.all()
            for key in objs.keys():
                if args == [''] or key.split(".")[0] == args[0]:
                    string.append(str(objs[key]))
            print(string)
        else:
            print("** class doesn't exist **")

    def do_update(self, classNam):
        """Updates an instance based on the class name"""
        classNam = classNam.split()
        if len(classNam) == 0:
            print("** class name missing **")
            return
        elif classNam[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(classNam) == 1:
            print("** instance id missing **")
            return

        

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
