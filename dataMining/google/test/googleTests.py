from google.main import processTitles
import pprint

inputfile = "test.txt"

expectedJobTitles = ["software engineer", "systems analyst", "programmer", "project management",
                     "functional consultant", "business analyst", "computer scientist", 
                     "system engineer", "design engineer", "computer consultant", "software architect",
                     "customer service", "University lecturer", "defence research scientist",
                     "telecommunications engineer", "mechanical engineer", "electrical engineer",
                     "aerospace engineer", "civil engineer", "developer", "data scientist",
                     "application developer", "cloud architect", "build lead", "systems analyst",
                     "consultant", "chef", "social worker", "primary school teacher",
                     "database development", "hardware engineer", "computer programmer", "doctor",
                     "interaction designer", "physician", "teacher", "librarian"]

retrievedJobTitles = ["software engineer"]

processTitles(inputfile, "test", retrievedJobTitles)

count = 0
for title in expectedJobTitles:
    for retrievedTitle in retrievedJobTitles:
        if retrievedTitle == title:
            count = count + 1
            
for title in expectedJobTitles:
    if not title in retrievedJobTitles:
        print title
        
    
            
            
            
recall = count/float(len(expectedJobTitles))
accuracy = count/float(len(retrievedJobTitles))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(retrievedJobTitles)
print len(retrievedJobTitles)


print "recall is: " + str(recall) + " accuracy is: " + str(accuracy)


