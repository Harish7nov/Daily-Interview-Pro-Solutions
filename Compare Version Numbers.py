''' Version numbers are strings that are used to identify unique states of software products. A version number is in the format a.b.c.d.
	and so on where a, b, etc. are numeric strings separated by dots. These generally represent a hierarchy from major to minor changes.
	Given two version numbers version1 and version2, conclude which is the latest version number. Your code should do the following:
		If version1 > version2 return 1.
		If version1 < version2 return -1.
		Otherwise return 0.

	Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and that the version strings do not start or end with
	dots. Unspecified level revision numbers default to 0.
'''

class Solution:
    def level(self,version):
        l=1
        for i in version:
            if(i=='.'):
                l+=1
        return(l)
    def compareVersion(self, version1, version2):
        if(self.level(version1)!=self.level(version2)):
            return(0)
        j=0
        v1=0
        v2=0
        i=0
        c=True
        while(c):
            #print(i)
            while(version1[i]!='.'):
                i+=1
            v1=version1[j:i]
            v1=int(v1)
            i=j
            while(version2[i]!='.'):
                i+=1
            v2=version2[j:i]
            v2=int(v2)
            i+=1
            j=i
            if(v1<v2):
                return -1
            elif(v1>v2):
                 return 1
            else:
                continue
   
#Driver Code
version1 = "1.100.1"
version2 = "2.005.2"
print(Solution().compareVersion(version1, version2))
