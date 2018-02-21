import wfuzz
from robot.api import logger

# s = wfuzz.FuzzSession(url="http://testphp.vulnweb.com/FUZZ", printer = ("session.json", "json"), concurrent = 6)
#
# for req in s.fuzz(hc = [404], payloads = [("file", dict(fn = "/Users/abhaybhargav/Documents/Code/Python/RoboWFuzz/directory-list-1.0.txt"))]):
#     print req

class RoboWFuzz(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, dirfile):
        self.dirfile = dirfile

    def brute_directories(self, url_fuzz, concur = "1", file_name = "directory_brute.json", follow = "False"):
        sess = wfuzz.FuzzSession(url=url_fuzz, printer=(file_name, "json"), concurrent=int(concur), follow = bool(follow))

        for req in sess.fuzz(hc = [404], payloads = [("file", dict(fn = self.dirfile))]):
            logger.info(req)
