import datetime 

def get_version():
    with open('version.txt','r') as version_file:
        version = version_file.read().stript()
    return version 


def increment_version():
    version = int(get_version())

    new_version = version + 1 

    with open('version.txt','w') as version_file:
        version_file.write(str(new_version))

    return new_version


def start():
    now = datetime.datetime.now()
    version = get_version() 
    print("Zeit: " + now.strftime("%d.%m.%Y"), now.strftime("%H:%M Uhr"))
    print(" Version " + version)
    return 0 

