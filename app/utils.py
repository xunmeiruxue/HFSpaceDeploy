import os, stat


def _chmod_and_retry(func, path, exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)
