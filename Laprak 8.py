# # Materi 3
# with open('mbox-short.txt') as handle:
#     count = 0
#     for line in handle:
#         count = count + 1
#     print('Line Count:', count)
    
# with open('mbox-short.txt') as handle:
#     hasil = handle.read()
# print("Ukuran: ", len(hasil) ,"bytes")
# print("Huruf dari belakang sendiri mundur 16 huruf adalah: " + hasil[-16::1])

# with open('mbox-short.txt') as handle:
#     count = 1
#     for line in handle:
#         if line.startswith("Date:") and count < 10:
#             count += 1
#             print(line.strip())  

# # # Materi 4
# handle = open('output.txt', 'w')
# tulisan = "teks ini akan dituliskan ke file\n "
# handle.write(tulisan)
# handle.close()

# handle = open('tidak-ada.txt')
# print(handle)