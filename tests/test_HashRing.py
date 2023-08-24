from src.HashRing import HashRing


server = "ServerOne"
request = "/api/1230987/info"
response = "{name: Wahab, age: 22}"


def testHashInt():
    hashring = HashRing()
    testKey = "abc123"
    hashInt = hashring.hashInt(testKey)
    assert isinstance(hashInt, int), f"Expected type int, \
            but got {type(hashInt)}"


def testSimpleHashRing():
    cache = HashRing()
    cache.putNode(server)
    cache.putData(request, response)
    assert cache.getData(request) == response, "Data doesn't match"


def testSimpleReplacementTest():
    cache = HashRing()
    cache.putNode(server)
    cache.putData(request, response)

    serverTwo = "ServerTwo"
    cache.putNode(serverTwo)
    cache.removeNode(server)

    assert cache.getData(request) == response, "Data doesn't match"


def testEdgeCases():
    pass


def testInvalidScenarios():
    # Ex: Remove all nodes but without removing data
    pass


def runTests():
    # Test basic HashRing functions
    testHashInt()
    testSimpleHashRing()
    testSimpleReplacementTest()

    print("All HashRing tests passing!")


if __name__ == "__main__":
    runTests()
