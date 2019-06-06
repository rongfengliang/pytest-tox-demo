from hashids import Hashids
hashids = Hashids()
def generateID():
    hashid = hashids.encode(123, 456, 789)
    return hashid