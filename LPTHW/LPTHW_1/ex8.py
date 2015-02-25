formatter = "%r %r %r %r"
formatter2 = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print "no formatter", 1,2,3,4
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print formatter2 % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print "no formatter", 
print "I had this thing.",
print "That you could type up right.",
print "But it didn't sing.",
print "So I said goodnight."
