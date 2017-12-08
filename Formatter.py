import os
import psutil

class Wiper():

    currDrive = ''
    drivePath = ''
    def __init__(self, drive=None):
        self.drive = drive

    def testDrive(self):
        print(self.drive)

    def closeDrive():
        self.drive.close()
        print("Drive Closed!")

    def openDrive(self, drive):
        self.drive = drive
        print("Drive opened!")

    def checkFileSystem(self):
        disk_partitions = psutil.disk_partitions()[0]
        print(disk_partitions)

    def formatToNTFS(drive=None):
        if drive is None: #Use current drive
            pass
        else:
            pass

    def formatToFAT32(drive=None):
        if drive is None: #Use current drive
            pass
        else:
            pass
    def setDrivePath(self, path):
        self.drivePath = path

#Variable for path (change using GUI or static only lol)
path = "/dev/sdc"

with open("/dev/sdc", 'r+b') as drive:
    wiper = Wiper()
    wiper.setDrivePath(path)
    wiper.openDrive(drive)

wiper.testDrive()
wiper.checkFileSystem()
