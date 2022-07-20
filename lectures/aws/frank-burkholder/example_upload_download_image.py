import boto3

def print_s3_contents_boto3(connection):
    for bucket in connection.buckets.all():
        for key in bucket.objects.all():
            print(key.key)

if __name__ == '__main__':
    print("\nRunning script") 
    boto3_connection = boto3.resource('s3')
    print_s3_contents_boto3(boto3_connection)
    # upload a file
    bucket_name = 'frank-dsi-2' # make this bucket and artists subfolder beforehand on s3
    s3_client = boto3.client('s3')
    s3_client.upload_file('Casey_Kawaguchi.jpg', bucket_name, 'artists/Casey_in_subfolder.jpg')
    print("\nUploaded file")
    print_s3_contents_boto3(boto3_connection)
    # now download the file
    print("\nDownloaded file")
    s3_client.download_file(bucket_name, 'artists/Casey_in_subfolder.jpg', 'Casey_back_from_sf.jpg')
    print("\nFinished")
