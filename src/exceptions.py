import sys
from logger import logging


def error_message(error, error_message:sys):
    _, _, exc_tb = error_message.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = print("The error occured at file[{0}], line number [{1}], error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error)))

    return error_message

class CustomException():
    def __init__(self, error_detail, error_message:sys):
        super().__init__(error_detail, error_message)
        self.error_detail = error_message

        def __str__(self):
            return self.error_detail