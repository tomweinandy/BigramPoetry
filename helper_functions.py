

def true(tweet):
    condition = 'RT' not in tweet.text
    return condition


def conditions_met(tweet):
    conditions_list = ['RT' not in tweet.text,
                       len(tweet.text.split(' ')) > 2,
                       'http' not in tweet.text,
                       tweet.lang == 'en',
                       tweet.user.screen_name != 'BrigramPoetry']
    return all(conditions_list)