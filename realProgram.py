with open('version.txt','r') as version_file:
    version = version_file.read().strip()
print("Hello i am a test-version: "+ str(version))