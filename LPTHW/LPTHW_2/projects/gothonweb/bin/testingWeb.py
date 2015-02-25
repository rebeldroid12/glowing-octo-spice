
import web
        
urls = (
    '/(.*)', 'h'

	)

app = web.application(urls, globals())

render = web.template.render('templates/')

class hello:        
    def GET(self):
        #name = 'Bob'
        #return render.bob(name)
        return 'Hello World!!!!'

class h:
	def GET(self,name):
        
        #i = web.input(name=None)
        #return render.index(i.name)
        
		#name = 'Bob'
		return render.bob(name)


if __name__ == "__main__":
    app.run()


#http://webpy.org/tutorial3.en





