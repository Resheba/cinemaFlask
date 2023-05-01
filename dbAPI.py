import json, aiohttp, random

TOKEN = ''


async def searchContentAIO(query: str):
  try:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/search?title={query}&token={TOKEN}'
      ) as request:
        response_set = json.loads(await request.text()).get('results')

        ids_set = set()
        result = []
        for index, key in enumerate(
            map(lambda x: x.get('kinopoisk_id'), response_set)):
          if key in ids_set: continue
          if len(ids_set) > 19: break
          ids_set.add(key)
          result.append(response_set[index])

    return result
  except Exception as ex:
    print('searchContentAIO', ex)


async def catContentAIO(cat: str = '', type: str = '', year: str | int = ''):
  try:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/json?token={TOKEN}&cat={cat}&type={type}&year={str(year)}'
      ) as request:
        response_set = json.loads(await request.text()).get('results')

        ids_set = set()
        result = []
        for index, key in enumerate(
            map(lambda x: x.get('kinopoisk_id'), response_set)):
          if key in ids_set: continue
          if len(ids_set) > 30: break
          ids_set.add(key)
          result.append(response_set[index])

    return result
  except Exception as ex:
    print('catContentAIO', ex)


# async def searchContent(query: str):
#   try:
#     request = requests.get(
#       f'https://bazon.cc/api/search?title={query}&token={TOKEN}')
#     response_set = json.loads(request.text).get('results')
#     return response_set
#   except Exception as ex:
#     print('searchContent', ex)


async def getContentAIO(kp_id: int):
  try:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/search?kp={kp_id}&token={TOKEN}') as request:
        response = json.loads(await request.text()).get('results')[-1]
    return response
  except Exception as ex:
    print('getContentAIO', ex)


async def getMainMenuFilmsAIO():
  try:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/json?token={TOKEN}&type=film&page=1'
      ) as request:
        response = json.loads(await request.text()).get('results')

        ids_set = set()
        result = []
        for index, key in enumerate(
            map(lambda x: x.get('kinopoisk_id'), response)):
          if key in ids_set: continue
          ids_set.add(key)
          result.append(response[index])

    return result[:12]
  except Exception as ex:
    print('getMainMenuFilmsAIO', ex)


async def getMainMenuSerialsAIO():
  try:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/json?token={TOKEN}&type=serial&page=1'
      ) as request:
        response = json.loads(await request.text()).get('results')

        ids_set = set()
        result = []
        for index, key in enumerate(
            map(lambda x: x.get('kinopoisk_id'), response)):
          if key in ids_set: continue
          ids_set.add(key)
          result.append(response[index])

    return result[:12]
  except Exception as ex:
    print('getMainMenuSerialsAIO', ex)


async def getMainMenuMultsAIO():
  try:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/json?token={TOKEN}&type=film&page=1&cat=мультфильм'
      ) as request:
        response = json.loads(await request.text()).get('results')

        ids_set = set()
        result = []
        for index, key in enumerate(
            map(lambda x: x.get('kinopoisk_id'), response)):
          if key in ids_set: continue
          ids_set.add(key)
          result.append(response[index])

    return result[:6]
  except Exception as ex:
    print('getMainMenuMultsAIO', ex)


async def getRandomRecByCatAIO(cat: str):
  try:
    page = random.randint(0, 20)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/json?token={TOKEN}&type=all&page={page}&cat={cat}'
      ) as request:
        response = json.loads(await request.text()).get('results')

        response = random.sample(response, 4)

        # ids_set = set()
        # result = []
        # for index, key in enumerate(map(lambda x: x.get('kinopoisk_id'), response)):
        #   if key in ids_set: continue
        #   ids_set.add(key)
        #   result.append(response[index])

    return response
  except Exception as ex:
    print('getRandomRecByCatAIO', ex)


async def getFilmsByCatAIO(cat: str):
  try:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
      async with session.get(
          f'https://bazon.cc/api/json?token={TOKEN}&type=film&page=1&cat={cat}'
      ) as request:
        response = json.loads(await request.text()).get('results')

        ids_set = set()
        result = []
        for index, key in enumerate(
            map(lambda x: x.get('kinopoisk_id'), response)):
          if key in ids_set: continue
          ids_set.add(key)
          result.append(response[index])

    return result
  except Exception as ex:
    print('getFilmsByCatAIO', ex)
