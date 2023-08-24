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


def testSimpleReplacement():
    cache = HashRing()
    cache.putNode(server)
    cache.putData(request, response)

    serverTwo = "ServerTwo"
    cache.putNode(serverTwo)
    cache.removeNode(server)

    assert cache.getData(request) == response, "Data doesn't match"


def testModerateReplacement():
    cache = HashRing()
    startingServers = ["s1", "s2", "s3"]
    for s in startingServers:
        cache.putNode(s)

    data = [(str(r), str(r)) for r in range(8)]
    for req, res in data:
        cache.putData(req, res)

    newServers = ["s4", "s5", "s6"]
    for s in newServers:
        cache.putNode(s)

    for s in startingServers:
        cache.removeNode(s)

    for req, res in data:
        assert cache.getData(req) == res, "Data does not match"


def testEdgeCases():
    pass


def testInvalidScenarios():
    # Ex: Remove all nodes but without removing data
    pass


def runTests():
    # Test basic HashRing functions
    testHashInt()
    testSimpleHashRing()
    testSimpleReplacement()
    testModerateReplacement()

    print("All HashRing tests passing!")


if __name__ == "__main__":
    runTests()
