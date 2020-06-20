import struct

FilePath = './img/test.RAF'


class RAF:
    def __init__(self, filename):
        with open(filename, 'rb') as f:
            self.type_String = struct.unpack('>16s', f.read(16))[0]
            self.Format_Ver = struct.unpack('>4s', f.read(4))[0]
            self.Camera_Id = struct.unpack('>8s', f.read(8))[0]
            self.Camera_Str = struct.unpack('>32s', f.read(32))[0]
            self.offset_Ver = struct.unpack('>4s', f.read(4))[0]
            self.offset_Unk = struct.unpack('>20s', f.read(20))[0]
            self.offset_Jpg_Offset = struct.unpack('>4b', f.read(4))[0]
            # self.offset_Jpg_Length = struct.unpack('>4b', f.read(4))[0]
            # self.offset_CFA_Header_Offset = struct.unpack('>4b', f.read(4))[0]
            # self.offset_CFA_Header_Length = struct.unpack('>4b', f.read(4))[0]
            # self.offset_CFA_Offset = struct.unpack('>4b', f.read(4))[0]
            # self.offset_CFA_Length = struct.unpack('>4b', f.read(4))[0]


    def display_EXIF(self):
        pass


if __name__ == '__main__':
    obj = RAF(FilePath)
    pass
    # with open(FilePath, "rb") as f:
    #     # 循环读取一张图片，一次性读取1024个字节
    #     while True:
    #         strb = f.read(1024)
    #         if strb == b"":
    #             break
    #         print(strb)
