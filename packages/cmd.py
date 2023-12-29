import os

def command(commandText):
    os.system(f"{commandText}")

def createDirectroy(dirPath):
    os.system(f"mkdir {dirPath}")
    os.system("ls")

def removeDirectory(dirPath):
    os.system(f"rm -rf {dirPath}")
    os.system("ls")