#tower of hanoi


def hanoi(n,a,b,c):
    # a => c
    if(n==0):
        return
    hanoi(n-1,a,c,b) # ย้าย a (ล,ก) -> b___c จุดพัก (ย้ายa,พักc,ไปb)
    print("จานที่ = ",n,"จาก = ",a,"ไป = ",c)
    hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")