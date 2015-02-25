# import web

# urls = (
# 	'/','index'
# 	)

# app = web.application(urls,globals())
# render = web.template.render('templates/')

# class index:
# 	def GET(self):
# 		greeting = 'Hello World'
# 		return render.index(greeting)

# if __name__ == '__main__':
# 	app.run()


# import web

# urls = (
#   '/hello', 'Index'
# )


# app = web.application(urls, globals())

# render = web.template.render('templates/')

# class Index(object):
#     def GET(self):
#         form = web.input(name="Nobody", greet='Hello there')
#         #greeting = "Hello, %s" % form.name
       
#     	greeting = "%s, %s" % (form.greet, form.name)
# 	return render.index(greeting)
# 		# if form.greet:
#   #   		greeting = "%s, %s" % (form.greet, form.name)
#   #   		return render.index(greeting = greeting)
# 		# else:
#   #   		return "ERROR: greet is required."

# if __name__ == "__main__":
#     app.run()

#http://localhost:8080/hello?name=Loren
#http://localhost:8080/hello?name=Loren&greet=Hola



import web

urls = (
	'/hello', 'Index',
	)

app = web.application(urls,globals())

render = web.template.render('templates/', base='layout')

class Index(object):
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(name='Nobody', greet='hello')
		greeting = "%s, %s" % (form.greet,form.name)
		return render.index(greeting)

if __name__ == "__main__":
	app.run()

