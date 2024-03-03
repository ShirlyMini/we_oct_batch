import logging
import datetime

dt = datetime.datetime.now()

def custom_log():#dont use logger name
    # logging.basicConfig(filename=fr'.\Logs\test_{dt.strftime("%Y%b%d_%H%M%S")}.log', filemode="w", level=logging.INFO,
    #                     format="%(levelname)s :: %(asctime)s %(message)s", force=True)
    logging.basicConfig(handlers=[logging.FileHandler(filename=fr'.\Logs\test_{dt.strftime("%Y%b%d_%H%M%S")}.log', mode="w"),
                                  logging.StreamHandler()],
                        level=logging.INFO,
                        format="%(levelname)s :: %(asctime)s %(message)s", force=True)
    logging.getLogger()
    return logging