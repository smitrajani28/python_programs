import argparse
import requests

def DownloadFile(url, local_filename):
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 
perser = argparse.ArgumentParser()

perser.add_argument("url", help="enter url")
perser.add_argument("output", help="enter output")

args = perser.parse_args()

print(args.url)
print(args.output)
DownloadFile(args.url, args.output)