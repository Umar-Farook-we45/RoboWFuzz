import wfuzz
from robot.api import logger


header = """
==================================================================
ID	Response   Lines      Word         Chars          Request    
==================================================================
"""
class RoboWFuzz(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, dirfile):
        self.dirfile = dirfile

    def brute_directories(self, url_fuzz, concur = "1", file_name = "directory_brute.txt", format = 'raw', follow = "False"):
        
        if(follow == "True"):
            follow = True
        else:
            follow = False
            logger.info("Disable Brute Force")

        sess = wfuzz.FuzzSession(url=url_fuzz, printer=(file_name, format), concurrent=int(concur), follow = bool(follow))
        target = "Target: {0}".format(url_fuzz)

        if(format == 'raw'):
            f = open(file_name,'w+')
            f.write(target + '\n' + header + '\n')

            for req in sess.fuzz(hc = [404], payloads = [("file", dict(fn = self.dirfile))]):
                f.write(str(req)+ '\n')
                logger.info(req)
            f.close()
        else:
            for req in sess.fuzz(hc = [404], payloads = [("file", dict(fn = self.dirfile))]):
                logger.info(req)