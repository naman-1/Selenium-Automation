from selenium import webdriver as drive
import time
Time = time.time()
chrome = drive.Chrome()
chrome.maximize_window()
def youtube():
    topTrending = []                                      #THIS WILL BE THE MAIN LIST WHICH WILLL BE HAVING ALL THE TRENDING VIDEO DETAILS   
    chrome.get('https://www.youtube.com/feed/trending')   #Load Youtube trending page
    descriptionXpath = chrome.find_elements_by_xpath('//*[@id="description-text"]')           #These are the id for various things to be captured
    titleXpath = chrome.find_elements_by_xpath('//*[@id="video-title"]')                      #--------------------------------------------------
    viewsChannelClass = chrome.find_elements_by_class_name('style-scope ytd-video-meta-block')#--------------------------------------------------
    #timeClass = chrome.find_elements_by_class_name('style-scope ytd-thumbnail')               #--------------------------------------------------
    
    time.sleep(1)                                         #After loading the trending page wait
    for videoRank in range(1,51):
        videoDetail = {}                                  # THIS DICTIONARY IS CRTEATED TO STORE DETAILS OF INDIVIDUAL VIDEOS ## BY APPENDING THIS INTO LIST --topTrending
        videoTitle = titleXpath[videoRank].text           #All elements needed to be extracted in text format
        videoViewsChannel = viewsChannelClass[videoRank]  
        #videoTime = timeClass[videoRank].text             #-----------------------
        videoDescription = descriptionXpath[videoRank].text#-----------------------
        commonViCh = videoViewsChannel.text.split()       #Channel name and views are extracted as one so they are splitted into individual terms
        videoViews = commonViCh[-5]
        videoChannel = commonViCh[:-5]
        videoDetail['Rank of video is'] = videoRank       #entering extracted data into dictionary #RANK
        videoDetail['Title of video is'] = videoTitle     #----------------------------------------#TITLE
        videoDetail['Views on video is'] = videoViews     #----------------------------------------#VIEWS
        videoDetail['Channel name is'] = videoChannel     #----------------------------------------#CHANNEL     
        #videoDetail['Time of video is'] = videoTime       #----------------------------------------#TIME
        videoDetail['Details of video'] = videoDescription#----------------------------------------#DESCRIPTION
        topTrending.append(videoDetail)
    print(topTrending)
for i in range(10):
    youtube()
    print('time consumed in process is',time.time() - Time) 
print('time consumed in process is',time.time() - Time) 
