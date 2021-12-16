import requests
import json
import time

def get_animals():
  print('getting animals')
  total_pages = 0
  current_page = 1
  MAX_BATCH = 100
  # for iterating to MAX_BATCH
  stored_animals = []
  updated_animals = []
  total_helped_animals = 0
  total_stored_animals = 0

  while(current_page != total_pages):
    # get the page of animals
    response = requests.get(
          'http://localhost:3123/animals/v1/animals?page='+ str(current_page),
      )
    if response.ok:
      # get total number of pages
      total_pages = response.json()['total_pages']

      # if the response is ok modify then reupload
      for animal in response.json()['items']:
        animal['friends'] = ['clayton']
        animal['name'] = animal['name'] + ' updated 1'
        stored_animals.append(animal)

        # if the animal list is at MAX_BATCH, post them back to server
        if len(stored_animals) == MAX_BATCH:
          total_stored_animals = total_stored_animals + len(stored_animals)
          # number of uploaded this time
          helped = post_animals(stored_animals)
          # add to total count
          total_helped_animals = total_helped_animals + helped
          updated_animals = updated_animals + stored_animals
          # restore to 0 to begin counting to batch again
          stored_animals = []
          

      # get next page
      print('page: {} of {}'.format(current_page, total_pages))
      current_page = current_page + 1

  # final upload of animals
  if(len(stored_animals) > 0):
    total_stored_animals = total_stored_animals + len(stored_animals)
    total_helped_animals = total_helped_animals + post_animals(stored_animals)

  print('DONE!')
  # print('updated animals: {}'.format(updated_animals))
  print('total helped animals {}'.format(total_helped_animals))
  print('total stored animals {}'.format(total_stored_animals))


def post_animals(stored_animals):
  ok = False
  helped_animals = 0
  # retry loop
  while not ok:
    response = requests.post(
            'http://localhost:3123/animals/v1/home',
            data=json.dumps(stored_animals)
        )
    ok = response.ok
    if response.ok:
      # get number of helped animals
      helped_animals = int(response.json()['message'].split(' ')[1])
      
      # doesn't seem to show the modified name value
      response = requests.get(
          'http://localhost:3123/animals/v1/animals/{}'.format(stored_animals[0]['id']))
      
    return helped_animals

if __name__ == '__main__':
  get_animals()
