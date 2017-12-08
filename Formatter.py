import os
import psutil

class Wiper():

    currDrive = ''
    drivePath = ''
    driveInfo = []
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

    def checkFileSystem(self):
        print(self.drivePath)

        for disk in psutil.disk_partitions():
            print(disk[0])
            if(disk[0] == self.drivePath):
                print("Found " + self.drivePath + "'s Metadata!")
                self.driveInfo = disk
                print(self.driveInfo)

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

    def writeFile(self, fileName=None, string=None):#test Update: working!
        if fileName is None:
            fileName = "sample.txt"
        if string is None:
            string = "Life"
        with open(os.path.join(self.driveInfo[1], fileName), "w") as file:
            file.write(string)
            print("File written at " + os.path.join(self.driveInfo[1], fileName))

    def listFiles(self, path=None):
        if path is None:
            path = self.driveInfo[1]
        print(os.listdir(path))


#Variable for path (change using GUI or static only lol)
path = "/dev/sdc"

#Open drive in r+b
with open("/dev/sdc", 'r+b') as drive:
    wiper = Wiper()
    wiper.setDrivePath(path)
    wiper.openDrive(drive)

#Testing methods
wiper.testDrive()
wiper.checkFileSystem()
wiper.writeFile()
wiper.listFiles()
