import time

from arduino.app_utils import App

from arduino.app_bricks.video_imageclassification import VideoImageClassification

classification_stream = VideoImageClassification()

def loop():
    # You can replace this with any code you want your App to run repeatedly.

    def rottenTomato():
        print("Rotten Tomato")

    classification_stream.on_detect("rotten tomato", rottenTomato)

    def freshTomato():
        print("Fresh Tomato")

    classification_stream.on_detect("fresh tomato", freshTomato)

    def rottenPotato():
        print("Rotten Potato")

    classification_stream.on_detect("rotten potato", rottenPotato)

    def freshPotato():
        print("Fresh Potato")

    classification_stream.on_detect("fresh potato", freshPotato)

    def rottenOrange():
        print("Rotten Potato")

    classification_stream.on_detect("rotten orange", rottenOrange)

    def freshOrange():
        print("Fresh Orange")

    classification_stream.on_detect("fresh orange", freshOrange)

    def rottenOkra():
        print("Rotten Okra")

    classification_stream.on_detect("rotten okra", rottenOkra)

    def freshOkra():
        print("Fresh Okra")

    classification_stream.on_detect("fresh potato", freshOkra)    

    def rottenCucumber():
        print("Rotten Cucumber")

    classification_stream.on_detect("rotten cucumber", rottenCucumber)

    def freshCucumber():
        print("Fresh Cucumber")

    classification_stream.on_detect("fresh cucumber", freshCucumber)    

    def rottenCapsicm():
        print("Rotten Capsicm")

    classification_stream.on_detect("rotten capsicm", rottenCapsicm)

    def freshCapsicm():
        print("Fresh Capsicm")

    classification_stream.on_detect("fresh capsicm", freshCapsicm)    

    def rottenBitterGroud():
        print("Rotten Bitter Groud")

    classification_stream.on_detect("rotten bitter groud", rottenBitterGroud)

    def freshBitterGroud():
        print("Fresh Bitter Groud")

    classification_stream.on_detect("fresh bitter groud", freshBitterGroud)    

    def rottenBanana():
        print("Rotten Banana")

    classification_stream.on_detect("rotten banana", rottenBanana)

    def freshBanana():
        print("Fresh Banana")

    classification_stream.on_detect("fresh banana", freshBanana)    

    def rottenApple():
        print("Rotten Apple")

    classification_stream.on_detect("rotten apple", rottenApple)

    def freshApple():
        print("Fresh Apple")

    classification_stream.on_detect("fresh apple", freshApple)
    
    def all_detected(results):
        print("Results: ", results)

    classification_stream.on_detect_all(all_detected)
    
    time.sleep(10)


# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)
