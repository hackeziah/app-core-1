from app.celery import celery as app

@app.task
def download(url, filename):
    print("jelllll")
    # """
    # Download a page and save it to the BASEDIR directory
    #   url: the url to download
    #   filename: the filename used to save the url in BASEDIR
    # """
    # response = urllib.request.urlopen(url)
    # data = response.read()
    # with open(BASEDIR+"/"+filename,'wb') as file:
    #     file.write(data)
    # file.close()

# @app.task
# def list():
#     """ Return an array of all downloaded files """
#     return os.listdir(BASEDIR)
