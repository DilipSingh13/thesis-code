import boto3
import os
import time
import concurrent.futures

def downloadDirectoryFroms3(directory):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('testpython0') # name of our bucket
    for obj in bucket.objects.filter(Prefix = directory): # for-loop will iterate all files inside the directory to be downloaded
        if not os.path.exists(os.path.dirname(obj.key)): # check if there is directory or not
            os.makedirs(os.path.dirname(obj.key)) # make directory if not exist
        bucket.download_file(obj.key, obj.key) # save all files to ngnix server path
        

def main():
    t1 = time.perf_counter()

    size = (1200, 1200)
    
    direct = [
        'my-app'
    ]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(downloadDirectoryFroms3, direct)
    
    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')

if __name__ == '__main__':
 main()
