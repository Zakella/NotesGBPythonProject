class Note:
    def __init__(self, note_id, header, summary, creating_date):
        self.__id = note_id
        self.__summary = summary
        self.__header = header
        self.__creating_date = creating_date

    def get_id(self):
        return self.__id

    def get_summary(self):
        return self.__summary

    def get_header(self):
        return self.__header

    def get_creating_date(self):
        return str(self.get_creating_date)

    def __str__(self):
        return f"Id {self.__id} \n" \
               f"header :{self.__header} , \n" \
               f"summary: {self.__summary},\n" \
               f"created at: {self.__creating_date} \n"

    def in_dict(self):
        new_data = {'id': self.get_id(),
                    'header': self.get_header(),
                    'summary': self.get_summary(),
                    'created': self.get_creating_date()}
        return new_data



