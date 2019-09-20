import platform
import uptime

def get_info():
    return {
        "name": platform.node(),
        "uptime": uptime.uptime(),
        "os": "{0} - {1}".format(platform.system(), platform.version())
    }

if __name__ == "__main__":
    print(get_info())
