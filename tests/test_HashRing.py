from src.HashRing import HashRing


def testHashInt():
    hashring = HashRing()
    testKey = "abc123"
    hashInt = hashring.hashInt(testKey)
    assert isinstance(hashInt, int), f"Expected type int, \
            but got {type(hashInt)}"


def runTests():
    # Test basic HashRing functions
    testHashInt()

    print("All tests passed!")


if __name__ == "__main__":
    runTests()
