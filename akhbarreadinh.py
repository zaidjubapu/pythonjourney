from Win32com.client import Dispatch
def speak(str):
    # from Win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    speak.speak(str)
if __name__ == '__main__':
    speak("kaise ho zaid")