mydict={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "service-prefix:action-name",
            "Resource": "*",
            "Condition": {
                "DateGreaterThan": {"aws:CurrentTime": "2020-04-01T00:00:00Z"},
                "DateLessThan": {"aws:CurrentTime": "2020-06-30T23:59:59Z"}
            }
        }
    ]
}
print(mydict["Version"])
print(mydict["Statement"])
print(mydict["Statement"][0])
print(mydict["Statement"][0]["Effect"])
print(mydict["Statement"][0]["Action"])
print(mydict["Statement"][0]["Resource"])
print(mydict["Statement"][0]["Condition"])
print(mydict["Statement"][0]["Condition"]["DateGreaterThan"])
print(mydict["Statement"][0]["Condition"]["DateLessThan"])
