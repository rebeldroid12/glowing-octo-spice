print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "RAW: So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "NOT RAW: So, you're %s old, %s tall and %s heavy." % (
    age, height, weight)

print "NADA: So, you're "+ str(age) + " old, " + height + " tall and " +weight+ " heavy."