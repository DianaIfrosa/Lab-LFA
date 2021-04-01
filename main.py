import sys

#input data structures
list=[]
#list of words
words=[]
#dictionary of states
states={}

states["S"]=[] # start
states["N"]=[] # normal
states["F"]=[] # finish

#store them in a set for easier validation
all_states=set()

transitions=[]

def Read():
    f=open("date.in")

    #skip comments
    for line in f:
        if line[0]!='#':
         list.append(line.strip())

    f.close()

    poz=0
    n=len(list)

    while poz<n:
        if list[poz].find("Sigma")!=-1:
            poz+=1
            while list[poz]!="End":
                words.append(list[poz])
                poz+=1
            #current position = end
            poz+=1

        if list[poz].find("States")!=-1:
            poz+=1
            #dictionary with keys S,F,N-normal and add states
            while list[poz]!="End":
                transition_tuple=[]
                transition_tuple=list[poz].split(",")
                all_states.add(transition_tuple[0])
                if len(transition_tuple)==1:
                    states["N"].append(transition_tuple[0])
                elif len(transition_tuple)==2:
                        if transition_tuple[1].strip()=="S":
                            states["S"].append(transition_tuple[0])
                        elif transition_tuple[1].strip()=="F":
                            states["F"].append(transition_tuple[0])
                else: #length is 3 so initial and final state
                    states["F"].append(transition_tuple[0])
                    states["S"].append(transition_tuple[0])

                poz+=1
            poz+=1 #skip "end"

        if list[poz].find("Transitions") != -1:
            poz+=1
            while list[poz] != "End":

                transition_tuple=list[poz].split(",")
                transitions.append(tuple(transition_tuple))

                poz+=1
            poz+=1
        poz+=1

def Output():
    print("The states are:", states)
    print("The transitions are:", transitions)
    print("The words are:",  words)

def Validate():
    #many initial states
    if len(states["S"])!=1:
        print("There are many initial states!")
        return 0
    #no final state
    if len(states["F"])==0:
        print("There is no final state!")
        return 0
    for trans in transitions:
        if trans[1] not in words:
            print("Invalid word!")
            return 0
        if trans[0] not in all_states:
            print("Invalid state!")
            return 0
        if trans[2] not in all_states:
            print("Invalid state!")
            return 0

    return 1

def ValidateInput():

  if Validate()==0:
    print("Input is not valid!")
  else:
    print("Valid input!")
    DFA()


def DFA():

    s=sys.argv[1:]
    #s=input("word:")
    lg=len(s)
    current_state=states["S"][0]
    i=0
    rej=0 #whether it was aborted or not
    lg_tranz=len(transitions) #how many transitions i have
    ok=0
    while i<lg:
      ok=0 #whether i find a good transitions or not
      for j in range(lg_tranz):
          if transitions[j][0]==current_state: # i have found a transition that starts from my current state
             if s[i:].find(transitions[j][1])==0: #verify if the word from transition is what i need
                 #the transition is valid
                ok=1
                current_state=transitions[j][2] #go to the next transition
                i=i+len(transitions[j][1]) #skip the previous word
                break

      if ok==0: #abort
          print("Rejected")
          rej=1
          break

    if rej==0 and current_state not in states["F"]:
        print("Rejected")
    elif current_state in states["F"]:
        print("Accepted")

def main():
    Read()
    Output()
    ValidateInput()
    
if __name__ == "__main__":
    main()



    



