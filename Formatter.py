import os
import psutil
class Formatter():

    drive = ''
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
        psutil.disk_partitions()

with open("/dev/sdc", 'r+b') as drive:
    wiper = Formatter()
    wiper.openDrive(drive)

wiper.testDrive()
wiper.checkFileSystem()