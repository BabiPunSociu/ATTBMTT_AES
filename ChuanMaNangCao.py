import AES_MaHoa
import AES_SinhKhoa

# import re để sử dụng regular expression
import re
def nhap64bits(mes):
    while True:
        _input = input(mes)
        # Thay thế các kí tự khác "chữ cái hexa hoặc số" bởi chuỗi rỗng
        _input = re.sub('[^A-F0-9]+', '', _input)
        # Kiểm tra input có đủ 16 kí tự ~ 64 bits không?
        if len(_input)== (32):
            return _input

if __name__=='__main__':
    # Input (M_64bits, K_64bits)
    M = nhap64bits('Nhập bản rõ 64 bits (dạng hexa): M = ')
    K = nhap64bits('Nhập khóa 64 bits (dạng hexa): K = ')
    
    W0 = K[0:8]
    W1 = K[8:16]
    W2 = K[16:24]
    W3 = K[24:]
    state = AES_SinhKhoa.CreateMatrix4x4(M) #(4x4)
    
    for i in range(10):
        # Sinh khóa
        W0, W1, W2, W3 = AES_SinhKhoa.SinhKhoa(W0, W1, W2, W3, i)
        # Tạo key (4x4)
        key=[]
        key.append(W0)
        key.append(W1)
        key.append(W2)
        key.append(W3)
        # Mã hóa
        # SubByte
        state = AES_MaHoa.SubByte(state)
        # ShiftRows
        state = AES_MaHoa.ShiftRows(state)
        # MixColumns
        if i<10:
            state = AES_MaHoa.MixClolumn(state)
        # AddRoundKey
        state = AES_MaHoa.AddRoundKey(state, key)