import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("learning-artifacts/00-12-debugging-and-profiling/logging_info.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

logger.info("训练开始")
logger.warning("损失异常升高")
logger.error("损失出现 NaN，停止训练")
print("程序仍然执行到了这里")
