import os
import sys
import logging
from datetime import datetime


LOG_FILENAME=f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs",LOG_FILENAME)

os.makedirs(log_path,exist_ok=True)


logging.basicConfig(
    filename=os.path.join(log_path,LOG_FILENAME),
    format='%(asctime)-15s-%(name)s -%(levelno)d - %(levelname)s - %(message)s',
    level=logging.INFO
)

#  for testig purposr
# if __name__ == "__main__":
#     logging.info("logging started")