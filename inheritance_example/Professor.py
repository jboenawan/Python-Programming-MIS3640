from BabsonPerson import *

class Professor(BabsonPerson):
    def __init__(self, name, courses):
        BabsonPerson.__init__(self, name)
        self.courses = courses
    
    def get_courses(self):
        return self.courses

    def speak(self, utterance):
        return BabsonPerson.speak(self, "Folks, " + utterance)

    def isProf(obj):
        return isinstance(obj, Professor)

def main():
    prof1 = Professor("Zhi Li", "MIS 3640")
    print(prof1)
    print(prof1.speak("tatatatata"))
    print(prof1.get_courses())
    

if __name__ == '__main__':
    main()
