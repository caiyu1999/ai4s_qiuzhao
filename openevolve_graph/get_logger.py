import logging
import os
import time


def setup_root_logger(log_dir: str = "", log_level: str = "DEBUG"):
    """
    设置根logger，确保所有子logger都能正确输出。
    这是推荐的配置方式，因为它会捕获所有logger的输出。
    
    :param log_dir: 日志文件存放目录。如果为None，则只输出到控制台。
    :param log_level: 日志级别，字符串类型，如"INFO"、"DEBUG"等。
    """
    # 获取根logger
    root_logger = logging.getLogger()
    
    # 清空现有的handlers
    root_logger.handlers.clear()
    
    # 设置日志级别
    root_logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # 创建formatter
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # 控制台输出
    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(formatter)
    # root_logger.addHandler(console_handler)
    
    # 文件输出
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        file_path = os.path.join(log_dir, f"openevolve_{time.strftime('%Y%m%d_%H%M%S')}.log")
        file_handler = logging.FileHandler(file_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    
    # 确保子logger能传播到根logger（这是默认行为，但明确设置）
    root_logger.propagate = True
    
    return root_logger

# 详细的日志类
class DetailedLogger:
    """详细的日志记录器，用于精准定位问题"""
    
    def __init__(self, name: str = "GraphNode"):
        self.name = name
        self.logger = logging.getLogger(__name__)
    def info(self, message: str, **kwargs):
        """记录信息日志"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        extra_info = " | ".join([f"{k}={v}" for k, v in kwargs.items()]) if kwargs else ""
        log_msg = f"[INFO] {timestamp} | {self.name} | {message}"
        if extra_info:
            log_msg += f" | {extra_info}"
        # 这里会对接上层的父代logger
        self.logger.info(log_msg)
    
    def error(self, message: str, **kwargs):
        """记录错误日志"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        extra_info = " | ".join([f"{k}={v}" for k, v in kwargs.items()]) if kwargs else ""
        log_msg = f"[ERROR] {timestamp} | {self.name} | {message}"
        if extra_info:
            log_msg += f" | {extra_info}"
        # 这里会对接上层的父代logger
        self.logger.error(log_msg)
    
    def warning(self, message: str, **kwargs):
        """记录警告日志"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        extra_info = " | ".join([f"{k}={v}" for k, v in kwargs.items()]) if kwargs else ""
        log_msg = f"[WARNING] {timestamp} | {self.name} | {message}"
        if extra_info:
            log_msg += f" | {extra_info}"
        # 这里会对接上层的父代logger
        self.logger.warning(log_msg)
    
    def debug(self, message: str, **kwargs):
        """记录调试日志"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        extra_info = " | ".join([f"{k}={v}" for k, v in kwargs.items()]) if kwargs else ""
        log_msg = f"[DEBUG] {timestamp} | {self.name} | {message}"
        if extra_info:
            log_msg += f" | {extra_info}"
        # 这里会对接上层的父代logger
        self.logger.debug(log_msg)
    
    def step(self, step_name: str, **kwargs):
        """记录步骤日志"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        extra_info = " | ".join([f"{k}={v}" for k, v in kwargs.items()]) if kwargs else ""
        log_msg = f"[STEP] {timestamp} | {self.name} | {step_name}"
        if extra_info:
            log_msg += f" | {extra_info}"
        # 这里会对接上层的父代logger
        self.logger.info(log_msg)