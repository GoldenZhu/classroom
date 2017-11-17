import web

db = web.database(dbn='sqlite', db='MovieSite.db')
render = web.template.render('templates/')

urls = (
	'/', 'index',
	'/movie/(\d+)', 'movie',
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
		print movie_id
		print condition
		movie = db.select('movie', where=condition)[0]
		return render.movie(movie)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()



