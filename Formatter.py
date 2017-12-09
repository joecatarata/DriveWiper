import os
import psutil
import platform
import re

class Wiper():
    currDrive = ''
    drivePath = ''
    driveInfo = []
    linuxCommands = {}
    def __init__(self, drive=None):
        self.currDrive = drive

    def testDrive(self):
        print(self.drive)

    def closeDrive():
        self.drive.close()
        print("Drive Closed!")

    def openDrive(self, drive):
        self.drive = drive
        print("Drive opened!")

    def getFileSystem(self, driveLetter=None): #Gets file system and assigns it to self.drivePath
        print(self.drivePath)
        for disk in psutil.disk_partitions():
            print(disk[0])
            if driveLetter is None:
                if(disk[0] == self.drivePath):
                    print("Found " + self.drivePath + "'s Metadata!")
                    self.driveInfo = disk
                    print(self.driveInfo)
            else: #G:\\
                if(disk[0] == driveLetter):
                    print("Found " + self.drivePath + "'s Metadata!")
                    self.driveInfo = disk
                    print(self.driveInfo)

    def formatDrive(self, outputFileSystem=None, drive=None):
        if drive is None: #Use current drive
            drive = self.drive
        if outputFileSystem is None: #default Format
            outputFileSystem = "FAT32"
        if "Linux" in platform.platform(): #for Linux
            os.system("umount " + self.drivePath)
            if outputFileSystem is "FAT32":
                os.system("sudo mkfs.vfat "  + self.drivePath)
                print("Drive formatted to FAT32!")
            elif outputFileSystem == "NTFS": #NOT WORKING! TO DO
                os.system("sudo mkntfs " + self.drivePath)
                print("Drive formatted to NTFS!")
            elif outputFileSystem is "exFat":
                os.system("sudo mkfs.exfat " + self.drivePath)
                print("Drive formatted to exFat!")

    def setDrivePath(self, path):
        self.drivePath = path

    def writeFile(self, fileName=None, string=None):#test Update: working!
        if fileName is None:
            fileName = "sample.txt"
        if string is None:
            string = "Sample"
        with open(os.path.join(self.driveInfo[1], fileName), "w") as file:
            file.write(string)
            print("File written at " + os.path.join(self.driveInfo[1], fileName))

    def listFiles(self, path=None):
        if path is None:
            path = self.driveInfo[1]
        print(os.listdir(path))

    def deleteFile(self, fileName, **kwargs):
        if 'path' not in kwargs:
            path = self.driveInfo[1]
        else:
            path = kwargs['path']
        with open(os.path.join(path,fileName), "r+b") as file:
            pass

    def getMetadata(self, fileName, path=None):
        if path is None:
            path = self.driveInfo[1]

        metadata = {}
        temp = os.stat(os.path.join(path,fileName))
        print(temp)
        metadata["File Name"] = fileName
        metadata["Inode"] = temp[1]
        metadata["File Size"] = temp[6]

        print(metadata)
        return metadata
        #Do data unit and metadata layer



#Variable for path (change using GUI or static only lol)
path = "/dev/sdc"

#Open drive in r+b
with open(path, 'r+b') as drive:
    wiper = Wiper()
    wiper.setDrivePath(path)
    wiper.openDrive(drive)

#Testing the methods
wiper.testDrive()
wiper.getFileSystem()
wiper.listFiles()
#wiper.getMetadata("sample.txt")
wiper.writeFile()
#wiper.deleteFile('path'=/dev/sdc)
wiper.formatDrive("exFat") #Change argument to output fileSystem
