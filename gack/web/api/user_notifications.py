from gack.web.api import API


@API.route('/user_notifications', methods=['POST'])
def user_notifications():
    return 'user notifications here'
