import requests, xml.dom.minidom as xmlget, os

class bcolors:
    HIJAU = '\x1b[0;32m'
    MERAH = '\x1b[01;31m'
    NORMAL = '\x1b[0m'
    CYAN = '\x1b[0;36m'
    BIRU = '\x1b[0;34m'
    PUTIH = '\x1b[1;37m'


def main():
    response = requests.get('http://data.bmkg.go.id/autogempa.xml')
    result = response.text
    save = open('result.xml', 'w')
    save.write('%s' % result)
    save.close()
    rxml = xmlget.parse('result.xml')
    Tanggal = rxml.getElementsByTagName('Tanggal')[0].firstChild.data
    Jam = rxml.getElementsByTagName('Jam')[0].firstChild.data
    Lintang = rxml.getElementsByTagName('Lintang')[0].firstChild.data
    Bujur = rxml.getElementsByTagName('Bujur')[0].firstChild.data
    Magnitude = rxml.getElementsByTagName('Magnitude')[0].firstChild.data
    Kedalaman = rxml.getElementsByTagName('Kedalaman')[0].firstChild.data
    Wilayah = rxml.getElementsByTagName('Wilayah1')[0].firstChild.data
    Potensi = rxml.getElementsByTagName('Potensi')[0].firstChild.data
    print (' Tanggal     : {}').format(Tanggal)
    print (' Jam         : {}').format(Jam)
    print bcolors.CYAN
    print (' Lintang     : {}').format(Lintang)
    print (' Bujur       : {}').format(Bujur)
    print (' Magnitude   : {}').format(Magnitude)
    print (' Kedalaman   : {}').format(Kedalaman)
    print bcolors.HIJAU
    print (' Wilayah     : {}').format(Wilayah)
    print (' Potensi     : {}').format(Potensi)


os.system('cls' if os.name == 'nt' else 'clear')
print bcolors.BIRU
print '[S]====================================================[S]'
print '[A]_ _|  \\  | ____| _ \\   ___| ____|  \\  |  _ \\   \\    [A]'
print '[D]  |    \\ | |    |   | |     __|   |\\/ | |   | _ \\   [D]'
print '[B]  |  |\\  | __|  |   | |   | |     |   | ___/ ___ \\  [B]'
print '[O]___|_| \\_|_|   \\___/ \\____|_____|_|  _|_|  _/    _\\ [O]'
print '[Y]====================================================[Y]'
print bcolors.MERAH
print '~=[+]=========================================[+]=~'
print '  [+]               ~=[INFO]=~                [+]  '
print '~=[+]=========================================[+]=~'
print '  [+]      ~=[CODDED BY TUANSADBOYS]=~        [+]  '
print '~=[+]=========================================[+]=~'
print '~=[+]DEVILS UNION HURTED,INDONESIA CYBER MAFIA[+]=~'
print '~=[+]=========================================[+]=~'
print '~=[+]     ~=[https/github.com/DangerMr]=~     [+]=~'
print '~=[+]=========================================[+]=~'
print '~=[+]          ~=[+6288703041772]=~           [+]=~'
print '~=[+]=========================================[+]=~'
print bcolors.HIJAU
print 'MENGAMBIL INFO DARI BMKG'
print bcolors.NORMAL
print
if __name__ == '__main__':
    main()
    if os.path.exists('result.xml'):
        os.remove('result.xml')
    else:
        print 'The file does not exists'
    print bcolors.NORMAL
