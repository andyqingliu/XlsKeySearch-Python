import logging
import coloredlogs
import sys

global logger

logger = logging.getLogger("Test")

logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter("%(asctime)s[%(thread)d] %(levelname)s %(pathname)s[:%(lineno)d] %(message)s")

coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}, 'levelname': {'color': 'yellow', 'bold': True}, 'name': {'color': 'blue'}, 'pathname': {'color': 'cyan'}}
coloredlogs.install(fmt="%(asctime)s[%(thread)d] %(levelname)s %(pathname)s[:%(lineno)d] %(message)s")

# 输出到控制台
# streamHandler = logging.StreamHandler(sys.stdout)
# logger.addHandler(streamHandler)

# testing 

# 输出到文件
fileHandler = logging.FileHandler(filename="Log.txt", mode="w", encoding="utf-8")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)