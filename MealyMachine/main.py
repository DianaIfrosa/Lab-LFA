#input data

n=0 #number of nodes
m=0 #number of transitions
start_state=""
final_states=[]
no_final_states=0
no_strings=0
list_strings=[]
transitions=[]

def Read():
    global n,m,start_state,final_states,no_strings,no_final_states,list_strings,transitions

    f=open("data.in")

    n,m= f.readline().split()
    n=int(n) #number of nodes
    m=int(m) #number of transitions

    for i in range (m):
        s=f.readline().split()
        transitions.append(tuple(s))

    transitions.sort() #for easier search

    start_state=f.readline().strip()

    final_states=f.readline().split()

    no_final_states=int(final_states[0])
    final_states.pop(0)

    no_strings = int(f.readline().strip())

    for i in range(no_strings):
        str=f.readline().strip()
        list_strings.append(str)

    f.close()

def Do():

    for i in range(no_strings):
        AcceptString(list_strings[i])

def AcceptString(string):

     curr_state=start_state
     rej=0 #rejected (whether it was aborted or not)
     output_string=""

     seq=[] #sequence

     i=0 #current position in string
     len_string=len(string)

     while i<len_string:
         ok=0 #whether i found a match or not for the current letter
         seq.append(curr_state) #update the sequence
         for trans in transitions:
             if trans[0]>curr_state: #use the fact that the transitions list is ordered
                 break
             if trans[0]==curr_state and trans[2]==string[i]: #match
                 curr_state=trans[1] #move to the following state
                 output_string+=trans[3] #update the output string
                 ok=1
                 i+=1
                 break
         if ok==0: #no match was found
             rej=1 #abort
             break

     seq.append(curr_state)

     if curr_state not in final_states:
         rej=1

     if rej==1:
        print("NO")
     else:
         print("YES")
         print(output_string)
         print("Sequence of states:", *seq)

def main():
    Read()
    Do()

if __name__ == "__main__":
    main()



