import boto3
import os
import time

def downloadDirectoryFroms3():
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('testpython0') 
    for obj in bucket.objects.filter(Prefix = 'my-app'):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key) # save to same path
        

def main():
    downloadDirectoryFroms3()
    t1 = time.perf_counter()

    size = (1200, 1200)
    
    t2 = time.perf_counter()
    
    source='/my-app'
    dest='/var/www/html'
    
    shutil.rmtree(dest)
    shutil.copytree(source, dest, copy_function=shutil.copy)

    print(f'Finished in {t2-t1} seconds')

if __name__ == '__main__':
 main()
