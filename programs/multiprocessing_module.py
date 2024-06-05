import requests
import concurrent.futures

def downloadFile(url, name):
    print(f"start downloading file{name+1}.jpg")
    response = requests.get(url)
    open(f"files/file{name+1}.jpg", "wb").write(response.content)
    print(f"downloaded file{name+1}.jpg")
if __name__ == '__main__':
    url = "https://picsum.photos/200/300"    

    # normal method
    # pros = []
    # for i in range(30):
    #     p = multiprocessing.Process(target = downloadFile, args=[url, i])
    #     p.start()
    #     pros.append(p)
    # for i in pros:
    #     i.join()

    # process pool method
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1= [url for i in range(100)]
        l2= [i for i in range(100)]
        results = executor.map(downloadFile, l1 ,l2)    