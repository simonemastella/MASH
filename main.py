HASH_LEN=1024
def hash(message):
    result = ''.join(format(ord(i), 'b') for i in message)
    while len(result)!=HASH_LEN: 
        if len(result)<HASH_LEN:
            size=''.join(format(ord(i), 'b') for i in str(len(result)))
            result+=size+result
        if len(result)>HASH_LEN:
            result=bin(int(result[:HASH_LEN],2)+int(result[HASH_LEN:],2))
            result=result[2:]
    partOne=""
    for i in range(0, HASH_LEN, 4):
        partOne+=result[i]
    partTwo="" 
    while len(partTwo)!=HASH_LEN/4:
        zero,uno=0,0
        if len(partTwo)<HASH_LEN/4:
            for c in result:
                if c =="0":
                    zero+=1
                if c=="1":
                    uno+=1
            zero=bin(zero)
            uno=bin(uno)
            add=bin(int(zero[2:])+int(uno[2:]))
            partTwo+=zero[2:]+uno[2:]+add[2:]
        if len(partTwo)>HASH_LEN/4:
            partTwo=bin(int(partTwo[:256],2)+int(partTwo[256:],2))
            partTwo=partTwo[2:]
    partThree=bin(int(result[:256],2)+int(result[256:512],2)+int(result[512:768],2)+int(result[768:1024],2))
    partThree=partThree[2:258]
    partFour=bin(int(partOne,2)+int(partTwo,2)-int(partThree,2))
    partFour=partFour[2:258]
    final=""
    partOne=(int(partOne,2)+int(result[:256],2))
    partTwo=(int(partTwo,2)+int(result[256:512],2))
    partThree=(int(partThree,2)+int(result[512:768],2))
    partFour=(int(partFour,2)+int(result[768:1024],2))
    final=bin(partTwo+partThree-partOne+partFour)
    final=str(int(final[2:250],2))
    final=[final[i:i+3] for i in range(0, len(final), 3)]
    alnum='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    mash=""
    for num in final:
        mash+=alnum[int(num)%len(alnum)]
    return mash

if __name__ == '__main__':
    print(hash(input("Mash of: ")))