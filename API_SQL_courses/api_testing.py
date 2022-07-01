import requests
import responses

APIKEY = "dbf00bd534c684628f03620fb1982f8f"
TOKEN = "07fffb2ee7549a6aac240bcc69eed65a08c9b656feaf7ffdf0a8b09be6ff1e82"
URL = "https://trello.com/"


def get_user_boards():
    """
    This function returns information about all boards that the user has access to
    :return: list of dict
    """
    endpoint = "1/members/me/boards"
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return response_json


def get_board_id(name):
    """
    Returns the id of the specified board
    :param name: name of the board
    :return: int
    """
    id = None
    response = get_user_boards()
    for board in response:
        if board['name'] == name:
            id = board['id']
            break

    if id is None:
        print("No board found with the name: {}".format(name))
    return id


def update_board(name, **kwargs):
    """
    Updates boards information
    :param name: name of the board to be updated
    :param kwargs: board's parameters to be updated. The ful list is here: https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-put
    :return: None
    """
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_board(name):
    """
    Deleted the board
    :param name: board name
    :return:  None
    """
    board_id = get_board_id(name)
    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.text
    print(response_json)


def create_new_board(name):
    """
    Create a new board
    :param name: new board name
    :return: None
    """
    endpoint = "1/boards/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    response = requests.post(url=URL + endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


# AN my code start

def create_new_list(board_name, list_name):
    board_id = get_board_id(board_name)
    endpoint = URL + "1/lists"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': list_name,
        'idBoard': board_id
    }

    response = requests.request(
        "POST",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.text
    print(response_json)


def get_list_id(board_name, list_name):
    board_id = get_board_id(board_name)
    endpoint = "1/boards/{}/lists".format(board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }
    response = requests.get(url=URL + endpoint, params=params)
    response_json = response.json()

    id = None

    for list in response_json:
        if list['name'] == list_name:
            id = list['id']
            break

    if id is None:
        print("No list found with the name: {}".format(list_name))
    return id


def create_new_card(board_name, list_name, card_name):
    endpoint = URL + "1/cards"
    list_id = get_list_id(board_name, list_name)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name,
        'idList': list_id
    }
    response = requests.request(
        "POST",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.text
    print(response_json)


def get_card_id(board_name, list_name, card_name):
    list_id = get_list_id(board_name, list_name)
    endpoint = "1/lists/{}/cards".format(list_id)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }
    response = requests.get(url=URL + endpoint, params=params)
    response_json = response.json()

    id = None

    for card in response_json:
        if card['name'] == card_name:
            id = card['id']
            break

    if id is None:
        print("No card found with the name: {}".format(card_name))
    return id


def update_card(board_name, list_name, card_name, **kwargs):
    card_id = get_card_id(board_name, list_name, card_name)
    print(card_id)
    endpoint = URL + "1/cards/{}".format(card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_card(board_name, list_name, card_name):
    card_id = get_card_id(board_name, list_name, card_name)
    endpoint = URL + "1/cards/{}".format(card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.text
    print(response_json)


def archive_list(board_name, list_name):
    list_id = get_list_id(board_name, list_name)
    endpoint = URL + "1/lists/{}/closed".format(list_id)
    print(list_id, endpoint)

    params = {
        'key': APIKEY,
        'token': TOKEN
    }
    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.text
    print(response_json)

def archive_list_2():
    url = "https://trello.com/1/lists/62be6304a18a9078f17cab0e/closed"

    query = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.request(
        "PUT",
        url,
        params=query
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.text
    print(response_json)


if __name__ == "__main__":
    # get_user_boards()
    # create_new_board("Test Automation 1")
    # update_board("Test Automation", desc="Add items to finish automation")
    # delete_board("Test Automation 1")
    # create_new_list(board_name="Test Automation 1", list_name="second list")
    # create_new_card(board_name="Test Automation 1", list_name="first list", card_name="card3")
    # update_card(board_name="Test Automation 1", list_name="first list", card_name="card2", desc="new description22")
    # get_card_id(board_name="Test Automation 1", list_name="first list", card_name="card2")
    # delete_card(board_name="Test Automation 1", list_name="first list", card_name="card3")
    #archive_list(board_name="Test Automation 1", list_name="second list") #does not work, not clear why status code 400
    archive_list_2() # copy from TRELLO REST IP site, does not work ,status 400
