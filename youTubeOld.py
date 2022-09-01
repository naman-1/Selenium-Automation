from selenium import webdriver as drive
import time
T = time.time()
chrome = drive.Chrome()
chrome.maximize_window()
def youtube():
    topTrending = []                                      #THIS WILL BE THE MAIN LIST WHICH WILLL BE HAVING ALL THE TRENDING VIDEO DETAILS   
    descriptionXpath = '//*[@id="description-text"]'      #These are the id for various things to be captured
    titleXpath = '//*[@id="video-title"]'                 #--------------------------------------------------
    viewsChannelClass = 'style-scope ytd-video-meta-block'#--------------------------------------------------
    timeClass = 'style-scope ytd-thumbnail'               #--------------------------------------------------
    chrome.get('https://www.youtube.com/feed/trending')   #Load Youtube trending page
    time.sleep(1)                                         #After loading the trending page wait
    for videoRank in range(1,51):
        videoDetail = {}                                  # THIS DICTIONARY IS CRTEATED TO STORE DETAILS OF INDIVIDUAL VIDEOS ## BY APPENDING THIS INTO LIST --topTrending
        videoTitle = chrome.find_elements_by_xpath(titleXpath)[videoRank].text              #All elements needed to be extracted in text format
        videoViewsChannel = chrome.find_elements_by_class_name(viewsChannelClass)[videoRank]#-----------------------
        videoTime = chrome.find_elements_by_class_name(timeClass)[videoRank].text           #-----------------------
        videoDescription = chrome.find_elements_by_xpath(descriptionXpath)[videoRank].text  #-----------------------
        commonViCh = videoViewsChannel.text.split()       #Channel name and views are extracted as one so they are splitted into individual terms
        videoViews = commonViCh[-5]
        videoChannel = commonViCh[:-5]
        videoDetail['Rank of video is'] = videoRank       #entering extracted data into dictionary #RANK
        videoDetail['Title of video is'] = videoTitle     #----------------------------------------#TITLE
        videoDetail['Views on video is'] = videoViews     #----------------------------------------#VIEWS
        videoDetail['Channel name is'] = videoChannel     #----------------------------------------#CHANNELS     
        videoDetail['Time of video is'] = videoTime       #----------------------------------------#TIME
        videoDetail['Details of video'] = videoDescription#----------------------------------------#DESCRIPTION
        topTrending.append(videoDetail)
    print(topTrending)
    print('time consumed in process is',(time.time() - T))
        
youtube()
