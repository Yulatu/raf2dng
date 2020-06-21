import struct

file_path = './img/test_uncompressed.RAF'
export_path = './dng/test.dng'


class RAFHeader:
    def __init__(self, filename):
        with open(filename, 'rb') as f:
            self.type_string = struct.unpack('>16s', f.read(16))[0]
            self.format_ver = struct.unpack('>4s', f.read(4))[0]
            self.camera_id = struct.unpack('>8s', f.read(8))[0]
            self.camera_str = struct.unpack('>32s', f.read(32))[0].decode("utf_8")
            self.offset_ver = struct.unpack('>4s', f.read(4))[0]
            self.offset_unk = struct.unpack('>20s', f.read(20))[0].decode("utf_8")
            self.offset_jpg_offset = struct.unpack('>1i', f.read(4))[0]
            self.offset_jpg_length = struct.unpack('>1i', f.read(4))[0]
            self.offset_CFA_header_offset = struct.unpack('>1i', f.read(4))[0]
            self.offset_CFA_header_length = struct.unpack('>1i', f.read(4))[0]
            self.offset_CFA_offset = struct.unpack('>1i', f.read(4))[0]
            self.offset_CFA_length = struct.unpack('>1i', f.read(4))[0]


class JPEG:
    def __init__(self, filename, offset, length):
        with open(filename, 'rb') as f:
            f.seek(offset)


class CFAHeader:
    def __init__(self, filename, offset, length):
        self.data = []
        with open(filename, 'rb') as f:
            f.seek(offset)
            self.count = struct.unpack('>1i', f.read(4))[0]
            for record in range(self.count):
                tag = struct.unpack('>1h', f.read(2))[0]
                size = struct.unpack('>1h', f.read(2))[0]
                data = struct.unpack('>'+str(int(size/4))+'i', f.read(size))[0]
                self.data.append({"id": tag, "size": size, "data": data})


class CFA:
    def __init__(self, filename, offset, length):
        with open(filename, 'rb') as f:
            f.seek(offset)


class RAF:
    def __init__(self, filename):
        self.header = RAFHeader(filename)
        # self.jpg = JPEG(filename, self.header.offset_jpg_offset, self.header.offset_jpg_length)
        self.CFA_header = CFAHeader(filename, self.header.offset_CFA_header_offset, self.header.offset_CFA_header_length)
        # self.CFA = CFA(filename, self.header.offset_CFA_offset, self.header.offset_CFA_length)

    def export_EXIF(self):
        pass

    def export_DNG(self, path):
        pass


if __name__ == '__main__':
    obj = RAF(file_path)
    pass
    # with open(FilePath, "rb") as f:
    #     # 循环读取一张图片，一次性读取1024个字节
    #     while True:
    #         strb = f.read(1024)
    #         if strb == b"":
    #             break
    #         print(strb)
