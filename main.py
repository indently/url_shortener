import requests

# Function to shorten any link with a custom name
def shorten_link(full_link, link_name):
    API_KEY = 'YOU_API_KEY'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')
    # Gets the relevant information we need
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)


# Take user input
link = input('Enter a link: >> ')
name = input('Give your link a title: >> ')

# Call the function to shorten the link
shorten_link(link, name)
