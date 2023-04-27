
# Biến toàn cục:
Sbox = [
        ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'], 
        ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'], 
        ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'], 
        ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'], 
        ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'], 
        ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'], 
        ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'], 
        ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'], 
        ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'], 
        ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'], 
        ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'], 
        ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'], 
        ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'], 
        ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'], 
        ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'], 
        ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
        ]
#==============================================================================
def hexToDec(char_hex): # str_hex 4bits => int
    try:
        result=int(char_hex)
        return result
    except ValueError:
        #Chữ cái
        if char_hex == 'A':
            return 10
        elif char_hex == 'B':
            return 11
        elif char_hex == 'C':
            return 12
        elif char_hex == 'D':
            return 13
        elif char_hex == 'E':
            return 14
        return 15
#==============================================================================
def SubByte(state): # (4x4) => (4x4)
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            hang = hexToDec(byte[0])
            cot = hexToDec(byte[1])
            state[i][j]=Sbox[hang][cot]
    return state
#==============================================================================
def ShiftRows(state): # list_str => 4x4
    # Tạo ma trận 4x4 đã sắp xếp lại vị trí đúng shiftRows
    shiftRows = [
        [state[0][0], state[0][1], state[0][2], state[0][3]],
        [state[1][1], state[1][2], state[1][3], state[1][0]],
        [state[2][2], state[2][3], state[2][0], state[2][1]],
        [state[3][3], state[3][0], state[3][1], state[3][2]]
        ]
    return shiftRows
#==============================================================================
def hexToBin(strHEX):   # 1 byte hexa => str_bin_4_bits
    dec_x = hexToDec(strHEX)#Đưa về dạng thập phân
    str_bin = bin(dec_x)[2:] # Đưa về dạng nhị phân, và cắt bỏ '0b'
    if len(str_bin)==1:
        str_bin = '000'+str_bin
    elif len(str_bin)==2:
        str_bin = '00'+str_bin
    elif len(str_bin)==2:
        str_bin = '0'+str_bin
    return str_bin
#==============================================================================
def binToHex(str_bin_8bits): # str bin => str hex
    # Chuyển sang thập phân
    dec = int(str_bin_8bits,2)
    # Chuyển sang hex
    hexa = hex(dec)
    return hexa
#==============================================================================
def BinXorBin(strA, strB): # str xor str => str
    strA = [int(x)^int(y) for x,y in zip(strA, strB)]
    # chuyển list<str> -> str
    strA = "".join(map(str, strA))
    return strA
#==============================================================================
def HexXorHex(charA, charB): # str hex xor str hex => str hex
    # Đổi A, B thành bin
    bin_A = hexToBin(charA)
    bin_B = hexToBin(charB)
    # Xor
    bin_AB = BinXorBin(bin_A, bin_B)
    return binToHex(bin_AB) # Đổi về hexa
#==============================================================================
def HEXxHEX(strA, strB): # A,B là 1 byte hex => str_bin_8_bits
    if strA=='01':
        return hexToBin(strB)
    if strA=='02':
        # Chuyển strB thành nhị phân
        bin_strB = hexToBin(strB)
        # Dịch trái 1 bit
        strB = bin_strB[1:] + '0'
        # Nếu bit bên trái cùng của bin_strB == 1 => xor với '1B'
        if bin_strB[0]==1:
            strB = BinXorBin(strB, '00011011')
        return strB
    # Nhân với '03'
    strNhan02 = HEXxHEX('02', strB)
    bin_B = hexToBin(strB)
    return BinXorBin(strNhan02, bin_B)
#==============================================================================
def MixClolumn(state):
    A = [
        ['02','03','01','01'],
        ['01','02','03','01'],
        ['01','01','02','03'],
        ['03','01','01','02']
        ]
    Tich = [['' for i in range(4)] for i in range(4)] # (4x4)
    # Nhân ma trận:
    for i in range(4):
         for j in range(4):
             list_bin = [] # list các chuỗi 8bits đã nhân
             for k in range(4):
                 list_bin.append(HEXxHEX(A[i][k], state[k][j]))
             kq = list_bin[0]
             # Xor các chuỗi bits trong list_bin
             for x in range(1,len(list_bin)):
                 kq = BinXorBin(kq, list_bin[x])
             Tich[i][j] = binToHex(kq)
    return Tich
#==============================================================================
def AddRoundKey(state, key): #(4x4) xor (4x4) => (4x4)
    for i in range(4):
        for j in range(4):
            state[i][j] = HexXorHex(state[i][j], key[i][j])
#==============================================================================







