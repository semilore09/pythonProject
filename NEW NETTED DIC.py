CTYSCHOOL = {"jss1":
    {
    "child 1": {
                "firstname": "Jesutofunmi",
                    "surname": "Ayeola",
                    "othername": "oluwaseyi",
                    "Age": 12,
                    "Gender": "female",
                 "cummulative scores": [{"maths": 67, "Eng": 80, "V.O.A": 98, "RNV": 83, "LIT.IN.ENG": 58}]},
    "child 2": {
                "firstname": "Olusola",
                         "surname": "Awoniyi",
                         "othername": "Bridget",
                         "Age": 11,
                          "Gender": "female",
                "cummulative scores": [{"maths": 96, "Eng": 82, "V.O.A": 65, "RNV": 78, "LIT.IN.ENG": 50}]}},
"jss 2":{
        "child 1": {
                    "firsname": "Oluwafemi",
                         "surname": "Adebayo",
                         "othername": "Victor",
                          "Age": 14,
                          "Gender": "male",
                    "cummulative scores": [{"maths": 50, "Eng": 80, "V.O.A": 48, "RNV": 72, "LIT.IN.ENG": 98}]},
       "child 2": {
                    "firsname": "Aanuoluwapo",
                         "surname": "Adeniji",
                        "othername": "Elizabeth",
                        "Age": 12,
                        "Gender": "female",
                    "cummulative scores": [{"maths": 92, "Eng": 96, "V.O.A": 88, "RNV": 80, "LIT.IN.ENG": 95}]}}}
print(CTYSCHOOL)
a = CTYSCHOOL.items()
print(a)
print(CTYSCHOOL.keys())
print(CTYSCHOOL["jss1"])
print(CTYSCHOOL["jss1"]["child 1"]["firstname"])
print(CTYSCHOOL["jss 2"])
a = CTYSCHOOL["jss 2"]["child 1"]
print(a)
b = CTYSCHOOL["jss1"]["child 1"].update({"firstname":"Initial"})
print(b)
for i,o in CTYSCHOOL.values():
    print(i,o)