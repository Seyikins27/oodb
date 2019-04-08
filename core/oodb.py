from core.File_ops import mk_dir, mk_file, write_file, read_json_file


class Oodb:
    dir = ""
    class_name = ""
    file_name = ""

    def __init__(self, user, password, server, project):
        self.project=project

    def set_class(self, class_name, args=""):
        Oodb.dir = "../dbin/classes/" + self.project
        mk_dir(Oodb.dir)
        Oodb.class_name = class_name
        Oodb.file_name = Oodb.dir + "/" + Oodb.class_name + ".json"
        mk_file(Oodb.file_name, 'w+')
        write_file(Oodb.file_name, args, True)

    def select(self, args=""):
        if args == "":
            data = read_json_file(Oodb.file_name)
            print(data)
        else:
            print()
        return

    def update(self):
        return

    def delete(self):
        return

    def set_key(self):
        return

    def has_many(self):
        return

    def belongs_to(self):
        return

    def extends(self):
        return
