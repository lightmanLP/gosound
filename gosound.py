from sys import getfilesystemencoding
from ctypes import c_buffer, windll
from abc import ABC, abstractmethod
from typing import Tuple
from random import random


class AbstractPlaySound(ABC):
    """Abstract class of PlaySound"""
    @abstractmethod
    def volume(self, volume_percent: int):
        """
        Sets sound volume

        args:
        volume_percent: int = volume (from 0 to 100)
        """
        pass

    @abstractmethod
    def stop(self):
        """Stops sound"""
        pass


class PlaySound(AbstractPlaySound):
    """Plays sound from selected time"""
    def __init__(self, sound: str, play_sec: Tuple[int or float, int or float]):
        """
        sound: str = path to file | directory:/folder/folder2/file
        play_sec: tuple = start and end of sound | (start, end)
    
        /////////////////////////////////////////////////////////
        HINTS:
        
        In variable play_sec decimal float numbers must be less than 3 digits.
    
        Lib working only on WINDOWS.
    
        /////////////////////////////////////////////////////////
        """
        alias = f'playsound_{random()}'
        play_start, play_stop = [int(i * 1000) for i in play_sec]
        self._winCommand(f'open "{sound}" alias {alias}')
        self._winCommand(f'set {alias} time format milliseconds')
        self._winCommand(f'play {alias} from {play_start} to {play_stop}')

    def _winCommand(self, command: str):
        """I rly don't know wtf is this"""
        buf = c_buffer(255)
        command = command.encode(getfilesystemencoding())
        errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))


if __name__ == '__main__':
    print("V1.0 | SUPPORT OS: \n1)Windows\n/Author: @BTDIZP/GitHub rep: ")