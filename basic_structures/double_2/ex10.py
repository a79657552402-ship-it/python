
# Посмотрите видео и повторите код: https://www.youtube.com/watch?time_continue=562&v=LRudk3FQLoM&embeds_referring_euri=https%3A%2F%2Fyastatic.net%2Fvideo-player%2F0x85db8230c45%2Fpages-common%2Fyoutube%2Fyoutube.html&source_ve_path=Mjg2NjY&feature=emb_logo

def main():
    d = {'website':'google', 'url':'google.ru'}
    try:
        data = d['url']
    except:
        data = 'https://'
    else:
        data = data.upper()

    print(data)


main()