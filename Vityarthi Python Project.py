import matplotlib.pyplot as plt
import matplotlib.animation as animation

def classify_tds(tds):
    if tds<50:
        return "Poor"
    elif tds<150:
        return "Excellent"
    elif tds<500:
        return "Acceptable"
    elif tds<1000:
        return "Poor"
    else:
        return "Very Poor"
    
color_map={"Poor":"red", "Excellent":"green", "Good":"blue", "Acceptable":"orange",
           "Very Poor":"brown"}
def live_graph():
    fig, ax = plt.subplots(figsize=(10, 5))

    def update(frame):
        ax.clear()

        if len(l) == 0:
            ax.set_title("No TDS Data Available")
            return

        blocks = range(1, len(l) + 1)
        qualities = [classify_tds(t) for t in l]

        # Color for each bar
        colors = [color_map[q] for q in qualities]

        ax.bar(blocks, l, color=colors)
        ax.set_xlabel("Block Number")
        ax.set_ylabel("TDS (ppm)")
        ax.set_title("LIVE TDS Level Monitor")

        # Add quality label above each bar
        for i, t in enumerate(l):
            ax.text(i + 1, t + 20, qualities[i], ha='center')

        ax.set_xticks(blocks)
        ax.grid(axis='y', linestyle='--', alpha=0.4)

    ani = animation.FuncAnimation(fig, update, interval=1000)  # updates every 1 sec
    plt.show()

print("To check water purity and saving it")
l=[]
n=int(input("Enter number of blocks in the hostel:"))
while True:
    print("Type 1. To check the quality of water")        #introducing menu
    print("Type 2. To update the TDS of the block")
    print("Type 3. To remove any entry")
    print("Tyoe 4. To print the list containing entries of each block")
    print("Type 5. To Exit")
    print("Type 6. To Print Graph")
    f=int(input("Enter the choice:"))           #enter the choice
    if f==1:
        for i in range(n):              #to run for all values in list
            a=int(input("Enter the TDS of the water on the block"))
            if a<50:
                print("Water lacks minerals and not beneficial")
            

            elif a<150 and a>=50:
                print("Excellent water quality")
            

            elif a<300 and a>=150:
                print("Minerally tasty")
            

            elif a<500 and a>=300:
                print("Acceptable but less minerals")
            

            elif a<1000 and a>=500:
                print("Poor Quality, needs treatment")
            

            elif a>=1000:
                print("Very Poor and not acceptable quality")
            

            else:
                print("Error in the value entered, pls reconsider")

            l.append(a)                 #appending values in list

        print("The notable TDS of each block respectively is:", l)
    elif f==2:                          #updating the list
        b=int(input("Enter the block whose TDS value need to be changed:"))
        c=int(input("Enter the new TDS value:"))
        l[b-1]=c                        #assigning new value
        print("The updated list is:", l)

    elif f==3:                          #removing elements in list
        d=int(input("Enter the block whose value needs to be removed:"))
        if 1<=d<=len(l):
            k=l.pop(d-1)
            print("The updated list is:",l)
        else:
            print("Invalid block number")

    elif f==4:                          #displaying the list
        print("The list is:",l)

    elif f==5:
        print("Exitingggg....")
        break

    elif f==6:
        print("Opening LIVE TDS graph....")
        live_graph()

    else:
        print("The entered value is invalid")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
    




        
