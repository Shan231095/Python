class multiplefunctions():
    def Subfields():
        print("Sub-fields in AI are:\nMachine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
        SubfieldsInAI="Sub-fields in AI are:\nMachine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing"
        return SubfieldsInAI

    def OddEven():
        num=int(input("Enter a Number:"))
        if((num%2)==0):
            print(num,"is Even number")
            OddEven="Even number"
        else:
            print(num,"is Odd number")
            OddEven="Odd number"
        return OddEven

    def Eligible():
        Gender=input("Enter the Gender:")
        Age=int(input("Enter the Age:"))
        if(Gender=="Female"):
            if(Age>=18):
                print("Eligible")
                EligibilityForMarriage="Eligible"
            else:
                print("Not Eligible")
                EligibilityForMarriage="Not Eligible"
        elif(Gender=="Male"):
            if(Age>=21):
                print("Eligible")
                EligibilityForMarriage="Eligible"
            else:
                print("Not Eligible")
                EligibilityForMarriage="Not Eligible"
        else:
            print("Not Valid")
            EligibilityForMarriage="Not Valid"
        return EligibilityForMarriage

    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=(sub1+sub2+sub3+sub4+sub5)
        print("Total=",Total)
        Percentage=((Total/500)*100)
        print("Percentage=",Percentage)
        FindPercent="Percentage"
        return FindPercent

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        Area=((height*breadth)/2)
        print("Area Formula:(Height*Breadth)/2") 
        triangle="Area Formula:(Height*Breadth)/2"
        print("Area of the Triangle:",Area)
        triangle="Area"
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        Perimeter=height1+height2+breadth
        print("Perimeter Formula:Height1+Height2+Breadth")
        triangle="Perimeter Formula:Height1+Height2+Breadth"
        print("Perimeter of Traingle:",Perimeter)
        triangle="Perimeter"
        return triangle