import os
import glob

from icrawler.builtin import GoogleImageCrawler

fpath = "/Users/wonjunhui/Desktop/craw_image_4/*.*"
i=788
for path in glob.glob(fpath):
    # name = str(int(path.split('.')[0][-6:]))
    if path.split('/')[5][0:2] == "00":
        # fpath_r = os.rename(path,path[:38]+path.split('/')[5][2:].split('.')[0]+'.'+path.split('/')[5][2:].split('.')[1])
        # print(path.split('/')[5][2:].split('.')[0]+'.'+path.split('/')[5][2:].split('.')[1])
        name = int(path.split('/')[5][2:].split('.')[0])+788
        fpath_r = os.rename(path,path[:38]+str(name)+'.'+path.split('/')[5][2:].split('.')[1])
        # fpath_r = os.rename(((str(path.split('/')[5][2:].split('.')[0])+788))+'.'+path.split('/')[5][2:].split('.')[1])
    # print(path.split('/')[5][0:2])

    # print(path.split('/')[5].split('.')[1])

    # fpath_r = os.rename(path,path[:38]+name+"."+path.split('.')[1])
    # print(path[:38]+name+"."+path.split('.')[1])
    # i = i+1
# google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
#                                     storage={'root_dir': '/Users/wonjunhui/Desktop/craw_image_4'})
# try:
#     google_crawler.crawl(keyword='연예인', max_num=1000,
#                      # date_min=None, date_max=None,
#                      min_size=(200,200), max_size=None)
# except:
#     print("요류")

