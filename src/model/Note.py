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
        return self.get_creating_date


