from django.db import models
import math

class College(models.Model):
    #basic data
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, default="", blank=True)
    year = models.CharField(max_length=9, default="")
    state = models.CharField(max_length=20, default="")

    #total undergrad university ethnicity data
    internationalStudents = models.IntegerField('International Students',default=0)
    hispanicStudents = models.IntegerField('Hispanic Students', default=0)
    blackStudents = models.IntegerField('African American, non-hispanic Students', default=0)
    whiteStudents = models.IntegerField('Nhite, non-hispanic students', default=0)
    nativeStudents = models.IntegerField('American Indian or Alaska Native, non-hispanic', default=0)
    asianStudents = models.IntegerField('Asian, non-hispanic', default=0)
    pacificStudents = models.IntegerField('Native Hawaiian or Pacific Islander, non-hispanic', default=0)
    mixedStudents = models.IntegerField('Two or More races, non-hispanic', default=0)
    unknownStudents = models.IntegerField('unknown ethinicity', default=0)
    def totalUndergrads(self):
        return self.internationalStudents + self.hispanicStudents + self.blackStudents + self.whiteStudents + self.nativeStudents + self.mixedStudents + self.unknownStudents

    #application Data
    #totalApps = models.IntegerField('Total Applications', default=0)
    maleApps = models.IntegerField('Male Applications', default=0)
    femaleApps = models.IntegerField('female Applications', default=0)
    #otherApps = models.IntegerField("Other Applications", blank=True, default=0)

    #admitted Data
    #totalAdmits = models.IntegerField('Total Admissions', default=0)
    maleAdmits = models.IntegerField('Male Admissions', default=0)
    femaleAdmits = models.IntegerField('Female Admissions', default=0)
    #otherAdmits = models.IntegerField('Other Admits', blank=True, default=0)

    maleEnrolled = models.IntegerField('Male Enrolled', default=0)
    femaleEnrolled = models.IntegerField('female Enrolled', default=0)

    #wait list
    offeredWaitlist = models.IntegerField(blank=True, default=0)
    tookWaitlist = models.IntegerField(blank=True, default=0)
    admittedWaitlist = models.IntegerField(blank=True, default=0)
    def waitlistAcceptRate(self):
        return round((self.admittedWaitlist/self.tookWaitlist)*100, 2)

    #SAT data
    satWriting25th = models.IntegerField(blank=True,default=0)
    satWriting75th = models.IntegerField(blank=True,default=0)
    satMath25th = models.IntegerField(blank=True,default=0)
    satMath75th = models.IntegerField(blank=True,default=0)
    def satTotal25th(self):
        return self.satMath25th + self.satWriting25th
    def satTotal75th(self):
        return self.satMath75th + self.satWriting75th

    #act data
    actMath25th = models.IntegerField(blank=True,default=0)
    actMath75th = models.IntegerField(blank=True,default=0)
    actEnglish25th = models.IntegerField(blank=True,default=0)
    actEnglish75th = models.IntegerField(blank=True,default=0)
    def actTotal25th(self):
        return round((self.actMath25th + self.actEnglish25th)/2)
    def actTotal75th(self):
        return round((self.actMath75th + self.actEnglish75th)/2)

    #athletic Division
    athDiv = models.CharField(max_length=50, default="", blank=True)
    athConference = models.CharField(max_length=50, default='', blank=True)

    #finance stuff
    tuitionCost = models.IntegerField(default=0)
    roomCost = models.IntegerField(default=0)
    boardCost = models.IntegerField(default=0)
    requiredFeeCost = models.IntegerField(default=0)
    def totalCost(self):
        return self.tuitionCost + self.roomCost + self.boardCost + self.requiredFeeCost

    studentFacultyRatio = models.CharField(max_length=50, default="", blank=True)

    #totals
    def totalApps(self):
        return self.maleApps + self.femaleApps

    def totalAdmits(self):
        return self.maleAdmits + self.femaleAdmits

    def totalEnrolled(self):
        return self.maleEnrolled + self.femaleEnrolled

    #acceptance rate data
    def totalAcceptRate(self):
        return round((self.maleAdmits + self.femaleAdmits) / (self.maleApps+self.femaleApps) * 100, 2)

    def maleAcceptRate(self):
        return round((self.maleAdmits)/(self.maleApps) * 100, 4)

    def femaleAcceptRate(self):
        return round((self.femaleAdmits)/(self.femaleApps) * 100, 4)

    #yield data
    def totalYield(self):
        return round((self.totalEnrolled())/(self.totalAdmits()) * 100, 2)

    def maleYield(self):
        return round((self.maleEnrolled)/(self.maleAdmits) * 100, 2)

    def femaleYield(self):
        return round((self.femaleEnrolled)/(self.femaleAdmits) * 100, 2)

    def __str__(self):
        return self.name
