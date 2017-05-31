#here we model a band using object oriented concep

class Musician(object): 
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoign, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bing","Bang","Bong"])
    
    def count_in(self):
        print("a one \n two \n three \n fo")
    
    def spontaneously_combust(self):
        print("whooosh, crackle, crackle")

class Band():
    def __init__(self):
        self.members = []
        
    def hire(self, hiree): #takes a musician as a parameter
        self.members.append(hiree)#add musician to member array
    
    def fire(self, firee): #create a new members array, excluding "firee"
        self.members = [m for m in self.members if m != firee]
        
    def play_gig(self, city):
        import random
        
        try:#we check if there is a drummer in the band, if so...
            drummer = random.choice([d for d in self.members #randomly select
                                    if str(type(d)) == 
                                    "<class '__main__.Drummer'>"])
            print("hello, " + city)
            drummer.count_in()#call the count_in function 
            for member in self.members: #print sounds for each member
                print(member.sounds)
            
        except IndexError: #if we have no drummer, then drummer array is empty
            print("no drummer :( \ncan't play!")
            
    def get_members(self): #accessor for members list
        return(self.members)
        
#this section is used to test the class
if __name__ == '__main__':
    
    #instantiate objects
    gerald = Guitarist()
    bob = Bassist()
    don = Drummer()
    marker_guys = Band()
    
    #hire musicians, but no drummer
    marker_guys.hire(bob)
    marker_guys.hire(gerald)
    
    #access each member in band, print type of musician
    for i in range(0,len(marker_guys.get_members())):
        print(type(marker_guys.get_members()[i]))
    
    #attempt gig without drummer, should fail
    marker_guys.play_gig("townville")
    #hire drummer
    marker_guys.hire(don)    
    #attempt gig again
    marker_guys.play_gig("townville")
    #fire band
    marker_guys.fire(bob)
    marker_guys.fire(gerald)
    marker_guys.fire(don)