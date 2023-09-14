# youtube video indirici

from pytube import YouTube

def video_dowloander(youtube_link,url_to_dowloand):
    my_video = YouTube(youtube_link)
    my_video.streams.get_highest_resolution().download(url_to_dowloand)
    return my_video.title

try:
    youtube_linkk = input("İndirmek istediğiniz videounun url'sini giriniz :  ")
    url_to_dowloandd= input("İndirmek istediğiniz yerin url'sini giriniz :  ")
    print("Videonuz yükleniyor,lütfen bekleyiniz.")
    video = video_dowloander(youtube_linkk,url_to_dowloandd)
    print(f"{video} başarıyla indirildi.")
except:
    print("Video indirilemedi.İnternetinizi kontrol edin ve tekrar deneyin.")