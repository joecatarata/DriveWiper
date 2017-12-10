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


        return self.driveInfo

    def formatDrive(self, outputFileSystem=None, drive=None):
        if drive is None: #Use current drive
            drive = self.drive
        if outputFileSystem is None: #default Format
            outputFileSystem = "FAT32"
        if "Linux" in platform.platform(): #for Linux
            os.system("umount " + self.drivePath)
            if outputFileSystem is "FAT32":
                os.system("sudo mkfs.vfat -F 32 "  + self.drivePath)
                print("Drive formatted to FAT32!")
            elif outputFileSystem == "ext4": #Working
                os.system("sudo mkfs.ext4 " + self.drivePath)
                print("Drive formatted to ext4!")
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

    def deleteFile(self, fileName, algorithm=None, path=None):
        if path is None:
            path = self.driveInfo[1]
        if algorithm is None:
            algorithm = "ZeroFill"

        metadata = self.getMetaData(fileName)
        fileSize = metadata['File Size']
        with open(os.path.join(path,fileName), "wb+") as file:
            for ctr in range(0,fileSize):
                if algorithm is "ZeroFill":
                    file.write(b'\x00')
                    print("Entered 0Fill")
                elif algorithm is "OneFill":
                    file.write(b'\x11')
                    print("Entered 1fill")
                elif algorithm is "AlterFill": #Alternate Fill (0/1)
                    if ctr % 0 is 0:
                        file.write(b'\x00')
                    else:
                        file.write(b'\x11')
                elif algorithm is "TwoFill":
                    file.write(b'\x10')
                elif algorithm is "ThreeFill":
                    file.write(b'\x11')

            os.remove(os.path.join(path,fileName))

        print("File deleted!")


    def getMetaData(self, fileName, path=None):
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
#wiper.writeFile()
#wiper.deleteFile("new 1.txt", "OneFill")
#wiper.formatDrive("FAT32") #Change argument to output fileSystem
