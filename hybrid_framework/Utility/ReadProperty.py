import configparser

obj = configparser.RawConfigParser()
obj.read(r"C:\Users\user\PycharmProjects\pythonProject_WE_October\hybrid_framework\Configurations\common_data.ini")

class Read_Property:
    @staticmethod
    def GetURL():
        return obj.get('common data', 'url')

    @staticmethod
    def GetUsername():
        return obj.get('common data', 'username')

    @staticmethod
    def GetPassword():
        return obj.get('common data', 'password')