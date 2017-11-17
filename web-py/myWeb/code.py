import web

db = web.database(dbn='sqlite', db='MovieSite.db')
render = web.template.render('templates/')

urls = (
	'/', 'index',
	'/movie/(\d+)', 'movie',
	'/cast/(.*)', 'cast',
)

class index:
    def GET(self):
        movies = db.select('movie')
        return render.index(movies)

    def POST(self):
		data = web.input()
		condition = r'title like "%' + data.title + r'%"'
		movies = db.select('movie', where=condition)
		return render.index(movies)


class movie:
	def GET(self, movie_id):
		movie_id = movie_id.encode('unicode-escape')
		condition = "id='" + movie_id +"'"
		movie = db.select('movie', where=condition)[0]
		return render.movie(movie)

class cast:
	def GET(self, cast_name):
		condition = r'casts like "%' + cast_name + r'%"'
		print condition
		movies = db.select('movie', where=condition)
		return render.index(movies)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()



