from flask import Flask, render_template, request
from dbAPI import *

app = Flask(__name__)


@app.route('/search/')
async def view_search_page():
  q = request.args.get('q')
  context = {'results': [], 'q': q}
  if q:
    context['results'] = await searchContentAIO(query=q)
  # print(context['results'])
  return render_template('search.html', **context)


@app.route('/cat/')
async def view_cat_page():
  cat = request.args.get('cat') or ''
  type = request.args.get('type') or ''
  if cat or type: results = await catContentAIO(cat, type)
  else: results = []
  context = {'results': results, 'cat': cat.title(), 'type': type}
  return render_template('genres.html', **context)


# @app.route('/search/<query>')
# async def view_search_result(query):
#   results = (await searchContentAIO(query))
#   if results == None:
#     return await not_found(f'No content with query <b>{query}</b>.')
#   return str(results[:12])


@app.route('/')
async def index():
  films = await getMainMenuFilmsAIO()
  serials = await getMainMenuSerialsAIO()
  mults = await getMainMenuMultsAIO()
  _2023 = await catContentAIO(type='film', year=2023)
  comedies = await catContentAIO(cat='комедия', type='all')

  context = {
    'film_contents': films,
    'serial_contents': serials,
    'mults_contents': mults,
    '_2023': _2023,
    'comedies': comedies,
  }

  return render_template('index.html', **context)


@app.route('/content/<int:kp_id>')
async def view_content(kp_id):
  result = (await getContentAIO(kp_id))
  if result == None:
    return await not_found(f'No content with id <b>{kp_id}</b>.')
  info = result.get('info')
  rating = info.get('rating')
  context = {
    'kp_id': kp_id,
    'name': info.get('rus'),
    'year': info.get('year'),
    'country': info.get('country'),
    'director': info.get('director'),
    'genre': info.get('genre'),
    #'orig_name': info.get('orig'),
    'description': info.get('description'),
    'poster': info.get('poster'),
    #'max_qual': result.get('max_qual'),
    #'translation': result.get('translation'),
    'actors': info.get('actors'),
    #'rating_KP': rating.get('rating_kp'),
    'rating_IMDB': rating.get('rating_imdb'),
    #'title': info.get('rus'),
    'link': result.get('link'),
    'time': int(info.get('time')) // 60,
    'rec_contents': await
    getRandomRecByCatAIO(info.get('genre').split(',')[0])
  }
  return render_template('content.html', **context)


@app.errorhandler(404)
async def not_found(error):
  return error


@app.route('/support/')
async def view_support():
  return render_template('support.html')


app.run(host='0.0.0.0', port=81)
# if __name__ == "__main__":
#   from waitress import serve
#   serve(app, host="0.0.0.0", port=81)
