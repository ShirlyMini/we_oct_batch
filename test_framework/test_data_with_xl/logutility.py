import logging

# log_obj = logging.getLogger()
# print(log_obj)
# log_obj.setLevel(logging.DEBUG)
# print(log_obj)
# logging.debug("this is info")
# logging.info("this is info")
# logging.warning("this is info")
# logging.error("this is info")
# logging.critical("this is info")

########
# logging.basicConfig(filename=r".\log_1.txt", filemode="a", level=logging.DEBUG,format="%(levelname)s :: %(asctime)s %(message)s")
#
# log_obj = logging.getLogger()
# # print(log_obj)
# # log_obj.setLevel(logging.DEBUG)
# # print(log_obj)
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warn")
# logging.error("this is error")
# logging.critical("this is critical")

####################3

def logger():
    logging.basicConfig(filename=r".\log_1.txt", filemode="a", level=logging.DEBUG,
                        format="%(levelname)s :: %(asctime)s %(message)s")
    logging.getLogger()
    return logging